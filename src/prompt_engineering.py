import random

few_shot_examples = [
    # Promotions
    ("Save big on clearance items – up to 70% off!", "Promotions"),
    ("Introducing our new product line – available now!", "Promotions"),
    ("Exclusive deal: Subscribe now and get 2 months free", "Promotions"),
    ("Join our loyalty program for exclusive rewards!", "Promotions"),
    ("Discover our award-winning skincare products", "Promotions"),
    ("Reserve your seat now for our product launch webinar", "Promotions"),

    # Priority
    ("Deadline Approaching: Final drafts due by Friday", "Priority"),
    ("Incident Alert: Unexpected downtime in production", "Priority"),
    ("Reminder: Submit budget revisions by 5 PM", "Priority"),

    # Updates
    ("New Office Guidelines: Please review seating update", "Updates"),
    ("Quarterly Newsletter: Message from the CEO", "Updates"),
    ("Staff Bulletin: Remote work policy updates", "Updates"),
]

# Fix shuffle globally once
random.seed(38)
shuffled_examples = few_shot_examples.copy()
random.shuffle(shuffled_examples)

def build_prompt(email_text: str) -> str:
    shots = "\n\n".join([f'Email: "{ex[0]}"\nCategory: {ex[1]}' for ex in shuffled_examples])

    return f"""
You are an intelligent email assistant. Classify the email into one of: Priority, Updates, or Promotions.

Think:
- Does the email promote sales, offers, or marketing content? → Promotions
- Is it internal info or general company updates? → Updates
- Is it time-sensitive or requesting urgent action? → Priority

Examples:
{shots}

Now classify this email:
\"\"\"{email_text}\"\"\"

Category:"""
