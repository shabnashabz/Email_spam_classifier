import tkinter as tk
from tkinter import messagebox
import joblib

model = joblib.load("model/spam_classifier.pkl")

def classify_email():
    email_text = email_entry.get("1.0", tk.END).strip()
    if email_text:
        result = model.predict([email_text])[0]
        messagebox.showinfo("Classification Result", f"The email is classified as: {result}")
    else:
        messagebox.showwarning("Input Error", "Please enter an email text.")

root = tk.Tk()
root.title("Spam Classifier")
root.geometry("400x300")

title_label = tk.Label(root, text="Email Spam Classifier", font=("Helvetica", 16))
title_label.pack(pady=10)

instruction_label = tk.Label(root, text="Enter email text below:")
instruction_label.pack()

email_entry = tk.Text(root, height=10, width=40)
email_entry.pack(pady=10)

classify_button = tk.Button(root, text="Classify", command=classify_email)
classify_button.pack(pady=5)

root.mainloop()
