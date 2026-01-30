import tkinter
from pathlib import Path

PASS_PATH = "vault.txt"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    new_data = f"{website_entry.get()} | {email_entry.get()} | {password_entry.get()}\n"
    file_path = Path(PASS_PATH)
    saved_data = file_path.read_text()
    file_path.write_text(saved_data + new_data)

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

generate_button = tkinter.Button(text="Generate Password")
generate_button.grid(row=3, column=2)

add_button = tkinter.Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()