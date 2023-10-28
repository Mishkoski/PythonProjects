import tkinter
import tkinter as tk
import json
from tkinter import messagebox

screen = tk.Tk()
screen.title("Banking")
screen.geometry("250x400")

screen.configure(bg="black")
image = tk.PhotoImage(file="bank_PNG15.png")
image_label = tk.Label(screen, image=image, bg="black")
image_label.grid(column=1, row=0)

label1 = tkinter.Label(text="Banking System", bg="black", fg="white", font=("Arial", 12, "bold"))
label1.grid(column=1, row=1, padx=60)

label2 = tkinter.Label(text="Login:", bg="black", fg="white")
label2.grid(column=1, row=2)

entry_three = tkinter.Entry()
entry_three.grid(column=1, row=3, padx=60)
entry_three.configure(bg="grey")
entry_three.insert(0, "UserName")

entry_four = tkinter.Entry()
entry_four.grid(column=1, row=4, padx=60)
entry_four.configure(bg="grey")
entry_four.insert(0, "Password")


def check_username(username, password):
    try:
        with open("data.json", "r") as json_file:
            data = json.load(json_file)
            if username in data and data[username]["password"] == password:
                return True
            else:
                return False
    except FileNotFoundError:
        messagebox.showerror("Error", "Data file not found!")
        return False


def new_window_login(username, password):
    def new_window_change_password():
        def change_password():
            # nonlocal username
            previous_password = entry_change_one.get()
            new_password = entry_change_two.get()
            confirm_password = entry_change_three.get()

            try:
                with open("data.json", "r") as json_file:
                    data = json.load(json_file)

                    # Check if the previous password matches the stored password for the user
                    if data[username]["password"] == previous_password:
                        # Check if the new password and confirm password match
                        if new_password == confirm_password:
                            # Update the password in the data dictionary
                            data[username]["password"] = new_password

                            # Save the updated data back to the JSON file
                            with open("data.json", "w") as json_file:
                                json.dump(data, json_file)

                            messagebox.showinfo("Success", "Password changed successfully.")
                            change_password_window.destroy()
                        else:
                            messagebox.showerror("Error", "New password and confirm password do not match.")
                    else:
                        messagebox.showerror("Error", "Incorrect previous password.")
            except FileNotFoundError:
                messagebox.showerror("Error", "Data file not found.")


        change_password_window = tk.Tk()
        change_password_window.title("Change Password")
        change_password_window.geometry("300x250")
        change_password_window.configure(bg="black")

        entry_change_one = tkinter.Entry(change_password_window, width=30)
        entry_change_one.grid(column=0, row=1, padx=50, pady=20, sticky='w')
        entry_change_one.configure(bg="grey")
        entry_change_one.insert(0, "Enter your previous password")

        entry_change_two = tkinter.Entry(change_password_window, width = 30)
        entry_change_two.grid(column = 0, row = 2, padx=50, pady=20, sticky='w')
        entry_change_two.configure(bg = "grey")
        entry_change_two.insert(0, "Enter your new password")

        entry_change_three = tkinter.Entry(change_password_window, width = 30)
        entry_change_three.grid(column = 0, row = 3, padx=50, pady=20, sticky='w')
        entry_change_three.configure(bg = "grey")
        entry_change_three.insert(0, "Confirm your new password")

        button_change = tk.Button(change_password_window, text = "Change your password", bg = "light blue", command = change_password)
        button_change.grid(column = 0, row = 4, pady = 10)

        change_password_window.mainloop()


    def add_to_balance(amount, username):
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
                # Update the balance in the data dictionary
                data[username]["balance"] += amount

            # Save the updated data back to the JSON file
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)

            messagebox.showinfo("Success", f"{amount} added to your balance.")
            label.config(text = "Balance: " + str(data[username]["balance"]) )
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found!")

    def reduce_from_balance(amount, username):
        try:
            with open("data.json", "r") as json_file:
                data = json.load(json_file)
                # Update the balance in the data dictionary
                data[username]["balance"] -= amount

            # Save the updated data back to the JSON file
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
                messagebox.showinfo("Success", f"{amount} deducted from your balance.")
                label.config(text = "Balance: " + str(data[username]["balance"]) )
        except FileNotFoundError:
            messagebox.showerror("Error", "Data file not found!")

    if check_username(username, password):
        balance = 0
        with open("data.json", "r") as b:
            balance = json.load(b)[username]["balance"]
        new_window = tk.Tk()
        new_window.title("Login")
        new_window.geometry("550x180")
        new_window.configure(bg="black")

        label = tk.Label(new_window, text="Balance: " + str(balance), bg="black", fg="white")
        label.grid(column=0, row=0)

        # Iznosot na pari kaj vnesi ili iznesi
        entry_one = tk.Entry(new_window)
        entry_one.grid(column=0, row=1, columnspan=2)
        entry_one.configure(bg="grey")

        button1 = tk.Button(new_window, text="Vnesi", bg="light blue", command=lambda: add_to_balance(int(entry_one.get()), username))
        button1.grid(column=0, row=2)

        button2 = tk.Button(new_window, text="Iznesi", bg="light blue", command=lambda: reduce_from_balance(int(entry_one.get()), username))
        button2.grid(column=1, row=2)

        label1 = tk.Label(new_window, text="Ispratete pari do:", bg="black", fg="white", padx=115)
        label1.grid(column=4, row=0)

        entry_two = tk.Entry(new_window, width=30)
        entry_two.grid(column=4, row=1)
        entry_two.configure(bg="grey")
        entry_two.insert(0, "UserName")

        entry_six = tk.Entry(new_window, width=30)
        entry_six.grid(column=4, row=2)
        entry_six.configure(bg="grey")
        entry_six.insert(0, "Kolku pari sakate da ispratite?")

        entry_five = tk.Entry(new_window, width=30)
        entry_five.grid(column=4, row=3)
        entry_five.configure(bg="grey")
        entry_five.insert(0, "Vnesete go vashiot password")

        def transfer_funds():
            recipient_username = entry_two.get()
            amount = int(entry_six.get())
            sender_password = entry_four.get()

            if check_username(username, sender_password):
                try:
                    with open("data.json", "r") as json_file:
                        data = json.load(json_file)
                        if entry_five.get() == sender_password:


                            # Check if sender has sufficient balance
                            if data[username]["balance"] >= amount:
                                # Reduce amount from sender's balance
                                data[username]["balance"] -= amount

                                # Add amount to recipient's balance
                                data[recipient_username]["balance"] += amount

                                # Save the updated data back to the JSON file
                                with open("data.json", "w") as json_file:
                                    json.dump(data, json_file)

                                messagebox.showinfo("Success", f"{amount} transferred to {recipient_username}.")
                                p = entry_three.get()
                                print(p)
                                label.config(text="Balance: " + str(data[entry_three.get()]["balance"]))

                            else:
                                messagebox.showerror("Error", "Insufficient balance.")
                        else:
                            messagebox.showerror("Error", "Incorrect Password")
                except FileNotFoundError:
                    messagebox.showerror("Error", "Data file not found.")
            else:
                messagebox.showerror("Error", "Invalid recipient username or password.")

        button3 = tk.Button(new_window, text="Confirm Transfer", bg="light blue", command=transfer_funds)
        button3.grid(column=4, row=4, columnspan=2)

        button4 = tk.Button(new_window, text="Change password", bg="light blue",command = new_window_change_password)
        button4.grid(column=8, row=8, padx=1, pady=40)

        new_window.mainloop()
    else:
        messagebox.showerror("Error", "Invalid User")


button = tkinter.Button(text="Login", bg="light blue", command = lambda: new_window_login(entry_three.get(), entry_four.get()))
button.grid(column=1, row=5)

label5 = tkinter.Label(text="Don't have an account?", bg="black", fg="white")
label5.grid(column=1, row=7)

button2 = tkinter.Button(text="Register", bg="light blue")
button2.grid(column=1, row=8)


def new_window_register():
    def save_to_json():
        username = entry_username.get()
        password = entry_password.get()
        data = {username: {"password": password, "balance": 0}}
        with open("data.json", "r") as d:
            datta = json.load(d)
            datta.update(data)

        with open("data.json", "w") as json_file:
            json.dump(datta, json_file)

        new_window.destroy()

    new_window = tk.Tk()
    new_window.title("Registration")
    new_window.geometry("250x160")
    new_window.configure(bg="black")

    entry_username = tk.Entry(new_window)
    entry_username.grid(column=0, row=0, padx=50, pady=20, sticky='w')
    entry_username.insert(0, "Username")
    entry_username.configure(bg = "grey")

    entry_password = tk.Entry(new_window)
    entry_password.grid(column=0, row=1, padx=50, pady=20, sticky='w')
    entry_password.insert(0, "Password")
    entry_password.configure(bg = "grey")

    # Register button
    button_register = tk.Button(new_window, text="Register", bg="light blue", command=save_to_json)
    button_register.grid(column=0, row=2, pady=10)

    new_window.mainloop()


button2 = tkinter.Button(text="Register", command=new_window_register, bg="light blue")
button2.grid(column=1, row=8)

label6 = tkinter.Label(text="Forgot your password?", bg="black", fg="white")
label6.grid(column=1, row=9)

button3 = tkinter.Button(text="Reset password", bg="light blue")
button3.grid(column=1, row=10)

screen.mainloop()
