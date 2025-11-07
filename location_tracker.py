"""
Location Tracking Module for SafeCity AI
Uses IP-based geolocation via geocoder
"""

import geocoder
import streamlit as st

def get_location():
    """
    Get current location based on IP address
    
    Returns:
        dict: Location information
    """
    try:
        st.info("📍 Fetching your location...")
        g = geocoder.ip('me')
        
        if g.ok:
            location_data = {
                "city": g.city or "Unknown",
                "region": g.state or "Unknown",
                "country": g.country or "Unknown",
                "lat": g.lat,
                "lng": g.lng,
                "address": g.address or "Unknown location"
            }
            return location_data
        else:
            return get_default_location()
            
    except Exception as e:
        st.warning(f"Could not fetch location: {e}")
        return get_default_location()

def get_default_location():
    """Return default location if tracking fails"""
    return {
        "city": "Unknown",
        "region": "Unknown",
        "country": "India",
        "lat": 0.0,
        "lng": 0.0,
        "address": "Location unavailable"
    }

def get_maps_link(lat, lng):
    """Generate Google Maps link"""
    return f"https://maps.google.com/?q={lat},{lng}"
