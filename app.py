"""
SafeCity AI - Main Application
AI-powered emergency response system
"""

import streamlit as st
import os
from dotenv import load_dotenv

# Import custom modules
from emotion_detector import detect_emotion
from voice_processor import capture_audio
from location_tracker import get_location, get_maps_link
from alert_system import send_alert
from config import CONFIDENCE_THRESHOLD, DISTRESS_EMOTIONS

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="SafeCity AI",
    page_icon="🚨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .big-font {
        font-size:50px !important;
        font-weight: bold;
    }
    .success-box {
        background-color: #d4edda;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #28a745;
    }
    .error-box {
        background-color: #f8d7da;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #dc3545;
    }
    .warning-box {
        background-color: #fff3cd;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #ffc107;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="big-font">🚨 SAFE CITY AI</p>', unsafe_allow_html=True)
st.markdown("### Because Safety Can't Wait")
st.markdown("---")

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Settings")
    
    guardian_number = st.text_input(
        "Guardian Phone Number",
        "+91",
        help="Include country code (e.g., +91 for India)"
    )
    
    confidence = st.slider(
        "Alert Confidence Threshold",
        0.5, 1.0, CONFIDENCE_THRESHOLD,
        step=0.05,
        help="Higher = fewer false alarms"
    )
    
    st.divider()
    st.markdown("**Project Info:**")
    st.markdown("- **Team:** BOLD")
    st.markdown("- **Hackathon:** BUILDATHON-2025")
    st.markdown("- **Theme:** AI for Social Good")
    st.markdown("- **Model:** DistilBERT (Hugging Face)")

# Main interface
col1, col2 = st.columns(2, gap="large")

# ===== TEXT INPUT SECTION =====
with col1:
    st.header("📝 Text Input")
    st.markdown("Type your message or describe what's happening:")
    
    text_input = st.text_area(
        "Enter message here...",
        placeholder="e.g., Help me someone is following me",
        height=150,
        label_visibility="collapsed"
    )
    
    if st.button("🔍 Analyze Text", key="text_btn", use_container_width=True):
        if text_input.strip():
            with st.spinner("Analyzing emotion..."):
                emotion_result = detect_emotion(text_input)
            
            st.divider()
            
            # Display emotion detection result
            st.subheader(f"Detected Emotion: {emotion_result['emotion'].upper()}")
            st.metric("Confidence", f"{emotion_result['confidence']*100:.1f}%")
            # Debug: Show all emotion scores
            if 'all_scores' in emotion_result and emotion_result['all_scores']:
                st.write("**All Detected Emotions:**")
                for score in emotion_result['all_scores']:
                    st.write(f"- {score['label']}: {score['score']*100:.1f}%")

            # Check if distress
            is_distress = (emotion_result['emotion'].lower() in DISTRESS_EMOTIONS 
                          and emotion_result['confidence'] >= confidence)
            
            if is_distress:
                st.error("🚨 DISTRESS DETECTED - ALERT TRIGGERED!")
                
                # Get location
                with st.spinner("Fetching location..."):
                    location = get_location()
                
                st.warning(f"📍 Location: {location['address']}")
                st.info(f"Coordinates: {location['lat']:.4f}, {location['lng']:.4f}")
                
                # Send alert button
                if st.button("📤 SEND ALERT TO GUARDIAN", key="alert_btn", use_container_width=True):
                    if guardian_number.startswith("+") and len(guardian_number) > 5:
                        success = send_alert(guardian_number, text_input, location)
                        if success:
                            st.balloons()
                    else:
                        st.error("❌ Please enter a valid phone number in Settings")
            else:
                st.success("✅ No distress detected. You're safe!")
        else:
            st.warning("Please enter a message to analyze")

# ===== VOICE INPUT SECTION =====
with col2:
    st.header("🎤 Voice Input")
    st.markdown("Click to record your voice:")
    
    if st.button("🎙️ START RECORDING", key="voice_btn", use_container_width=True):
        with st.spinner("Activating microphone..."):
            voice_text = capture_audio()
        
        if voice_text:
            st.success(f"✅ You said: *{voice_text}*")
            
            st.divider()
            
            with st.spinner("Analyzing emotion..."):
                emotion_result = detect_emotion(voice_text)
            
            st.subheader(f"Detected Emotion: {emotion_result['emotion'].upper()}")
            st.metric("Confidence", f"{emotion_result['confidence']*100:.1f}%")
            
            # Check if distress
            is_distress = (emotion_result['emotion'].lower() in DISTRESS_EMOTIONS 
                          and emotion_result['confidence'] >= confidence)
            
            if is_distress:
                st.error("🚨 DISTRESS DETECTED - ALERT TRIGGERED!")
                
                # Get location
                with st.spinner("Fetching location..."):
                    location = get_location()
                
                st.warning(f"📍 Location: {location['address']}")
                st.info(f"Coordinates: {location['lat']:.4f}, {location['lng']:.4f}")
                
                # Send alert button
                if st.button("📤 SEND ALERT TO GUARDIAN", key="voice_alert_btn", use_container_width=True):
                    if guardian_number.startswith("+") and len(guardian_number) > 5:
                        success = send_alert(guardian_number, voice_text, location)
                        if success:
                            st.balloons()
                    else:
                        st.error("❌ Please enter a valid phone number in Settings")
            else:
                st.success("✅ No distress detected. You're safe!")

# Footer
st.markdown("---")
st.markdown("""
    <div style="text-align: center; color: gray;">
    <p>SafeCity AI - An AI-powered emergency response system</p>
    <p>Team BOLD | Sai Vidya Institute of Technology | BUILDATHON-2025</p>
    <p><strong>Made with ❤️ for a Safer India</strong></p>
    </div>
""", unsafe_allow_html=True)
