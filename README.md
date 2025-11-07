# SafeCity AI - Because Safety Can't Wait

## 🎯 Overview

SafeCity AI is an **AI-powered emergency response system** that automatically detects distress through voice and text, fetches user location, and sends instant SOS alerts to guardians.

### Problem
- Every 8 minutes, an assault is reported in India
- Existing SOS apps require **manual activation** - but in panic, people can't reach phones
- We need technology that senses distress **automatically**

### Solution
SafeCity AI uses **Artificial Intelligence** to detect fear/panic/distress and automatically alerts help.

---

## 🚀 Live Demo

**Try SafeCity AI Online:**  
https://safecity-ai-yourname.streamlit.app

---

## ✨ Features

✅ **Text Input** - Type distress messages  
✅ **Voice Input** - Hands-free operation (just speak)  
✅ **AI Emotion Detection** - Detects fear, anger, sadness, anxiety, panic  
✅ **Automatic Location** - IP-based location tracking  
✅ **SMS Alerts** - Sends instant SMS to guardians  
✅ **Google Maps Link** - Location shared via maps  
✅ **90% Confidence Threshold** - Minimizes false alarms  
✅ **Privacy-First** - No data storage, real-time processing only  

---

## 🛠️ Technology Stack

- **Frontend:** Streamlit
- **AI Model:** DistilBERT (Hugging Face)
- **Speech Recognition:** SpeechRecognition + PyAudio
- **Location:** Geocoder (IP-based)
- **Alerts:** Twilio SMS API
- **Language:** Python

---

## 📋 How It Works

1. **User Input** → Text or Voice
2. **Emotion Detection** → AI analyzes message/speech
3. **Distress Check** → Is emotion = fear/anger/sadness/anxiety/panic?
4. **Location Fetch** → Get user's location via IP
5. **Send Alert** → SMS to guardian with location + maps link

---

## 💻 Installation (Local Setup)

### Prerequisites
- Python 3.8+
- Pip
- Microphone (for voice input)
- Twilio account (for SMS alerts)

### Quick Start

