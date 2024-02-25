from tkinter import *
from tkinter import messagebox
import pyperclip
import pyshorteners

root = Tk()
root.config(bg='cyan4')
root.attributes('-fullscreen', True)

def login():
    username = entry1.get()
    password = entry2.get()

    if username == '' and password == '':
        messagebox.showerror('login', 'Blanks are not allowed')
    elif username == 'abcd' and password == '1234':
        root.destroy()
        top = Tk()
        top.title("URL SHORTENER")
        top.config(bg='#49A')

        url = StringVar()
        url_address = StringVar()

        def urlshortener():
            url_add = url.get()
            url_short = pyshorteners.Shortener().tinyurl.short(url_add)
            url_address.set(url_short)

        def copy_url():
            url_short = url_address.get()
            pyperclip.copy(url_short)

        Label(top, text="My URL Shortener", font=("poppins")).pack(pady=10)
        Entry(top, textvariable=url).pack(pady=5)
        Button(top, text="Generate Short URL", command=urlshortener).pack(pady=7)
        Entry(top, textvariable=url_address).pack(pady=5)
        Button(top, text="COPY URL", command=copy_url).pack(pady=5)
        top.mainloop()

label1 = Label(root, text='Login Page', bg='cyan4', fg='cyan', font=('areal',24))
label1.place(x=560, y=80)
label2 = Label(root, text='UserName:', bg='cyan4', fg='white', font=('areal',20))
label2.place(x=310, y=190)
label3 = Label(root, text='Passsword:', bg='cyan4', fg='white', font=('areal',20))
label3.place(x=310, y=340)

entry1 = Entry(root, font=('areal', 15))
entry1.place(x=600, y=200)
entry2 = Entry(root, font=('areal', 15), show='.')
entry2.place(x=600, y=350)

button = Button(root, text='Login', bg='cyan3', font=('areal', 15), bd=5, command=login)
button.place(x=600, y=500)

root.mainloop()