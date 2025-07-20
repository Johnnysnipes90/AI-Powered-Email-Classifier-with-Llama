# AI-Powered-Email-Classifier-with-Llama
AI-powered inbox assistant to classify and prioritize emails using Llama's local LLM capabilities.

## 🚀 Project Description
This project demonstrates how to use a local LLaMA-based LLM (model.gguf) to classify email content into three meaningful categories: Priority, Updates, or Promotions. By leveraging prompt engineering, we integrate LLaMA with a real-world dataset to build a powerful, privacy-preserving inbox assistant that runs entirely offline.

### 💡 Key Features
- 🧠 Local LLM Inference using LLaMA

- ✉️ Email Categorization using prompt-based text classification

- 🔒 Offline & Privacy-Preserving processing

- 📦 Modular Code Structure for easy maintenance and scalability

- 📊 Exploratory Data Analysis (EDA) in Jupyter

- ✅ Ready for deployment via CLI or Streamlit

### 🧪 Technologies Used
- Python

- LLaMA.cpp (or Python bindings like llama-cpp-python)

- Pandas

- Prompt Engineering

- Streamlit (UI)

- Git

## 📁 Dataset
Custom CSV containing real-world styled emails with 3 labels:

- Priority

- Promotions

- Updates

## 🧠 Model Workflow Summary
- 1. Load and Preprocess Email Data

- 2. Load LLaMA model (model.gguf) locally

- 3. Craft Classification Prompt Template

- 4. Query model with each email to get predicted category

- 5. Store and Evaluate Results



# 📁 Project Structure
Use a well-organized, modular file structure:
``` bash
llama-email-classifier/
├── data/
│   └── email_categories_data.csv
├── model/
│   └── model.gguf  # Pre-downloaded LLaMA model
├── notebooks/
│   └── 01_data_exploration.ipynb
│   └── 02_llama_classification.ipynb
├── src/
│   ├── classifier.py
│   ├── llama_initializer.py
│   └── prompt_engineering.py
├── results/
│   └── classification_results.csv
├── README.md
├── requirements.txt
└── app.py  # Streamlit
```

## 
📦 Requirements.txt
```txt
Edit
llama-cpp-python
pandas
streamlit  
```

