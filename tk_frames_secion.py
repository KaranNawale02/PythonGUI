import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk  # Import Pillow (PIL) for handling images
import os
from os import getcwd

# Create the main window
root = tk.Tk()

# Set the window size
root.geometry("800x600")

# Create the menu bar
menu = Menu(root, background="#2e7dcb")
root.config(menu=menu)

# Create File menu
filemenu = Menu(menu, background="white")
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New')
filemenu.add_command(label='Open...')
filemenu.add_separator()
filemenu.add_command(label='Exit', command=root.quit)

# Create Connection menu
helpmenu = Menu(menu)
menu.add_cascade(label='Connection', menu=helpmenu)
helpmenu.add_command(label="Connect")
helpmenu.add_command(label="COM Port")

# Create Views menu
viewsmenu = Menu(menu)
menu.add_cascade(label="Views", menu=viewsmenu)
viewsmenu.add_command(label="Exit")

# Create the upper section (header) with a blue background and border
header_frame = tk.Frame(root, bg="#2e7dcb", height=50, bd=2, relief="solid")
header_frame.grid(row=0, column=0, columnspan=2, sticky="ew")  # Span horizontally but don't stretch

# Create the left section (sidebar) with a blue background and border
sidebar_frame = tk.Frame(root, bg="#2e7dcb", width=100, bd=2, relief="solid")
sidebar_frame.grid(row=1, column=0, sticky="ns", rowspan=2)  # Stretch vertically but don't stretch horizontally

# Create the right section (content area) with a warm white background and border
content_frame = tk.Frame(root, bg="#ffefbf", bd=2, relief="solid")
content_frame.grid(row=1, column=1, sticky="nsew", rowspan=2)

# Load the image using Pillow (PIL)
img_path = os.path.join(getcwd(), "gen-ai.png")
try:
    # Open the image using PIL
    img = Image.open(img_path)
    img = img.resize((50, 50), Image.Resampling.LANCZOS)

    # Convert the image to a format Tkinter can work with
    img_tk = ImageTk.PhotoImage(img)
    # Display the image in the header frame
    image_label = tk.Label(header_frame, image=img_tk, bg="#2e7dcb")
    image_label.grid(row=0, column=0, padx=20)  # Add padding for spacing from the left edge

    # Keep a reference to the image object to prevent garbage collection
    image_label.image = img_tk
except Exception as e:
    print(f"Error loading image: {e}")


def on_button_click(button_name):
    if button_name == "add":
        try:
            a = int(valu1.get())
            b = int(val2.get())
            sum = a + b
            label.config(text=f"Addition = {sum}")
        except:
            label.config(text=f"Only Interfers are allowed !")

    elif button_name == "sub":
        try:
            a = int(valu1.get())
            b = int(val2.get())
            sub = a - b
            label.config(text=f"substraction = {sub}")
        except:
            label.config(text=f"Only Intgers are allowed !")

    elif button_name == "mul":
        try:
            a = int(valu1.get())
            b = int(val2.get())
            mul = a * b
            label.config(text=f"Multiplication = {mul}")
        except:
            label.config(text=f"Only intergers are allowed !")

# Create a label widget
name = tk.Label(content_frame,text="Simplee Calculator", font=("Arial",30))
name.pack(pady=20)
label = tk.Label(content_frame,
                 text="Enter Two Numbers ",
                 font=("Arial", 24), bg="lightblue")
label.pack(pady=20)

valu1 = tk.Entry(content_frame, font=("Arial", 18))
valu1.pack(pady=20)

val2 = tk.Entry(content_frame,font=("Arial",18))
val2.pack(pady=20)

button4 = tk.Button(content_frame, text="Addition",
                    font=("Arial", 18),
                    command=lambda: on_button_click("add"))
button4.pack(pady=10)

button3 = tk.Button(content_frame, text="Substract",
                    font=("Arial", 18),
                    command=lambda: on_button_click("sub"))
button3.pack(pady=10)

button2 = tk.Button(content_frame, text="Multiplication",
                    font=("Arial", 18),
                    command=lambda: on_button_click("mul"))
button2.pack(pady=10)

# Configure the grid layout to allow resizing of the content frame but not others
root.grid_rowconfigure(0, weight=0)  # Don't resize header
root.grid_rowconfigure(1, weight=1)  # Allow content frame to resize vertically
root.grid_rowconfigure(2, weight=1)  # Allow content frame to resize vertically

root.grid_columnconfigure(0, weight=0)  # Don't resize sidebar
root.grid_columnconfigure(1, weight=1)  # Makes the content area expand horizontally

# Run the application
root.mainloop()
