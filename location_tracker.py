
from config import DEFAULT_LATITUDE, DEFAULT_LONGITUDE, DEFAULT_ADDRESS

def get_location():
    """Get mock location (no external API calls)."""
    return {
        "latitude": DEFAULT_LATITUDE,
        "longitude": DEFAULT_LONGITUDE,
        "address": DEFAULT_ADDRESS,
        "safety_score": 75
    }

