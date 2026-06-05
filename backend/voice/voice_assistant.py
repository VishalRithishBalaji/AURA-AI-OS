from voice.microphone_stream import listen_microphone
from voice.whisper_input import speech_to_text
from voice.speech_output import speak
from voice.wake_word import detect_wake_word

from agents.orchestrator import route_task


async def start_voice_assistant():

    speak("AURA Voice System Activated")

    while True:

        try:

            # LISTEN
            audio = listen_microphone()

            text = speech_to_text(audio)

            if not text:
                continue

            print(f"\nYou Said: {text}")

            # CHECK WAKE WORD
            if detect_wake_word(text):

                speak("Processing your request")

                # REMOVE WAKE WORD
                cleaned_text = text.lower()

                wake_words = [
                    "hey aura",
                    "a u r a",
                    "hello aura"
                ]

                for word in wake_words:
                    cleaned_text = cleaned_text.replace(word, "")

                cleaned_text = cleaned_text.strip()

                # EXECUTE TASK
                response = await route_task(
                    cleaned_text
                )

                response_text = str(response)

                print(
                    f"\nAURA RESPONSE:\n{response_text}"
                )

                speak(response_text)

        except Exception as e:

            print(f"\nVoice Error: {e}")