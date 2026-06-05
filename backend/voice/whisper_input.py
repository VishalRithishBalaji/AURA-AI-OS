import speech_recognition as sr


recognizer = sr.Recognizer()


def speech_to_text(audio):

    try:

        text = recognizer.recognize_google(audio)

        print(f"\n🗣 You Said: {text}")

        return text

    except Exception as e:

        print(f"\nSpeech Error: {e}")

        return ""