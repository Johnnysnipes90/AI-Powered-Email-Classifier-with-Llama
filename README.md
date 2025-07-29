# AI-Powered-Email-Classifier-with-Llama
AI-powered inbox assistant to classify and prioritize emails using Llama's local LLM capabilities.

## 🚀 Project Description
This project demonstrates how to use a local LLaMA-based LLM (model.gguf) to classify email content into three meaningful categories: Priority, Updates, or Promotions. By leveraging prompt engineering, we integrate LLaMA with a real-world dataset to build a powerful, privacy-preserving inbox assistant that runs entirely offline.

**Main Features:**
- 🔍 Classify emails into: `Priority`, `Updates`, or `Promotions`
- 🌓 Toggle between Light and Dark Mode
- 🔀 Use curated examples or generate random examples
- 💻 Runs fully offline — no external API required
- ⚡ Powered by `tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf` (quantized LLaMA model)

---

### 🧪 Technologies Used
- Python

- LLaMA.cpp (or Python bindings like llama-cpp-python)

- Pandas

- Prompt Engineering

- Streamlit (UI)

- Git
---

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


---

## 🛠️ Installation & Setup

### 1. Clone this repository

```bash
git clone https://github.com/Johnnysnipes90/llama-email-classifier.git
cd llama-email-classifier
```

### Create a virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```
```txt
llama-cpp-python
pandas
streamlit  
```

### Download the Model
Place your quantized model file (e.g., tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf) in the model/ directory.

You can download TinyLLaMA from Hugging Face

## ▶️ Running the App
```bash
streamlit run app.py
```


## 🧠 How It Works
The application uses few-shot prompting with curated examples representing each category. It builds a structured prompt that guides the LLaMA model to classify the new input.
**Sample prompt format
```txt
You are an intelligent email assistant. Classify the email into one of: Priority, Updates, or Promotions.

Think:
- Does the email promote sales, offers, or marketing content? → Promotions
- Is it internal info or general company updates? → Updates
- Is it time-sensitive or requesting urgent action? → Priority

Examples:
Email: "Save big on clearance items – up to 70% off!"
Category: Promotions

...

Now classify this email:
"""Your bank account has been suspended. Please verify now."""

Category:
```
The model generates the category name directly as output (e.g., Priority).


## 🧭 Future Improvements
While the current implementation uses the lightweight TinyLLaMA-1.1B model for local inference, performance could be greatly improved by:

- ✅ Replacing the model with a larger LLaMA variant (e.g., 7B or 13B)

- ✅ Using instruction-tuned models (e.g., Mistral-Instruct, LLaMA 2 Chat)

- ✅ Fine-tuning a classification head or using embeddings + supervised classifier

- ✅ Integrating RAG (Retrieval-Augmented Generation) with email history/context

## 📌 Use Cases
📥 Smart Email Filtering

🧑‍💼 Productivity Boosters for executives

📬 Helpdesk Ticket Routing

🧠 Natural Language Understanding for enterprise tools

✉️ Auto-tagging in CRMs or mail clients



## 🧑‍💻 Author
John Olalemi
📧 johnolalemi90@gmail.com
🌐 GitHub: github.com/Johnnysnipes90 
LinkedIn: www.linkedin.com/in/john-olalemi
