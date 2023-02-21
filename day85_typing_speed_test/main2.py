from english_words import get_english_words_set
from random import choices
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, font
from itertools import cycle



class TypeTestGUI(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title("Keyboard Typing Test")
        self.resizable(width=False, height=False)
        self.set_theme('black')
        self.background_frame = ttk.Frame(self)
        self.background_frame.pack(expand=True, fill='both')
        self.background_color = '#2b2b2b'  # color for display background
        self.style = ttk.Style()
        self.style.configure('Display.TFrame', background=self.background_color)
        self.style.configure('Correct.TLabel', foreground="green")
        self.style.configure('Wrong.TLabel', foreground="red")
        self.text_display = Display()
        self.create_entry()
        self.create_menu()
        self.type_test = TypeTest()

    def create_entry(self):
        self.entry_frame = ttk.Frame(self.background_frame, relief='ridge', style='Display.TFrame')
        self.entry_frame.pack(pady=(20, 40), fill='y', expand=False)
        self.style.configure('EntryStyle.TEntry', fieldbackground=self.background_color, foreground='white')
        self.entry = ttk.Entry(self.entry_frame, font=('Arial', 28, 'bold'), style='EntryStyle.TEntry')
        self.entry.pack(fill='both', expand=True)
        self.entry.focus_set()
        self.entry.bind_all('<Key>', self.verify_entry)  # bind all key presses to the verify_entry method

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Start", command=self.start)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def start(self):
        words = " ".join(self.type_test.word_list)
        self.text_display.config(state="normal")
        self.text_display.delete('1.0', 'end')  # delete all words in Text widget
        self.text_display.insert(tk.INSERT, words)
        self.text_display.config(state="disabled")


    def verify_entry(self, event):
        print(event.keysym)


class Display(TypeTestGUI):
    def __init__(self, width=1200, height=400):
        super().__init__()
        self.display_frame = ttk.Frame(self.background_frame, width=width, height=height,
                                       relief='ridge', style='Display.TFrame')
        self.display_frame.pack(pady=(40, 20), padx=40, fill='both', expand=False)
        self.display_frame.pack_propagate(False)  # Stop the frame from propagating the widget to be "shrink or fit"
        self.text_display = tk.Text(self.display_frame, wrap="word",
                                    background=self.background_color, foreground="white",
                                    font=('Arial', 28, 'bold'), padx=10, width=56, relief="flat")
        self.text_display.insert(tk.INSERT, "Ready?")
        self.text_display.place(relx=0, rely=0)
        self.text_display.config(state="disabled")  # make Text widget so that it cannot be accessed by the user

    def update_all_text(self, text):
        self.text_display.config(state='normal')
        self.text_display.delete('1.0', 'end')  # delete all words in Text widget
        self.text_display.insert(tk.INSERT, text)
        self.text_display.config(state="disabled")

class TypeTest:
    def __init__(self):
        self.word_dictionary = get_english_words_set(['web2'])
        self.word_list = choices(list(self.word_dictionary), k=20)
        self.word_iterator = cycle(self.word_list)
        self.current_word = next(self.word_iterator)
        self.letter_iterator = cycle(self.current_word)
        self.current_letter = next(self.letter_iterator)
        self.entered_word = ''

    def check_letter(self, letter):
        if letter == self.current_letter:
            self.entered_word = self.entered_word + letter
            next(self.letter_iterator)
            return True
        return False




def main():
    window = TypeTestGUI()
    window.mainloop()


if __name__ == '__main__':
    main()
