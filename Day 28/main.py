import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_letters=[random.choice(letters) for _ in range(nr_letters)]
  password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]
  password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]

  password_list=password_letters+password_symbols+password_numbers

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    

    if(len(website)==0 or len(password)==0):
        oops=messagebox.showinfo(title="OOPS",message="Please don't leave any fields empty!")
    else:
        is_ok=messagebox.askokcancel(title=website,message=f"These are the detailes entered: \nEmail: {email}\nPassword: {password}\nIs it ok to save?")

        if is_ok:
            new_data={
                website:{
                    "email":email,
                    "password":password,
                }
            }
            try:
                with open("Day 28/data.json",mode="r") as file:
                    data=json.load(file)
            except FileNotFoundError:
                with open("Day 28/data.json",mode="w") as data_file:
                    json.dump(new_data,data_file,indent=4)
            else:
                # Updating data
                data.update(new_data)
                with open("Day 28/data.json",mode="w") as data_file:
                    # Saving updated data
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)


def search():
    website=website_entry.get()
    try:
        with open("Day 28/data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error",message="No data file found.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email:{email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")
    
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
logo_image=PhotoImage(file="Day 28/logo.png")
canvas.create_image(100,100,image=logo_image)
canvas.grid(row=0,column=1)

website_label=Label(text="website:",font=("Arial",10,"normal"))
website_label.grid(row=1,column=0)

website_entry=Entry(width=17)
website_entry.grid(row=1,column=1,columnspan=1)
website_entry.focus()

search_button=Button(text="Search",width=13,command=search)
search_button.grid(row=1,column=2)

email_label=Label(text="Email/Username:",font=("Arial",10,"normal"))
email_label.grid(row=2,column=0)

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"abcd1234@gmail.com")

password_label=Label(text="Password:",font=("Arial",10,"normal"))
password_label.grid(row=3,column=0)

password_entry=Entry(width=17)
password_entry.grid(row=3,column=1,columnspan=1)

gen_password_button=Button(text="Generate Password",command=generate_password)
gen_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)
print(password_entry.get())
window.mainloop()