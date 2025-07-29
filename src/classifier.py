import re
from src.prompt_engineering import build_prompt

def classify_email(
    llm,
    email_text: str,
    temperature: float = 0.0,
    top_p: float = 0.9,
    max_tokens: int = 10,
    raw_prompt: str = None
) -> str:
    """
    Classify the email into Priority, Updates, or Promotions using the LLaMA model.

    Args:
        llm: The loaded LLaMA model instance.
        email_text: The content of the email.
        temperature: Temperature for model inference.
        top_p: Top-p sampling parameter.
        max_tokens: Maximum output tokens.
        raw_prompt: Optional custom prompt.

    Returns:
        Predicted category (string).
    """
    prompt = raw_prompt if raw_prompt else build_prompt(email_text)
    output = llm(prompt, max_tokens=max_tokens, temperature=temperature, top_p=top_p)
    raw = output['choices'][0]['text'].strip()

    match = re.search(r'\b(Priority|Updates|Promotions)\b', raw, re.IGNORECASE)
    return match.group(1).capitalize() if match else "Unknown"
