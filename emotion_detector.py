from transformers import pipeline

emotion_classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def detect_emotion(text):
    """Detect emotion from text."""
    emotions = ["fear", "anger", "sadness", "joy", "neutral"]
    try:
        result = emotion_classifier(text, emotions)
        emotion = result["labels"][0]
        confidence = result["scores"][0]
        return {
            "emotion": emotion,
            "confidence": confidence,
            "all_scores": dict(zip(result["labels"], result["scores"]))
        }
    except Exception as e:
        print(f"Error detecting emotion: {e}")
        return {
            "emotion": "neutral",
            "confidence": 0.5,
            "all_scores": {}
        }

