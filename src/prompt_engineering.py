def create_prompt(email_text: str) -> str:
    return f"""Classify the following email into one of these categories:
- Priority
- Promotions
- Updates

Email:
\"\"\"
{email_text}
\"\"\"
Category:"""