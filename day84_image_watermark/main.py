import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk, Toplevel
from ttkthemes import ThemedTk
from PIL import ImageTk, Image, ImageDraw, ImageFont


class WindowGUI(ThemedTk):
    def __init__(self):
        super().__init__()
        self.title("Watermarker")
        self.set_theme('black')
        self.background_frame = ttk.Frame(self, width=350, height=276)  # frame to p
        self.background_frame.pack(side='top', expand=True, fill='both')
        self.image_frame = ttk.Frame(self.background_frame, width=256, height=256, relief='ridge')  # frame to contain the image
        self.image_frame.pack(pady=20, padx=20, expand=False, fill='none')
        # Note that there is a bug in tk which does not store an image within a frame unless a
        # reference is stored as a class object attribute.
        self.filename = 'add_image.png'
        self.default_filename = self.filename
        self.image = Image.open(self.filename)
        self.tk_image = ImageTk.PhotoImage(self.image)
        self.image_label = ttk.Label(self.image_frame, image=self.tk_image)  # images are placed within labels
        self.image_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # place at the center of frame
        self.add_buttons()
        self.create_menu()
        self.watermark_text = None

    def add_buttons(self):
        button_frame = ttk.Frame(self, width=350, height=50)
        button_frame.pack(side='bottom', fill='both', expand=True)
        add_button = ttk.Button(button_frame, text="Add Image", width=10, command=self.add_image)
        add_watermark = ttk.Button(button_frame, text="Watermark", width=10, command=self.add_watermark)
        save_button = ttk.Button(button_frame, text="Save Image", width=10, command=self.save_image)
        add_button.place(relx=0.25, rely=0.5, anchor=tk.CENTER)
        add_watermark.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        save_button.place(relx=0.75, rely=0.5, anchor=tk.CENTER)

    def create_menu(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Add Image", command=self.add_image)
        file_menu.add_command(label="Add Watermark", command=self.add_watermark)
        file_menu.add_command(label="Save", command=self.save_image)
        file_menu.add_separator()
        file_menu.add_command(label="Quit", command=quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

    def add_image(self):
        try:
            filename = fd.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.bmp *.tiff"), ("All Files", "*.*")])
            self.filename = filename
            self.image = Image.open(filename)
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_frame.configure(height=self.image.height, width=self.image.width)
            self.image_label.configure(image=self.tk_image)
        except AttributeError:
            pass

    def add_watermark(self):
        if not self.filename == self.default_filename:
            self.call_popup()
            watermarked_image = self.image.copy()
            font, font_size = self.get_font()
            width, height = self.get_image_size()
            x = int(width / 100)
            y = height - int(height / 80) - font_size
            print(self.image.size, x, y, font_size)
            draw = ImageDraw.Draw(watermarked_image)
            draw.text((x, y), self.watermark_text, fill=(125, 125, 125), font=font)
            self.image = watermarked_image
            self.tk_image = ImageTk.PhotoImage(watermarked_image)
            self.image_label.configure(image=self.tk_image)

    def save_image(self):
        if not self.filename == self.default_filename:
            try:
                file = fd.asksaveasfile(initialfile=self.filename,
                                        defaultextension=self.filename[:3],
                                        filetypes=[("Image Files", "*.png *.jpg *.bmp *.tiff"), ("All Files", "*.*")])
                self.image.save(file)
            except ValueError:
                pass

    def get_font(self):
        width, height = self.get_image_size()
        half_width, half_height = int(width / 2), int(height / 2)
        if half_width > half_height:
            font_size = half_height
        else:
            font_size = half_width
        font_size = int(font_size / 8)
        font = ImageFont.truetype("arial.ttf", font_size)
        return font, font_size

    def get_image_size(self):
        return self.image.size

    def call_popup(self):
        popup = Popup(self)
        popup.wait_window()


# Use Toplevel class inheritance to pass information between parent and child windows
class Popup(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)
        self.parent = parent
        self.geometry("300x100")
        self.frame = ttk.Frame(self, width=300, height=100)  # frame to p
        self.frame.pack(side='top', expand=True, fill='both')
        self.label = ttk.Label(self.frame, text="Enter image watermark text")
        self.label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)
        self.entry = ttk.Entry(self.frame)
        self.entry.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        button = ttk.Button(self.frame, text="Ok", command=self.button_pressed)
        button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)
        self.grab_set()  # make it so master level cannot be closed while this window is open
        self.entry.focus_set()  # focus on the entry widget
        self.entry.bind('<Return>', self.button_pressed)

    # Note that when binding widget to a function, an event parameter is passed
    def button_pressed(self, event=None):
        self.parent.watermark_text = self.entry.get()
        self.exit_popup()

    def exit_popup(self):
        self.destroy()


def main():
    window = WindowGUI()
    window.mainloop()


if __name__ == '__main__':
    main()
