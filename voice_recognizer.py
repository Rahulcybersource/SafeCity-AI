import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something...")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"Recognized: {text}")
        return text
    except Exception as e:
        print(f"Recognition error: {e}")
        return ""
