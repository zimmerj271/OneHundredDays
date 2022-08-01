import tkinter as tk

window = tk.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

my_label = tk.Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.grid(column=1, row=1)
my_label.config(padx=50, pady=50)

# Button
# def button_clicked():
#     print("I got clicked")
#
# def label_change():
#     my_label.config(text="I got clicked!")

# button = tk.Button(text="Click Me", command=button_clicked)
# button.pack()

# button2 = tk.Button(text="Click Me Too", command=label_change)
# button2.pack()

# Entry
def button_clicked():
    my_label.config(text=input_str.get())

input_str = tk.Entry(width=10)
button = tk.Button(text="Click Me", command=button_clicked)
button.grid(column=2, row=2)
new_button = tk.Button(text="New Button")
new_button.grid(column=3, row=1)
input_str.grid(column=4, row=3)




window.mainloop()
