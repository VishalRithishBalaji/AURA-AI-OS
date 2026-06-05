WAKE_WORDS = [
    "hey aura",
    "a u r a",
    "hello aura"
]


def detect_wake_word(text: str):

    text = text.lower()

    for word in WAKE_WORDS:

        if word in text:

            return True

    return False