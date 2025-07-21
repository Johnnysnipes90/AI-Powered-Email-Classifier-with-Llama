from src.prompt_engineering import create_prompt

def classify_email(llama_model, email_text):
    prompt = create_prompt(email_text)
    output = llama_model(prompt, max_tokens=10, stop=["\n"])
    return output["choices"][0]["text"].strip()