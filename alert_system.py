from datetime import datetime
from emotion_detector import detect_emotion
from location_tracker import get_location
from config import GUARDIAN_PHONE, USER_ID

def create_alert(message, user_id=USER_ID):
    """Create emergency alert from message."""
    emotion_data = detect_emotion(message)
    location = get_location()
    
    alert = {
        "user_id": user_id,
        "message": message,
        "emotion": emotion_data["emotion"],
        "confidence": round(emotion_data["confidence"], 2),
        "location": location,
        "timestamp": datetime.utcnow().isoformat(),
        "guardian_phone": GUARDIAN_PHONE,
        "status": "sent"
    }
    return alert

def send_alert(alert):
    """Mock send alert to guardians."""
    print(f"✅ Alert sent to {alert['guardian_phone']}")
    return True

    



