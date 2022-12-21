from tkinter import *
from tkinter import messagebox
from password_generator import gen_passwd

def generate_password():
    pass_input.delete(0, END)
    passwd = gen_passwd()
    pass_input.insert(0, passwd)

def saveCredentials():
    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    
    if website == '' or email == '' or password == '':
        return messagebox.showwarning(title="Hmm", message="All fields are required.")
    
    confirm = messagebox.askokcancel(title=website, message=f"Credentials entered. \nEmail: {email} \nPassword: {password} \nAre you sure to save?")
    if confirm:
        with open("data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            pass_input.delete(0, END)
        
window = Tk()
window.title("Advanced Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(126, 100, image=logo)
canvas.grid(column=2, row=1)

#Labels
website_l = Label(text="Website:")
website_l.grid(column=1, row=2)
email_l = Label(text="Email/Username:")
email_l.grid(column=1, row=3)
pass_l = Label(text="Password:")
pass_l.grid(column=1, row=4)
# Input Fields
website_input = Entry(width=40)
website_input.grid(column=2, row=2, pady=10, padx=2, columnspan=2)
website_input.focus()
email_input = Entry(width=40)
email_input.grid(column=2, row=3, pady=10, padx=2, columnspan=2)
email_input.insert(0, 'juba@gmail.com')  # Here you can pre-define default email used mostly
pass_input = Entry(width=21)
pass_input.grid(column=2, row=4)
# Buttons
generate_btn = Button(text="Generate Password", bg="white", width=15, command=generate_password)
generate_btn.grid(column=3, row=4)
add_btn = Button(text='Add', width=38, command=saveCredentials)
add_btn.config(bg="#3CB043", fg="white", activebackground="#D0312D", activeforeground="white", relief=RAISED, cursor="hand2")
add_btn.grid(column=2, row=5, columnspan=2, pady=10)

window.mainloop()