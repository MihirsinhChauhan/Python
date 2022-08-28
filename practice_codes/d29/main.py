from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- SEARCH BUTTON ------------------------------- #
def search():
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
            for website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website,message=f"email: {email}\n password: {password}")
    except:
        messagebox.showerror(title="Oops",message= "No entry Founnd!")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []
    let = [random.choice(letters) for _ in range(nr_letters)]
    sym = [random.choice(symbols) for _ in range(nr_symbols)]
    num = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list.extend(let)
    password_list.extend(sym)
    password_list.extend(num)

    random.shuffle(password_list)

    password = "".join(password_list)
    pass_input.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    password = pass_input.get()
    email = email_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(password) == 0 or len(website) == 0:
        messagebox.showerror(title="Oops", message="Please don,t leave any field empty!")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

        finally:
            website_input.delete(0, END)
            pass_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=1, column=1)

website_label = Label(text="Website :", font=("Courier", 12, "normal"))
website_label.grid(row=2, column=0)

website_input = Entry(width=35)
website_input.grid(row=2, column=1, columnspan=1)
website_input.focus()

search = Button(text="search",width= 12,command=search)
search.grid(row=2, column=2)

email_label = Label(text="Email/Username :", font=("Courier", 12, "normal"))
email_label.grid(row=3, column=0)

email_input = Entry(width=35)
email_input.grid(row=3, column=1, columnspan=2)
email_input.insert(0, "mihirchauhan473@gmail.com")

pass_label = Label(text="Password :", font=("Courier", 12, "normal"))
pass_label.grid(row=4, column=0)

pass_button = Button(text="Generate Password", command=generate_pass)
pass_button.grid(row=4, column=2)

pass_input = Entry(width=21)
pass_input.grid(row=4, column=1)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(row=5, column=1, columnspan=2)
window.mainloop()
