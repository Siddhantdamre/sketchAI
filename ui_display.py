import tkinter as tk
from PIL import Image, ImageTk

def display_sketch(image_path):
    root = tk.Tk()
    root.title("SketchArtIst")
    img = Image.open(image_path)
    img = img.resize((400, 400))
    tk_img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=tk_img)
    label.pack()
    root.mainloop()
