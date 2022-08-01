from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
FONT = ("Arial", 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = [choice(letters) for _ in range(randint(8, 10))]  # list comprehension to select 8 to 10 random chars from letters array
    nr_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    nr_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list = nr_letters + nr_numbers + nr_symbols
    shuffle(password_list)
    password = "".join(password_list)
    pw_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    user = user_entry.get()
    password = pw_entry.get()
    new_data = {
        website: {
            "user": user,
            "password": password,
        }
    }

    # Check if fields are empty
    if len(website) == 0 or len(user) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Do not leave empty fields")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)  # get data from JSON file
        except FileNotFoundError:
            data = new_data
        else:
            data.update(new_data)
        finally:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
            website_entry.delete(0, END)
            pw_entry.delete(0, END)


# ----------------------------- SEARCH -------------------------------- #
def search():
    website = website_entry.get()
    if len(website) == 0:
        messagebox.showerror(title="Missing Entry", message="Please enter website to search")
    else:
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="FileNotFoundError", message="No data file found")
        else:
            if website in data:
                user = data[website]['user']
                password = data[website]['password']
                pyperclip.copy(password)
                messagebox.showinfo(title="User/Password", message=f"User: {user}\nPassword: {password}")
            else:
                messagebox.showwarning(title="Missing data", message=f"Website {website} not found")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()  # Create Tk window
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Create canvas to place image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Add labels
website_label = Label(text="Website:", font=FONT, bg="white")
website_label.grid(column=0, row=1, sticky=E)
user_label = Label(text="Email/Username:", font=FONT, bg="white")
user_label.grid(column=0, row=2, sticky=E)
pw_label = Label(text="Password:", font=FONT, bg="white")
pw_label.grid(column=0, row=3, sticky=E)

# Add entries
website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, sticky=W)
website_entry.focus()
user_entry = Entry(width=52)
user_entry.grid(column=1, row=2, columnspan=2, sticky=W)
user_entry.insert(0, "zimmerj314@pm.me")
pw_entry = Entry(width=32)
pw_entry.grid(column=1, row=3, sticky=W)

# Add buttons
generate_pw = Button(text="Generate Password", width=14, bg="white", command=generate_password)
generate_pw.grid(column=2, row=3)
add_pw = Button(text="Add", width=43, bg="white", command=save)
add_pw.grid(column=1, row=4, columnspan=2, sticky=W)
search = Button(text="Search", width=14, bg="white", command=search)
search.grid(column=2, row=1)












window.mainloop()