
import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
GUARDIAN_PHONE = os.getenv("GUARDIAN_PHONE", "+919876543210")
USER_ID = os.getenv("USER_ID", "user_001")

# Location settings
DEFAULT_LATITUDE = 12.9716
DEFAULT_LONGITUDE = 77.5946
DEFAULT_ADDRESS = "Bangalore, India"

# Alert settings
MAX_RECORDING_TIME = 15
