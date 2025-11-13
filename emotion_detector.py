def detect_emotion(text):
    """Simple keyword-based emotion detection."""
    text_lower = text.lower()
    
    emotions_keywords = {
        "fear": ["help", "danger", "scared", "afraid", "emergency", "911", "rescue"],
        "anger": ["angry", "mad", "furious", "hate", "attack", "rage"],
        "sadness": ["sad", "crying", "depressed", "hurt", "pain", "sad"],
        "joy": ["happy", "great", "love", "wonderful", "excellent"],
    }
    
    emotion_scores = {}
    for emotion, keywords in emotions_keywords.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        emotion_scores[emotion] = score / len(keywords)
    
    emotion = max(emotion_scores, key=emotion_scores.get)
    confidence = min(emotion_scores[emotion], 1.0)
    
    if confidence == 0:
        emotion = "neutral"
        confidence = 0.5
    
    return {
        "emotion": emotion,
        "confidence": confidence,
        "all_scores": emotion_scores
    }


