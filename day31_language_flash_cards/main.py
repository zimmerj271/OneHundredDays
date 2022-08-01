from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"

try:
    df = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    df = pd.read_csv("data/french_words.csv")

current_card = pd.DataFrame()  # empty dataframe to save random row from df


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # Stop timer so that it doesn't run in the background
    current_card = df.sample()
    french_word = current_card['French'].item()
    canvas.itemconfigure(canvas_image, image=front_card_img)
    canvas.itemconfigure(language_text, text="French", fill="black")
    canvas.itemconfigure(word_text, text=french_word, fill="black")
    flip_timer = window.after(3000, func=flip_card)  # restart timer


def flip_card():
    global current_card
    english_word = current_card['English'].item()
    canvas.itemconfigure(canvas_image, image=back_card_img)
    canvas.itemconfigure(language_text, text="English", fill="white")
    canvas.itemconfigure(word_text, text=english_word, fill="white")

def remove_card():
    global current_card, df
    row_index = current_card.index[0]
    df.drop(labels=row_index, axis=0, inplace=True)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()  # create Tk window
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

# Create canvas to place image
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_card_img = PhotoImage(file="images/card_front.png")
back_card_img = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Add text to canvas
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
# canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 253, text="", font=("Arial", 60, "bold"))
# canvas.create_text(400, 253, text="trouve", font=("Arial", 60, "bold"))

# Add buttons
known_image = PhotoImage(file="images/right.png")
unknown_image = PhotoImage(file="images/wrong.png")
known_button = Button(image=known_image, highlightthickness=0, command=remove_card)
unknown_button = Button(image=unknown_image, highlightthickness=0, command=next_card)
known_button.grid(column=0, row=1)
unknown_button.grid(column=1, row=1)
next_card()

window.mainloop()
