import tkinter as tk
from PIL import ImageTk, Image

# define window
root = tk.Tk()
root.title('Notepad')
root.iconbitmap('pad.ico')
root.geometry("600x600")
root.resizable(0, 0)

# Define fonts and colors
text_color = "#e7eff6"
menu_color = "#adcbe3"
root_color = "#4b86b4"
root.config(bg=root_color)


# Define functions


# Define Layout
# Define frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tk.Button(menu_frame, image=new_image)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tk.Button(menu_frame, image=open_image)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tk.Button(menu_frame, image=save_image)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tk.Button(menu_frame, image=close_image, command=root.quit)
close_button.grid(row=0, column=3, padx=5, pady=5)


# run main loop
root.mainloop()
