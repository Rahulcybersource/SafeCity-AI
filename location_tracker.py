from geopy.geocoders import Nominatim
from config import DEFAULT_LATITUDE, DEFAULT_LONGITUDE, DEFAULT_ADDRESS

def get_location():
    """Get current location (mock implementation)."""
    try:
        # In production, use actual GPS/location API
        location = {
            "latitude": DEFAULT_LATITUDE,
            "longitude": DEFAULT_LONGITUDE,
            "address": DEFAULT_ADDRESS,
            "safety_score": calculate_safety_score(DEFAULT_LATITUDE, DEFAULT_LONGITUDE)
        }
        return location
    except Exception as e:
        print(f"Error getting location: {e}")
        return {
            "latitude": DEFAULT_LATITUDE,
            "longitude": DEFAULT_LONGITUDE,
            "address": DEFAULT_ADDRESS,
            "safety_score": 0
        }

def calculate_safety_score(latitude, longitude):
    """Calculate area safety score (mock implementation)."""
    # In production, use actual crime data API
    return 50  # Default score 0-100

def get_address_from_coords(latitude, longitude):
    """Get address from coordinates."""
    try:
        geolocator = Nominatim(user_agent="safecity_ai")
        location = geolocator.reverse(f"{latitude}, {longitude}")
        return location.address
    except Exception as e:
        print(f"Error getting address: {e}")
        return DEFAULT_ADDRESS

