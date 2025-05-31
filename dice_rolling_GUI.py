import tkinter as tk
from PIL import Image, ImageTk
import random
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

window = ttk.Window(themename="cosmo")
window.geometry("800x930")
window.title("Dice Roll")

bg_img_original = Image.open("Background.png").resize((800, 930), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_img_original)

bg_label = tk.Label(window, image=bg_photo)
bg_label.image = bg_photo
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

dice = ["die1.png", "die2.png", "die3.png", "die4.png", "die5.png", "die6.png"]
dice_x1, dice_y1 = 100, 420
dice_x2, dice_y2 = 400, 420

composite_label = tk.Label(window)
composite_label.place(x=0, y=0)

def dice_roll():
    combined = bg_img_original.copy()
    die1 = Image.open(random.choice(dice)).convert("RGBA")
    die2 = Image.open(random.choice(dice)).convert("RGBA")
    combined.paste(die1, (dice_x1, dice_y1), mask=die1)
    combined.paste(die2, (dice_x2, dice_y2), mask=die2)
    composite_image = ImageTk.PhotoImage(combined)
    composite_label.config(image=composite_image)
    composite_label.image = composite_image

dice_roll()

style = ttk.Style()
style.configure('danger.TButton',
                font=('Lemon Funky', 32, 'bold'),
                padding=10,
                background='#D74689',
                foreground='white',
                bordercolor='black',
                borderwidth=2,
                relief='groove')
button = ttk.Button(
    window,
    text="Roll",
    style='danger.TButton',
    command=dice_roll
)
button.place(x=320, y=720)

window.mainloop()