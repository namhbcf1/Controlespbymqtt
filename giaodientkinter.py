import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("600x600")
root.title('Control ESP by MQTT')

ID = tk.StringVar()
password = tk.StringVar()


signin = ttk.Frame(root)
signin.pack(padx=10, pady=10, fill='x', expand=True)


# ID
ID_label = ttk.Label(signin, text="ID :")
ID_label.pack(fill='x', expand=True)

ID_entry = ttk.Entry(signin, textvariable=ID)
ID_entry.pack(fill='x', expand=True)

password_label = ttk.Label(signin, text="Password:")
password_label.pack(fill='x', expand=True)

password_entry = ttk.Entry(signin, textvariable=password, show="*")
password_entry.pack(fill='x', expand=True)


login_button1 = ttk.Button(signin, text="b1")
login_button1.pack(fill='x', expand=True, pady=10)

login_button2 = ttk.Button(signin, text="b2")
login_button2.pack(fill='x', expand=True, pady=10)

login_button3 = ttk.Button(signin, text="b3")
login_button3.pack(fill='x', expand=True, pady=10)

login_button4 = ttk.Button(signin, text="sent")
login_button4.pack(fill='x', expand=True, pady=10)




root.mainloop()