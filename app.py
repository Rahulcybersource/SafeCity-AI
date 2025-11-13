import streamlit as st
from alert_system import process_alert
from voice_processor import capture_audio
from emotion_detector import detect_emotion
from location_tracker import get_location
from datetime import datetime

st.set_page_config(page_title="SafeCity AI", page_icon="🚨", layout="wide")

st.title("🚨 SafeCity AI - Emergency Alert System")
st.subheader("Prototype 1.0")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    user_id = st.text_input("User ID", value="default_user")
    guardian_phone = st.text_input("Guardian Phone", value="+0000000000")

# Main interface
col1, col2 = st.columns(2)

with col1:
    st.header("🎤 Voice Input")
    if st.button("🔴 Record Emergency Alert"):
        st.info("Recording... Please speak now!")
        message = capture_audio()
        if message:
            st.success(f"✅ Recognized: {message}")
            st.session_state.message = message
        else:
            st.error("❌ Failed to recognize speech")

with col2:
    st.header("📊 Alert Summary")
    if "message" in st.session_state:
        emotion_data = detect_emotion(st.session_state.message)
        location = get_location()
        
        st.write(f"**Message:** {st.session_state.message}")
        st.write(f"**Emotion:** {emotion_data['emotion'].upper()} (Confidence: {emotion_data['confidence']:.2f})")
        st.write(f"**Location:** {location['address']}")
        st.write(f"**Safety Score:** {location['safety_score']}/100")

# Alert submission
st.divider()
if st.button("✅ Submit Alert"):
    if "message" in st.session_state:
        with st.spinner("Processing alert..."):
            alert, success = process_alert(user_id)
        if success:
            st.success("✅ Alert sent successfully!")
            st.json(alert)
        else:
            st.error("❌ Failed to send alert")
    else:
        st.warning("⚠️ Please record a message first")

# Alert history
st.divider()
st.header("📜 Recent Alerts")
st.info("Alert history would be displayed here (database integration needed)")
