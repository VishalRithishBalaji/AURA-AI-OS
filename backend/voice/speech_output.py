import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)


voices = engine.getProperty("voices")

if len(voices) > 1:
    engine.setProperty(
        "voice",
        voices[1].id
    )


def speak(text: str):

    print(f"\n🤖 AURA: {text}")

    engine.say(text)

    engine.runAndWait()