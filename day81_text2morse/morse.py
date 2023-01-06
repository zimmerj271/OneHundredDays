import numpy as np
import sounddevice as sd

CHAR_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
                'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '..-', 'W': '.--', 'X': '-..-',
                'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
                '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'}


class MorseSound:
    def __init__(self, frequency: int=440, sample_rate: int=44100, unit_time: float=0.25):
        self.frequency = frequency
        self.fs = sample_rate
        self.unit_time = unit_time  # shortest unit of time in milliseconds

    def rest_time(self, extend: int=1) -> np.ndarray:
        sample_number = int(self.unit_time * self.fs * extend)
        no_sound_array = np.zeros((sample_number,), dtype=float)
        return no_sound_array

    def tone(self) -> np.ndarray:
        sample_number = int(self.unit_time * self.fs)
        time = np.linspace(start=0, stop=self.unit_time, num=sample_number, endpoint=False)
        tone_array = np.sin(2 * np.pi * self.frequency * time)
        return tone_array

    def dot(self) -> np.ndarray:
        dot_array = np.concatenate((self.tone(), self.rest_time()))  # add rest time after tone
        return dot_array

    def dash(self) -> np.ndarray:
        dash_array = np.concatenate((self.tone(), self.tone(), self.tone(), self.rest_time()))  # dash is 3x as long
        return dash_array

    def text_to_array(self, char: 'str') -> np.ndarray:
        if char == '.':
            return self.dot()
        if char == '-':
            return self.dash()

    def play_sound(self, morse_text: str):
        text_list = morse_text.split()
        sound_list = []
        for char in text_list:
            for tone in char:
                sound_list.append(self.text_to_array(tone))
            sound_list.append(self.rest_time(2))  # tones already have 1 base rest time, 3x total between chars

        sound_array = np.concatenate(sound_list)
        sd.play(sound_array, self.fs, blocking=True)
        return


class TextToMorse:
    def __init__(self, text):
        self.alphanumeric_text = text
        self.code_list = self.text_to_code()
        self.morse_text = self.get_string(self.code_list)

    def text_to_code(self) -> list:
        text_string = self.alphanumeric_text.upper()
        text_list = text_string.split()
        code_list = []
        for word in text_list:
            temp = [CHAR_TO_MORSE[x] for x in word]
            code_list.append(temp)
        return code_list

    def get_string(self, code_list: list) -> str:
        morse_text = ''
        for lst in code_list:
            word = ' '.join(lst)
            morse_text += word + '   '
        return morse_text
