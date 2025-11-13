import json
from datetime import datetime
from voice_processor import process_voice_input
from emotion_detector import detect_emotion
from location_tracker import get_location
from config import GUARDIAN_PHONE

def create_alert(user_id="default_user"):
    """Create emergency alert from voice input."""
    # Get voice message
    message = process_voice_input()
    
    # Detect emotion
    emotion_data = detect_emotion(message)
    
    # Get location
    location = get_location()
    
    # Create alert object
    alert = {
        "user_id": user_id,
        "message": message,
        "emotion": emotion_data["emotion"],
        "confidence": emotion_data["confidence"],
        "location": location,
        "timestamp": datetime.utcnow().isoformat(),
        "guardian_phone": GUARDIAN_PHONE,
        "status": "created"
    }
    
    return alert

def send_alert(alert):
    """Send alert to guardians (mock implementation)."""
    print(f"📤 Sending alert to {alert['guardian_phone']}")
    print(f"Alert details: {json.dumps(alert, indent=2)}")
    # In production, integrate with SMS/notification service
    return True

def process_alert(user_id="default_user"):
    """Process complete alert workflow."""
    alert = create_alert(user_id)
    success = send_alert(alert)
    return alert, success


