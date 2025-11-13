"""
Alert System Module for SafeCity AI
Sends SMS alerts via Twilio API
"""

import os
from datetime import datetime
from twilio.rest import Client
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def send_alert(guardian_number, message_text, location):
    """
    Send SOS alert via SMS
    
    Args:
        guardian_number (str): Guardian phone number
        message_text (str): Original distress message
        location (dict): Location information
        
    Returns:
        bool: True if alert sent successfully
    """
    try:
        # Get Twilio credentials
        account_sid = os.getenv('TWILIO_ACCOUNT_SID')
        auth_token = os.getenv('TWILIO_AUTH_TOKEN')
        from_number = os.getenv('TWILIO_PHONE_NUMBER')
        
        if not all([account_sid, auth_token, from_number]):
            st.error("❌ Twilio credentials not configured in .env file")
            return False
        
        # Create Twilio client
        client = Client(account_sid, auth_token)
        
        # Compose alert message
        maps_link = f"https://maps.google.com/?q={location['lat']},{location['lng']}"
        
        alert_message = f"""🚨 SAFECITY AI ALERT 🚨

DISTRESS DETECTED!

⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

💬 Message: "{message_text}"

📍 LOCATION:
{location['address']}
City: {location['city']}, {location['region']}, {location['country']}
Coordinates: {location['lat']:.4f}, {location['lng']:.4f}

🗺️ Maps Link: {maps_link}

⚠️ Please check on them immediately!
—
SafeCity AI: Because Safety Can't Wait"""
        
        # Send SMS
        message = client.messages.create(
            body=alert_message,
            from_=from_number,
            to=guardian_number
        )
        
        st.success(f"✅ Alert sent! ID: {message.sid}")
        return True
        
    except Exception as e:
        st.error(f"❌ Error: {e}")
        return False
from voice_recognizer import recognize_speech_from_mic

# Example integration inside alert creation route or command

# Use get_alert_message() instead of fixed text input for alert message



