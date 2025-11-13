
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
GUARDIAN_PHONE = os.getenv("GUARDIAN_PHONE", "+0000000000")

# Location settings
DEFAULT_LATITUDE = 0.0
DEFAULT_LONGITUDE = 0.0
DEFAULT_ADDRESS = "Unknown Location"

# Emotion thresholds
FEAR_THRESHOLD = 0.6
ANGER_THRESHOLD = 0.5
SADNESS_THRESHOLD = 0.5

# Alert settings
ALERT_TIMEOUT = 10  # seconds
MAX_RECORDING_TIME = 30  # seconds


