# Configuration settings for Popeye AI Assistant
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Voice command settings
VOICE_COMMAND_LANGUAGE = "en-US"

# Automation settings
AUTOMATION_CONFIG = {
    # Add specific tool configurations here
}

# Dark web monitoring settings
DARK_WEB_MONITOR_CONFIG = {
    "tor_proxy": "socks5h://127.0.0.1:9050"
}

# Freelancing settings
FREELANCING_CONFIG = {
    "platforms": ["upwork", "fiverr", "freelancer"]
}

# Content creation settings
CONTENT_CREATION_CONFIG = {
    "output_directory": "content"
}

# Self-learning settings
SELF_LEARNING_CONFIG = {
    "certifications": ["OSCP", "eJPT"]
}

# OSINT settings
OSINT_CONFIG = {
    "shodan_api_key": os.getenv("SHODAN_API_KEY"),
    "virustotal_api_key": os.getenv("VIRUSTOTAL_API_KEY"),
    "hibp_api_key": os.getenv("HIBP_API_KEY")
}

# Twilio settings
TWILIO_CONFIG = {
    "account_sid": os.getenv("TWILIO_ACCOUNT_SID"),
    "auth_token": os.getenv("TWILIO_AUTH_TOKEN"),
    "phone_number": os.getenv("TWILIO_PHONE_NUMBER")
}

# Telegram settings
TELEGRAM_CONFIG = {
    "bot_token": os.getenv("TELEGRAM_BOT_TOKEN"),
    "chat_id": os.getenv("TELEGRAM_CHAT_ID")
}