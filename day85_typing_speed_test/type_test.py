from english_words import get_english_words_set
from random import choices
from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk
from itertools import cycle
import time


class TypeTestGUI(ThemedTk):
    def __init__(self, test):
        super().__init__()
        self.title("Keyboard Typing Test")
        self.resizable(width=False, height=False)
        self.set_theme('black')
        self.background_frame = ttk.Frame(self)
        self.background_frame.pack(expand=True, fill='both')
        self.background_color = '#2b2b2b'  # color for display background
        self.style = ttk.Style()
        self.style.configure('Display.TFrame', background=self.background_color)
        self.display_frame = DisplayFrame(self.background_frame, self.background_color,
                                          width=1200, height=400, relief='ridge', style='Display.TFrame')
        self.pack_display()
        self.entry_frame = EntryFrame(self.background_frame, self.background_color,
                                      relief='ridge', style='Display.TFrame')
        self.pack_entry()
        self.type_test = test
        self.difficulty = tk.StringVar()
        self.create_menu()

    def pack_display(self):
        self.display_frame.pack(pady=(40, 20), padx=40, fill='both', expand=False)
        self.display_frame.pack_propagate(False)  # Stop the frame from propagating the widget to be "shrink or fit"

    def pack_entry(self):
        self.entry_frame.pack(pady=(20, 40), fill='y', expand=False)

    def create_menu(self):
        self.difficulty.set('one')  # set default difficulty to easy
        menu_bar = tk.Menu(self)
        submenu = tk.Menu(self, tearoff=False)
        submenu.add_radiobutton(label="Easy", value='one', variable=self.difficulty,
                                command=self.easy_difficulty)
        submenu.add_radiobutton(label="Hard", value='two', variable=self.difficulty,
                                command=self.hard_difficulty)
        self.config(menu=menu_bar)  # assign menu_bar to window
        file_menu = tk.Menu(menu_bar, tearoff=False)  # assign file_menu to menu_bar
        file_menu.add_command(label="Start", command=self.start)
        file_menu.add_cascade(label="Difficulty", menu=submenu, underline=False)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def start(self):
        self.type_test.start_test()
        words = " ".join(self.type_test.word_list)
        self.display_frame.update_all_text(words)
        self.display_frame.highlight_current_word(self.type_test.current_word)
        self.entry_frame.focus_entry()
        self.entry_frame.entry.bind_all('<Key>', self.check_input)  # bind all key presses to the verify_entry method

    def check_input(self, event):
        typed_char = event.keysym  # get key from event
        entered_word = self.entry_frame.entry.get()
        if typed_char == "BackSpace":
            self.display_frame.remove_color(entered_word, self.type_test.current_word)
        else:
            self.display_frame.add_color(entered_word, self.type_test.current_word)
            if self.type_test.check_word(entered_word):
                self.type_test.next_word()
                self.entry_frame.clear_entry()
                self.display_frame.highlight_current_word(self.type_test.current_word)
        self.type_test.end_test()

    def easy_difficulty(self):
        self.type_test.easy_difficulty = True

    def hard_difficulty(self):
        self.type_test.easy_difficulty = False


# One way to properly handle separate widgets as children of other widgets is to create child classes of Frame
# and 'stack the frames' on top of each other.  Be sure to correctly reference the parent widget and pass
# all *args and **kwargs to the Frame class.
class DisplayFrame(ttk.Frame):
    def __init__(self, parent, background_color, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.text = tk.Text(self, wrap="word", background=background_color,
                            foreground="white", font=('Arial', 28, 'bold'),
                            padx=10, width=56, relief="flat")
        self.text.insert(tk.INSERT, "Ready?")
        self.text.place(relx=0, rely=0)
        self.text.config(state="disabled")  # make Text widget so that it cannot be accessed by the user
        self.current_position = "1.0"  # starting position in Text widget
        self.word_position = [self.current_position]
        self.word_end_position = []
        self.word_index_range = None
        self.text.tag_config('current', background="#5b5b5b")
        self.text.tag_config('typed_char', foreground="green")
        self.text.tag_config('backspace', foreground="white")

    def update_all_text(self, text):
        self.text.config(state='normal')
        self.text.delete('1.0', 'end')  # delete all words in Text widget
        self.text.insert(tk.INSERT, text)
        self.text.config(state="disabled")

    def highlight_current_word(self, word):
        # StringVar will be used to store the count of the number of positions found by search
        # see: https://www.tcl.tk/man/tcl8.5/TkCmd/text.html#M127
        # see: https://www.pythontutorial.net/tkinter/tkinter-stringvar/
        count_var = tk.StringVar()
        index = self.text.search(f"{word}", "1.0", "end", count=count_var)
        self.current_position = index
        self.word_position.append(index)
        word_index = index.split(".", 1)
        word_length = int(word_index[1]) + len(word) - 1
        end_position = word_index[0] + "." + str(word_length)
        self.word_end_position.append(end_position)

        # Use tag_add to tell Text where to apply the tag config.  In this case starting from index
        # and ending at the end of the string found from search which is conveyed using count_var.get
        # Note that "%s + %sc" % () is a function call in tcl:
        # https://stackoverflow.com/questions/56114893/tkinter-text-widget-search-method
        self.text.tag_add('current', index, "%s + %sc" % (index, count_var.get()))

    def add_color(self, typed_word, word):
        matching_chars = [char1 for i, (char1, char2) in enumerate(zip(typed_word, word)) if char1 == char2]
        matching_str = "".join(matching_chars)
        count_var = tk.StringVar()
        index = self.text.search(f"{matching_str}", self.word_position[-1], self.word_end_position[-1], count=count_var)
        self.text.tag_add('typed_char', index, "%s + %sc" % (index, count_var.get()))

    def remove_color(self, typed_word, word):
        matching_chars = [char1 for i, (char1, char2) in enumerate(zip(typed_word, word)) if char1 == char2]
        matching_str = "".join(matching_chars)
        if typed_word == matching_str:
            length = len(matching_str)
            position = self.current_position.split(".", 1)
            char_position = int(position[1]) + length
            char_position = position[0] + "." + str(char_position)
            self.text.tag_remove('typed_char', char_position)


class EntryFrame(ttk.Frame):
    def __init__(self, parent, background_color, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.style = ttk.Style()
        self.style.configure('EntryStyle.TEntry', fieldbackground=background_color, foreground='white')
        self.entry = ttk.Entry(self, font=('Arial', 28, 'bold'), style='EntryStyle.TEntry')
        self.entry.pack(fill='both', expand=True)
        self.focus_entry()

    def focus_entry(self):
        self.entry.focus_set()  # Make cursor active on Entry

    def clear_entry(self):
        self.entry.delete(0, tk.END)


class TypeTest:
    def __init__(self, num_words):
        self.num_words = num_words
        self.word_dictionary = get_english_words_set(['web2'])
        self.word_list = None
        self.word_iterator = None
        self.current_word = None
        self.current_word_number = 0
        self.previous_word = None
        self.entered_word = None
        self.begin_time = None
        self.test_time = None
        self.word_count = 0
        self.easy_difficulty = True

    def start_test(self):
        self.begin_time = time.time()
        self.current_word_number = 0
        self.word_count = 0
        self.init_test()

    def init_test(self):
        if self.easy_difficulty:
            self.set_easy_difficulty()
        else:
            self.set_hard_difficulty()
        self.word_iterator = cycle(self.word_list)
        self.word_count = len(self.word_list)
        self.initialize_word()

    def initialize_word(self):
        self.current_word = next(self.word_iterator)
        self.entered_word = ''

    def check_word(self, entered_word):
        self.entered_word = entered_word
        if self.entered_word == self.current_word:
            return True
        return False

    def next_word(self):
        self.previous_word = self.current_word
        self.current_word_number += 1
        self.initialize_word()

    def word_per_minute(self):
        minutes = self.test_time / 60
        return round(len(self.word_list) / minutes, 2)

    def end_test(self):
        if self.current_word_number == len(self.word_list):
            self.test_time = time.time() - self.begin_time
            print(f"Total time: {self.test_time}")
            print(f"Words per minute: {self.word_per_minute()}")
            return True
        return False

    def set_easy_difficulty(self):
        try:
            file_handle = open("word_list.txt", "r")
            data = file_handle.read()
            word_list = data.split("\n")
            self.word_list = choices(word_list, k=self.num_words)
            file_handle.close()
        except FileNotFoundError:
            print("The word library was not found.\n")
            exit()

    def set_hard_difficulty(self):
        self.word_list = choices(list(self.word_dictionary), k=self.num_words)