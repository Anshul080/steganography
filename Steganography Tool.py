from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os
from stegano import lsb

# Initialize the main window
root = Tk()
root.title("Steganography Tool")
root.geometry("850x650")
root.resizable(False, False)
root.config(bg="lightblue")

# Function to select an image
def select_image():
    global filename
    filename = filedialog.askopenfilename(
        initialdir=os.getcwd(),
        title="Select Image File",
        filetypes=(("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")),
    )
    if filename:
        img = Image.open(filename)
        img = img.resize((250, 250))  # Resize the image for display
        img = ImageTk.PhotoImage(img)
        lbl.configure(image=img, width=250, height=250)
        lbl.image = img

# Function to hide a message in the image
def hide_image():
    if not filename:
        messagebox.showerror("Error", "Please select an image first.")
        return
    message = text1.get(1.0, END).strip()
    if not message:
        messagebox.showerror("Error", "Please enter a message to hide.")
        return
    secret = lsb.hide(filename, message)
    secret.save("hidden_image.png")
    messagebox.showinfo("Success", "Message hidden successfully in 'hidden_image.png'.")

# Function to reveal a hidden message from the image
def show_message():
    if not filename:
        messagebox.showerror("Error", "Please select an image first.")
        return
    try:
        clear_message = lsb.reveal(filename)
        if clear_message:
            text1.delete(1.0, END)
            text1.insert(END, clear_message)
        else:
            messagebox.showinfo("Error", "No message found in the image.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to save the image with the hidden message
def save_message():
    if not filename:
        messagebox.showerror("Error", "Please select an image first.")
        return
    message = text1.get(1.0, END).strip()
    if not message:
        messagebox.showerror("Error", "Please enter a message to save.")
        return
    secret = lsb.hide(filename, message)
    secret.save("secret_image.png")
    messagebox.showinfo("Success", "Message saved in 'secret_image.png'.")
    text1.delete(1.0, END)

# Set the app icon
image_icon = PhotoImage(file=r"C:\Users\Stany Cyril\Downloads\logo.jpg")
root.iconphoto(False, image_icon)

# Header section
header_frame = Frame(root, bg="lightblue")
header_frame.pack(pady=20)

logo = PhotoImage(file=r"C:\Users\Stany Cyril\Downloads\logo1.png")
Label(header_frame, image=logo, bg="lightblue").pack(side=LEFT, padx=10)
Label(header_frame, text="Steganography Tool", font=("Arial", 28, "bold"), bg="lightblue").pack(side=LEFT)

# Image display frame
f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=50, y=120)
lbl = Label(f, text="Select Image", font=("Arial", 12), bg="black", fg="white")
lbl.place(x=45, y=100)

# Text input frame
frame2 = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
frame2.place(x=450, y=120)

text1 = Text(frame2, width=40, height=10, font=("Arial", 12), bg="white", fg="black")
text1.place(x=10, y=10)
text1.insert(END, "Enter your secret message here")

scrollbar1 = Scrollbar(frame2, orient=VERTICAL, command=text1.yview)
text1.config(yscrollcommand=scrollbar1.set)
scrollbar1.place(x=320, y=10, height=230)

# Buttons for image selection and saving
frame3 = Frame(root, bd=3, bg="black", width=340, height=100, relief=GROOVE)
frame3.place(x=50, y=420)

Label(frame3, text="Image Options", font=("Arial", 12, "bold"), bg="black", fg="yellow").place(x=20, y=5)
Button(frame3, text="Select Image", font=("Arial", 12), bg="lightblue", command=select_image).place(x=20, y=40)
Button(frame3, text="Save Image", font=("Arial", 12), bg="lightblue", command=save_message).place(x=180, y=40)

# Buttons for hiding and revealing data
frame4 = Frame(root, bd=3, bg="black", width=340, height=100, relief=GROOVE)
frame4.place(x=450, y=420)

Label(frame4, text="Data Options", font=("Arial", 12, "bold"), bg="black", fg="yellow").place(x=20, y=5)
Button(frame4, text="Hide Data", font=("Arial", 12), bg="lightblue", command=hide_image).place(x=20, y=40)
Button(frame4, text="Show Data", font=("Arial", 12), bg="lightblue", command=show_message).place(x=180, y=40)

# Run the main loop
root.mainloop()