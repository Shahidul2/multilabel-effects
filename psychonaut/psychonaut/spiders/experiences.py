import scrapy

class ExperiencesSpider(scrapy.Spider):
    name = "experiences"
    allowed_domains = ["psychonautwiki.org"]
    start_urls = ["https://psychonautwiki.org/wiki/Experience_index"]

    def parse(self, response):
        # Step 1: Scrape all Experience links
        for a in response.css('div#mw-content-text li a'):
            title = a.css('::attr(title)').get()
            href = a.css('::attr(href)').get()
            if href and title and href.startswith("/wiki/Experience:"):
                full_url = response.urljoin(href)
                yield scrapy.Request(full_url, callback=self.parse_experience, meta={
                    'title': title,
                    'url': full_url
                })

    def parse_experience(self, response):
        title = response.meta['title']
        url = response.meta['url']
        content_selector = response.css("div#mw-content-text")
        content_html = content_selector.get()

        # Step 2: Extract Report section
        report_text = ""
        if 'id="Report"' in content_html:
            try:
                report_section = content_html.split('id="Report"')[1]
                report_text = report_section.split('<span class="mw-headline"', 1)[0]
                report_text = scrapy.Selector(text=report_text).xpath("string()").get().strip()
            except:
                report_text = ""

        # Step 3: Extract linked effects terms
        effects_terms = []
        if 'id="Effects_analysis"' in content_html:
            try:
                effects_section = content_html.split('id="Effects_analysis"')[1]
                effects_section = effects_section.split('<span class="mw-headline"', 1)[0]
                effects_selector = scrapy.Selector(text=effects_section)

                for a in effects_selector.css("a"):
                    link = a.css("::attr(href)").get()
                    text = a.css("::text").get()
                    if link and text and link.startswith("/wiki/"):
                        effects_terms.append(text.strip())
            except Exception as e:
                self.logger.warning(f"Failed to parse effects for {url}: {e}")
                effects_terms = []

        yield {
            'title': title,
            'url': url,
            'report_text': report_text,
            'effects_terms': list(set(effects_terms))
        }
