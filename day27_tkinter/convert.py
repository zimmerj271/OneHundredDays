import tkinter as tk

FONT = ("Arial", 12)

window = tk.Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

def miles_to_km():
    miles = mile_to_convert.get()
    km = float(miles) * 1.609
    mile_to_km_label.config(text=f"{km}")

# Create Tk objects to display
mile_to_convert = tk.Entry(width=5)
mile_to_convert.insert(0, "0")  # insert a value into entry object at start
mile_label = tk.Label(text="Miles", font=FONT)
equal_label = tk.Label(text="is equal to", font=FONT)
mile_to_km_label = tk.Label(text="0", font=FONT)
km_label = tk.Label(text="km", font=FONT)
button = tk.Button(text="Calculate", command=miles_to_km)

# Place objects on grid
mile_to_convert.grid(column=2, row=1)
mile_label.grid(column=3, row=1)
equal_label.grid(column=1, row=2)
mile_to_km_label.grid(column=2, row=2)
km_label.grid(column=3, row=2)
button.grid(column=2, row=3)




window.mainloop()