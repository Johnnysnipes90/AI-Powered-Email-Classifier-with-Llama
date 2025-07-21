import streamlit as st
from src.classifier import classify_email
from src.llama_initializer import load_llama_model

st.title("📧 AI-Powered Email Classifier")

email_text = st.text_area("Enter Email Content")
if st.button("Classify"):
    model = load_llama_model("model/model.gguf")
    category = classify_email(model, email_text)
    st.success(f"🧠 Predicted Category: {category}")