import tkinter as tk
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

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
def change_font(event):
    if font_option.get() == 'none':
        my_font = (font_family.get(), font_size.get())
    else:
        my_font = (font_family.get(), font_size.get(), font_option.get())

    # change font of text
    input_text.config(font=my_font)


def new_note():
    # use a messagebox to ask if user wants to save
    question = messagebox.askyesno(
        'New Note', 'Are you sure you want to start a new note?')
    if question == 1:
        # delete previous text
        input_text.delete('1.0', END)


def close_note():
    # use a messagebox to ask if user wants to save
    question = messagebox.askyesno(
        'Close Note', 'Are you sure you want to close the note?')
    if question == 1:
        # delete previous text
        root.destroy()


def save_note():
    # use a messagebox to ask if user wants to save
    # use filedialog to save file
    save_namw = filedialog.asksaveasfilename(initialdir='./',
                                             title='Save Note', filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(save_namw, 'w') as f:
        f.write(font_family.get() + '\n')
        f.write(str(font_size.get()) + '\n')
        f.write(font_option.get() + '\n')

        # add text to file
        f.write(input_text.get('1.0', END))


def open_note():
    # use filedialog to open file
    # use filedialog to get location of file
    open_name = filedialog.askopenfilename(
        initialdir='./', title='Open Note', filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(open_name, 'r') as f:
        # delete previous text
        input_text.delete('1.0', END)

        # read the contents of the file
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        # change the font
        change_font(1)

        # add text to file
        text = f.read()
        input_text.insert('1.0', text)


# Define Layout
# Define frames
menu_frame = tk.Frame(root, bg=menu_color)
text_frame = tk.Frame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

# Layout for menu frame
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tk.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tk.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tk.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tk.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

# create a list of font to use
families = ['Arial', 'Courier New', 'Comic Sans MS', 'Damascus',
            'Kefa', 'Symbol', 'Optima', 'Times New Roman', 'Verdana']
font_family = tk.StringVar()
font_family_drop = tk.OptionMenu(
    menu_frame, font_family, *families, command=change_font)
font_family.set('Terminal')
# set the width of the drop down menu
font_family_drop.config(width=10)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes = [8, 10, 12, 14, 16, 20, 24, 32, 48, 64, 72, 96]
font_size = tk.IntVar()
font_size_drop = tk.OptionMenu(
    menu_frame, font_size, *sizes, command=change_font)
font_size.set(12)
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['bold', 'italic', 'none']
font_option = tk.StringVar()
font_option_drop = tk.OptionMenu(
    menu_frame, font_option, *options, command=change_font)
font_option.set('none')
font_option_drop.config(width=3)
font_option_drop.grid(row=0, column=6, padx=5, pady=5)

# Layout for text frame
my_font = (font_family.get(), font_size.get())
input_text = tk.scrolledtext.ScrolledText(
    text_frame, width=1000, height=100, fg='#2a4d69', bg=text_color, font=my_font)
input_text.pack()


# run main loop
root.mainloop()
