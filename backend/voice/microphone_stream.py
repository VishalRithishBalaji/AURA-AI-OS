import speech_recognition as sr


recognizer = sr.Recognizer()


def listen_microphone():

    with sr.Microphone() as source:

        print("\n🎤 Listening...")

        recognizer.adjust_for_ambient_noise(
            source,
            duration=1
        )

        audio = recognizer.listen(source)

        return audio