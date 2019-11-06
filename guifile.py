import tkinter as tk
from PIL import ImageTk, Image
window = tk.Tk()
window.title("Join")
window.geometry("300x300")
window.configure(background='grey')
path = "resized//frame0.jpg"
name="Manshi"
img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(window, image = img)
panel1=tk.Label(window,text=name)
panel.pack(side = "bottom", fill = "both", expand = "yes")
panel1.pack()
window.mainloop()