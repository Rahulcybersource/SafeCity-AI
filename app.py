import streamlit as st
from alert_system import create_alert, send_alert
from voice_processor import capture_audio
from emotion_detector import detect_emotion
from location_tracker import get_location
from datetime import datetime
import json

st.set_page_config(page_title="SafeCity AI", page_icon="🚨", layout="wide")

st.title("🚨 SafeCity AI - Emergency Alert System")
st.subheader("Prototype 1.0 - Voice Emergency Alerts")

# Initialize session state
if "alerts" not in st.session_state:
    st.session_state.alerts = []
if "current_message" not in st.session_state:
    st.session_state.current_message = ""

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    user_id = st.text_input("User ID", value="user_001")
    guardian_phone = st.text_input("Guardian Phone", value="+919876543210")
    st.write("---")
    st.info("✅ Settings configured")

# Main content
col1, col2 = st.columns(2)

with col1:
    st.header("🎤 Alert Input")
    
    # Option 1: Voice Input (Local only)
    if st.button("🔴 Record Emergency Alert", key="record_btn"):
        st.info("🎤 Recording... Speak now!")
        message = capture_audio()
        if message:
            st.session_state.current_message = message
            st.success(f"✅ Recognized: {message}")
        else:
            st.warning("⚠️ Could not capture audio (Streamlit Cloud limitation)")
    
    # Option 2: Manual text input
    st.write("**Or type message manually:**")
    manual_message = st.text_area("Emergency Message", placeholder="Describe your emergency...")
    
    if manual_message:
        st.session_state.current_message = manual_message

with col2:
    st.header("📊 Alert Details")
    
    if st.session_state.current_message:
        emotion_data = detect_emotion(st.session_state.current_message)
        location = get_location()
        
        st.metric("Emotion Detected", emotion_data["emotion"].upper(), f"Confidence: {emotion_data['confidence']:.0%}")
        st.metric("Location", location["address"])
        st.metric("Safety Score", f"{location['safety_score']}/100")
        
        st.write("**Message:** " + st.session_state.current_message)
    else:
        st.info("👆 Record or type an emergency message")

# Submit alert
st.divider()
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("✅ Submit Emergency Alert", key="submit_btn"):
        if st.session_state.current_message:
            with st.spinner("Processing alert..."):
                alert = create_alert(st.session_state.current_message, user_id)
                success = send_alert(alert)
            
            if success:
                st.session_state.alerts.append(alert)
                st.success("✅ Alert submitted successfully!")
                st.balloons()
                
                # Display alert details
                st.json(alert)
                
                # Clear message
                st.session_state.current_message = ""
        else:
            st.error("❌ Please record or type a message first")

with col_btn2:
    if st.button("🗑️ Clear Message"):
        st.session_state.current_message = ""
        st.rerun()

# Alert History
st.divider()
st.header("📜 Alert History")

if st.session_state.alerts:
    for i, alert in enumerate(reversed(st.session_state.alerts), 1):
        with st.expander(f"Alert #{i} - {alert['timestamp'][:10]}"):
            col_a, col_b = st.columns(2)
            with col_a:
                st.write(f"**Message:** {alert['message']}")
                st.write(f"**Emotion:** {alert['emotion'].upper()}")
            with col_b:
                st.write(f"**Location:** {alert['location']['address']}")
                st.write(f"**Phone:** {alert['guardian_phone']}")
else:
    st.info("📭 No alerts submitted yet")

# Footer
st.divider()
st.caption("SafeCity AI - Prototype 1.0 | Emergency Alert System")

