import os
from dotenv import load_dotenv

# Load environment variables from the root .env file
load_dotenv()

# --- Reddit Config ---
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = os.getenv("REDDIT_USER_AGENT")

# --- AI Config ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# --- Email Config ---
SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")
SENDER_EMAIL = os.getenv("SENDER_EMAIL")

# --- App Settings ---
# Fetch the comma-separated strings from .env
_subreddits_str = os.getenv("SUBREDDITS")
_recipients_str = os.getenv("RECIPIENT_EMAILS")

# Process the strings into clean Python lists.
# This handles cases where the env var might be missing and removes whitespace.
SUBREDDITS = [name.strip() for name in _subreddits_str.split(',')] if _subreddits_str else []
RECIPIENT_EMAILS = [email.strip() for email in _recipients_str.split(',')] if _recipients_str else []