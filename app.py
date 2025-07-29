import streamlit as st
from PIL import Image
from streamlit_extras.toggle_switch import st_toggle_switch
from streamlit_extras.add_vertical_space import add_vertical_space
from src.classifier import classify_email
from src.llama_initializer import load_llama_model

# --- PAGE CONFIG ---
st.set_page_config(page_title="AI Email Classifier", page_icon="📧", layout="wide")

# --- DARK MODE TOGGLE ---
dark_mode = st_toggle_switch(
    label="🌙 Dark Mode",
    key="dark_mode",
    default_value=True,
    label_after=True,
    inactive_color="#D3D3D3",
    active_color="#000000"
)

# --- CUSTOM CSS ---
st.markdown(
    f"""
    <style>
    html, body, .stApp {{
        background-color: {'#0E1117' if dark_mode else '#F8F9FA'};
        color: {'#FFFFFF' if dark_mode else '#1C1C1C'};
        font-family: 'Segoe UI', sans-serif;
    }}
    .email-box {{
        background-color: {'#1e1e1e' if dark_mode else '#ffffff'};
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }}
    .stTextArea textarea {{
        font-size: 16px !important;
        line-height: 1.6 !important;
        border-radius: 10px !important;
    }}
    .btn-classify button {{
        background-color: {'#4A90E2' if dark_mode else '#1f77b4'} !important;
        color: white !important;
        border-radius: 10px;
        font-weight: 600;
        font-size: 18px;
        padding: 10px 20px;
    }}
    .btn-classify button:hover {{
        background-color: {'#357ABD' if dark_mode else '#145a86'} !important;
    }}
    .footer {{
        text-align: center;
        color: {'#AAAAAA' if dark_mode else 'gray'};
        font-size: 15px;
        margin-top: 30px;
    }}
    .footer a {{
        color: {'#4A90E2' if dark_mode else '#0072C6'};
        text-decoration: none;
        margin: 0 10px;
    }}
    .footer a:hover {{
        text-decoration: underline;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- LOGO + TITLE ---
col1, col2 = st.columns([5, 10])
with col1:
    logo = Image.open("images/email_inbox.jpg")
    st.image(logo, width=150)
with col2:
    st.markdown("<h1 style='font-size: 38px;'>📧 AI-Powered Email Classifier</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size:17px; color: gray;'>Classify email messages intelligently using LLaMA.</p>", unsafe_allow_html=True)

add_vertical_space(1)

import random

# --- EXAMPLE EMAILS ---
example_emails = {
    "📌 Priority: Submission Deadline": """Urgent: Please submit your final report by 3 PM today. This is critical to meet the board deadline.""",
    "📌 Priority: Server Down Alert": """Immediate Action Required: Production server is down. Engineers are investigating the issue.""",

    "🔔 Updates: Company Policy": """Quarterly Update: New company policies and the Q2 roadmap have been published on the intranet.""",
    "🔔 Updates: Wellness Reminder": """Reminder: The HR team will host a wellness seminar this Friday. Details attached.""",

    "🛍️ Promotions: Weekend Sale": """🎉 Flash Sale! Get 40% off all electronics this weekend only. Limited stock available.""",
    "🛍️ Promotions: Rewards Program": """Introducing our new rewards program — earn points every time you shop with us!"""
}

tooltips = {
    "📌 Priority: Submission Deadline": "Emails requiring urgent or immediate action.",
    "📌 Priority: Server Down Alert": "Critical system alerts or time-sensitive tasks.",
    "🔔 Updates: Company Policy": "Routine communications, updates, or notices.",
    "🔔 Updates: Wellness Reminder": "Internal announcements and reminders.",
    "🛍️ Promotions: Weekend Sale": "Marketing emails advertising sales or discounts.",
    "🛍️ Promotions: Rewards Program": "Emails promoting loyalty programs or offers."
}

# State storage for email input
if "email_text" not in st.session_state:
    st.session_state.email_text = ""

st.markdown("### 📨 Try an Example Email")

col_example, col_random = st.columns([3, 1])
with col_example:
    selected_example = st.selectbox("Choose an example:", ["-- Select --"] + list(example_emails.keys()))
    if selected_example != "-- Select --":
        st.session_state.email_text = example_emails[selected_example]
        tooltip = tooltips.get(selected_example, "")
        st.markdown(f"""
        <div style="border: 1px solid #444; padding: 15px; border-radius: 10px; background-color: #1f1f1f;">
            <abbr title="{tooltip}" style="cursor: help;"><i>{st.session_state.email_text}</i></abbr>
        </div>
        """, unsafe_allow_html=True)

with col_random:
    if st.button("🔀 Random Example"):
        random_choice = random.choice(list(example_emails.items()))
        st.session_state.email_text = random_choice[1]
        tooltip = tooltips.get(random_choice[0], "")
        st.markdown(f"""
        <div style="border: 1px solid #444; padding: 15px; border-radius: 10px; background-color: #1f1f1f;">
            <abbr title="{tooltip}" style="cursor: help;"><i>{st.session_state.email_text}</i></abbr>
        </div>
        """, unsafe_allow_html=True)



# --- INPUT BOX ---
st.markdown("<div class='email-box'>", unsafe_allow_html=True)
email_text = st.text_area("✍️ Paste or Type Your Email Below", value=st.session_state.email_text, height=250)
st.session_state.email_text = email_text
st.markdown("</div>", unsafe_allow_html=True)

# --- Load model once (cached for performance) ---
@st.cache_resource(show_spinner="🤖 Loading LLaMA model...")
def get_model():
    return load_llama_model("model/tinyllama-1.1b-chat-v0.3.Q4_K_M.gguf")

model = get_model()

# --- CLASSIFY BUTTON ---
with st.container():
    colA, colB, colC = st.columns([1, 2, 1])
    with colB:
        st.markdown('<div class="btn-classify">', unsafe_allow_html=True)
        if st.button("🚀 Classify Email"):
            if not email_text.strip():
                st.warning("Please enter or select an email before classifying.")
            else:
                with st.spinner("🧠 Classifying..."):
                    try:
                        category = classify_email(
                            model,
                            email_text,
                            temperature=0.0,
                            max_tokens=10
                        )
                        st.success(f"📂 **Predicted Category:** `{category}`")
                    except Exception as e:
                        st.error(f"❌ Error during classification: {str(e)}")
        st.markdown("</div>", unsafe_allow_html=True)

# --- FOOTER ---
add_vertical_space(4)
st.markdown("---")
st.markdown(
    """
    <div class="footer">
        <p>Made with ❤️ by <strong>John Olalemi</strong></p>
        <p>
            🌐 <a href="https://github.com/Johnnysnipes90" target="_blank">GitHub</a>
            |
            🔗 <a href="https://www.linkedin.com/in/john-olalemi" target="_blank">LinkedIn</a>
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
