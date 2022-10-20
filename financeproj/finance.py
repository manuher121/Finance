from tkinter import *
import sqlite3


def erase():
    e1.set("")
    e2.set("")
    e3.set("")


def create_db():
    conexion = sqlite3.connect("MySpending.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("CREATE TABLE MyOctoberSpending (Company VARCHAR(100),Type VARCHAR(100), Amount FLOAT)")
    except sqlite3.OperationalError:
        pass
    conexion.commit()
    conexion.close()


def submit():
    create_db()
    e1 = entry.get()
    e2 = entry2.get()
    e3 = entry3.get()
    if len(e1) and len(e2) and len(e3) != 0:
        try:
            ei3 = float(entry3.get())
        except ValueError:
            return
        else:
            conexion = sqlite3.connect("MySpending.db")
            cursor = conexion.cursor()

            cursor.execute(
                "INSERT INTO MyOctoberSpending VALUES('{}','{}','{}')".format(e1.capitalize(), e2.capitalize(), ei3))

            conexion.commit()
            conexion.close()
            erase()


def info():
    root = Tk()
    root.title("My Spendings")

    conexion = sqlite3.connect("MySpending.db")
    cursor = conexion.cursor()
    label1 = Label(root, text="Current spending for the month", bg="SlateBlue3", font=("Arial", 15)).pack(anchor='nw')
    money = 0
    sub = cursor.execute("SELECT * FROM MyOctoberSpending").fetchall()
    for a in sub:
        label2 = Label(root, text=("Company=>", a[0], "-Type=>", a[1],"Amount=>", a[2]), bg="SlateBlue3").pack(anchor='nw')
    sub2 = cursor.execute("SELECT Amount FROM MyOctoberSpending").fetchall()
    for a in sub2:
        money += float(a[0])
    label3 = Label(root, text=("Total_spent_this_month",money), bg="SlateBlue3", font=("Arial", 15), relief="ridge").pack(anchor='nw')
    print(money)

    conexion.commit()
    conexion.close()

    root.config(bg="SlateBlue3", bd=15, relief="ridge", width=1500, height=623)

    root.mainloop()

root = Tk()

root.overrideredirect(True)
root.config(bg="SlateBlue3",bd=2,relief="raised")


e1 = StringVar()
e2 = StringVar()
e3 = StringVar()

label = Label(root, bg="SlateBlue3", text="Spending company")
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)

entry = Entry(root, bg="SlateBlue3", textvariable=e1)
entry.grid(row=0, column=1, padx=5, pady=5)
entry.config(justify="left")

label2 = Label(root, bg="SlateBlue3", text="Type of spending")
label2.grid(row=1, column=0, sticky="w", padx=5, pady=5)

entry2 = Entry(root, bg="SlateBlue3", textvariable=e2)
entry2.grid(row=1, column=1, padx=5, pady=5)
entry2.config(justify="left")

label3 = Label(root, bg="SlateBlue3", text="Spending amount")
label3.grid(row=2, column=0, sticky="w", padx=5, pady=5)

entry3 = Entry(root, bg="SlateBlue3", textvariable=e3)
entry3.grid(row=2, column=1, padx=5, pady=5)
entry3.config(justify="left")

button1 = Button(root, text="Submit", bg="SlateBlue3", command=submit)
button1.grid(row=3, column=1, padx=5, pady=5)

button2 = Button(root, text="Info", bg="SlateBlue3", command=info)
button2.grid(row=3, column=0, padx=5, pady=5)

root.mainloop()
