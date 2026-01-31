import tkinter
import random
import string
import json
from tkinter import messagebox
from pathlib import Path

DATA_PATH = "vault.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def random_password():
    # remove text from password field
    password_entry.delete(0, tkinter.END)

    letters = [letter for letter in string.ascii_letters]
    numbers = [digit for digit in string.digits]
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)

    # copy password to clipboard
    window.clipboard_append(string=password)
    window.update()

    password_entry.insert(0, password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def check_fields():

    if all([website_entry.get(), email_entry.get(), password_entry.get()]):
        return True
    
    messagebox.showinfo(title="Password Manager", message="Please don't leave any fields empty!")
    return False

def save():
    if check_fields():
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()

        is_ok: bool = messagebox.askokcancel(title=website, message=f"These are the details entered:\nEmail: {email}\n"
                                                      f"Password: {password}\nIs it ok to save?")

        if is_ok:

            new_data = {website: {
                "email": email,
                "passowrd": password
            }}

            try:    
                with open(DATA_PATH, "r") as data_file:
                    data = json.load(data_file)

            except FileNotFoundError:
                with open(DATA_PATH, "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)

                with open(DATA_PATH, "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                clear_fields()
        

def clear_fields():
    website_entry.delete(0, tkinter.END)
    password_entry.delete(0, tkinter.END)

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
window.resizable(False, False)

# create canvas for logo img
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# other components (label, entry & button)
website_label = tkinter.Label(text="Website:")
website_label.grid(row=1, column=0)

website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = tkinter.Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = tkinter.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "test@gmail.com")

password_label = tkinter.Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = tkinter.Entry(width=21)
password_entry.grid(row=3, column=1)

generate_button = tkinter.Button(text="Generate Password", command=random_password)
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()