import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening... Please speak now!")
        try:
            audio = recognizer.listen(source, timeout=10)
            text = recognizer.recognize_google(audio)
            print(f"✅ Recognized: {text}")
            return text
        except Exception as e:
            print(f"❌ Error: {e}")
            return ""

if __name__ == "__main__":
    message = recognize_speech()
    if message:
        print(f"\n📢 Alert Message: {message}")
