# 🧠 Multi-Label Effects Classification of Psychoactive Drugs

A transformer-based **multi-label text classification model** that predicts the **subjective psychological effects** of psychoactive substances from **user trip reports**. Due to a smaller dataset, we achieved **55%** accuracy.

---

## Example Prediction

-Input : I saw impossible geometry and felt a strong sense of ego death while colors melted around me.
-Predicted Effects: ['ego death', 'geometry', 'visual distortion', 'unity', 'time distortion']

## 📚 Source & Data

- **Source:** [PsychonautWiki](https://psychonautwiki.org/)
- **Scraping:** Custom Scrapy crawler
- **Reports:** 231 unique trip reports
- **Labels:** 19 subjective effect categories  
- **Split:** 80/20 train-test split

---

## 🧼 Preprocessing & Encoding

- Cleaned raw text data and filtered infrequent effects.
- Converted effect labels into multi-hot encoded vectors.
- Label mapping stored in: `effect_types_encoded.json`

---

## 🤖 Model Details

- **Model:** [`allenai/longformer-base-4096`](https://huggingface.co/allenai/longformer-base-4096)
- **Frameworks:** FastAI + Blurr (HuggingFace integration)
- **Task:** Multi-label classification
- **Loss:** `BCEWithLogitsLoss`
- **Threshold:** 0.2 for effect selection

---

## Files & Resources

All essential artifacts (model, dataloader, label mappings) are hosted here:  
🔗 [Google Drive Link](https://drive.google.com/drive/folders/1yVNpABTf2h8XN1leokWMYz6JCxAEaWAf?usp=drive_link)

- `effect-classifier-stage-1.pkl` – trained model
- `dls-effect-classifier.pkl` – fastai DataLoaders
- `effect_types_encoded.json` – label map

---



