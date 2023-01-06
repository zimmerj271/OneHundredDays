from morse import MorseSound, TextToMorse


def get_code():
    user_input = input('What would you like to convert to Morse code? ')
    morse_code = TextToMorse(user_input)
    return morse_code.morse_text


def code_to_sound(code_text: str):
    morse_sound = MorseSound()
    morse_sound.play_sound(code_text)


if __name__ == "__main__":
    code = get_code()
    print(code)
    code_to_sound(code)
