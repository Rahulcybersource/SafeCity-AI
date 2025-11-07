"""
Emotion Detection Module for SafeCity AI
Uses DistilBERT model from Hugging Face - IMPROVED VERSION
"""

import streamlit as st
from transformers import pipeline

# Use a more sensitive emotion model
EMOTION_MODEL = "bhadresh-savani/distilbert-base-uncased-emotion"

@st.cache_resource
def load_emotion_model():
    """Load and cache the emotion detection model"""
    return pipeline(
        "text-classification",
        model=EMOTION_MODEL,
        return_all_scores=True  # Changed to True to see all emotion scores
    )

def detect_emotion(text):
    """
    Detect emotion from text input
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: {emotion: str, confidence: float, all_scores: list}
    """
    if not text or text.strip() == "":
        return {"emotion": "unknown", "confidence": 0.0, "all_scores": []}
    
    try:
        classifier = load_emotion_model()
        results = classifier(text)[0]
        
        # Find the emotion with highest score
        top_emotion = max(results, key=lambda x: x['score'])
        
        return {
            "emotion": top_emotion['label'].lower(),
            "confidence": round(top_emotion['score'], 4),
            "all_scores": results  # Show all emotions detected
        }
    except Exception as e:
        st.error(f"Error detecting emotion: {e}")
        return {"emotion": "error", "confidence": 0.0, "all_scores": []}
