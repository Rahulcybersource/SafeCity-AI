"""
Voice Processing Module for SafeCity AI - IMPROVED VERSION
Converts speech to text using SpeechRecognition
"""

import speech_recognition as sr
import streamlit as st

def capture_audio():
    """
    Capture audio from microphone and convert to text
    
    Returns:
        str: Transcribed text or None if failed
    """
    recognizer = sr.Recognizer()
    
    # Adjust sensitivity
    recognizer.energy_threshold = 300  # Lower = more sensitive
    recognizer.dynamic_energy_threshold = True
    
    try:
        with sr.Microphone() as source:
            st.info("🎤 Calibrating microphone...")
            
            # Longer ambient noise adjustment for better accuracy
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            
            st.success("✅ Microphone ready! Speak now...")
            
            # Listen for audio - LONGER TIMEOUTS
            audio = recognizer.listen(
                source,
                timeout=10,  # Wait up to 10 seconds for speech to start
                phrase_time_limit=15  # Allow up to 15 seconds of speech
            )
            
            st.info("🔄 Processing your speech...")
            
            # Convert speech to text using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            
            return text
            
    except sr.WaitTimeoutError:
        st.error("⏱️ No speech detected within 10 seconds. Please try again and speak louder.")
        return None
    except sr.UnknownValueError:
        st.error("❌ Could not understand audio. Please speak more clearly or check your microphone.")
        return None
    except sr.RequestError as e:
        st.error(f"🌐 Speech recognition service error: {e}. Check your internet connection.")
        return None
    except Exception as e:
        st.error(f"🎤 Microphone error: {e}. Make sure your microphone is connected and permissions are granted.")
        return None
