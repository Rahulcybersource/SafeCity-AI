

# LOWER threshold for testing (you can increase later)
CONFIDENCE_THRESHOLD = 0.60  # Changed from 0.90 to 0.60

# Distress emotions that trigger alerts
DISTRESS_EMOTIONS = ['fear', 'anger', 'sadness', 'anxiety', 'panic']

# Better emotion model
EMOTION_MODEL = "bhadresh-savani/distilbert-base-uncased-emotion"

# Voice recording parameters - INCREASED
VOICE_TIMEOUT = 10  # seconds
VOICE_PHRASE_LIMIT = 15  # seconds
