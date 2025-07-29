# 📧 AI-Powered Email Classifier with LLaMA

AI-powered inbox assistant to classify and prioritize emails using LLaMA's local LLM capabilities — completely offline, privacy-first, and elegantly packaged with Streamlit.

---

## 🚀 Project Description

This project demonstrates how to use a local LLaMA-based LLM (`.gguf` model) to classify email content into three meaningful categories:

- **Priority**
- **Updates**
- **Promotions**

By leveraging prompt engineering and few-shot examples, we integrate LLaMA with real-world styled email data to build a powerful, **privacy-preserving inbox assistant** that runs entirely offline — no cloud APIs required.

---

### 🔧 Features

- 🔍 Classify emails into: `Priority`, `Updates`, or `Promotions`
- 🌓 Toggle between Light and Dark Mode
- 🔀 Choose curated examples or generate random ones
- 💻 Fully offline — powered by a local quantized `.gguf` LLM model
- ⚡ Built with `tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf` (lightweight and fast!)

---

## 🧪 Technologies Used

- 🐍 Python 3.10+
- 🧠 [`llama-cpp-python`](https://github.com/abetlen/llama-cpp-python)
- 📊 Pandas
- 🧩 Prompt Engineering
- 🖼️ Streamlit
- 🧰 Streamlit Extras (`st_toggle_switch`, `add_vertical_space`)
- 🧪 Custom Dataset

---

## 📁 Dataset

A custom CSV dataset `email_categories_data.csv` simulating real-world email content, labeled with one of:

- `Priority`
- `Promotions`
- `Updates`

---

## 🧠 Model Workflow Summary

1. Load and preprocess email data  
2. Load quantized LLaMA `.gguf` model locally  
3. Craft structured few-shot classification prompt  
4. Query model with input email  
5. Extract and display predicted category  

---

# 📁 Project Structure
Use a well-organized, modular file structure:
``` bash
llama-email-classifier/
├── data/
│   └── email_categories_data.csv
├── model/
│   └── model.gguf  # Pre-downloaded LLaMA model
├── notebooks/
│   └── llama_classification.ipynb
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

### Clone this repository

```bash
git clone https://github.com/Johnnysnipes90/llama-email-classifier.git
cd llama-email-classifier
```

### Create a virtual environment
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### Install dependencies
```bash
pip install -r requirements.txt
```
```txt
llama-cpp-python
streamlit
pandas
pillow
streamlit-extras
```

### Download the Model
Place your quantized model file (e.g., tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf) in the model/ directory.

You can download TinyLLaMA from Hugging Face

## ▶️ Running the App
```bash
streamlit run app.py
```
## 🌍 Deploying to Streamlit Cloud
To deploy:

- Push this repo to your GitHub

- Go to https://streamlit.io/cloud

- Connect your GitHub account and select this repo

- Set the Python version and dependencies using requirements.txt

- Add app.py as the main entry point

- ⚠️ Make sure to remove large model files or host them separately (or use smaller models due to file size limits)


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
