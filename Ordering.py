# Made by Maow
# https://github.com/MaowTheCat

from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Ordering")
window.geometry('650x700')
window.tk.call('tk', 'scaling', 2.0)

items_ordered = []

order_number = 0

def order(item):
    items_ordered.append(item)
    print(f"Added: {item}")
    print(items_ordered)

def complete_order():
    global order_number

    order_number += 1

    path = rf"Your Drive\order logs\order_{order_number}.txt" # Make sure to change before /order logs/order_{order_number}.txt wiht the file path of your order log folder

    with open(path, "w") as file:
        for item in items_ordered:
            file.write(item + "\n")

    items_ordered.clear()

    print("Order saved.")

drinks_lb = Label(window, text="Drinks")
drinks_lb.grid(column=0,row=0)

drink1 = Button(window, text="The Lobster", command=lambda: order("The Lobster"))
drink1.grid(column=0, row=1)

drink2 = Button(window, text="Strawberry Mojito", command=lambda: order("Starwberry Mojito"))
drink2.grid(column=0, row=2)

drink3 = Button(window, text="Raspberry Mojito", command=lambda: order("Raspberry Mojito"))
drink3.grid(column=0, row=3)

drink4 = Button(window, text="Watermelon Mojito", command=lambda: order("Watermelon Mojito"))
drink4.grid(column=0, row=4)

drink5 = Button(window, text="Pina Colada", command=lambda: order("Pina Colada"))
drink5.grid(column=0, row=5)

food_lb = Label(window, text="Food")
food_lb.grid(column=1,row=0)

food1 = Button(window, text="Fries with Sauce", command=lambda: order("Fries with Sauce"))
food1.grid(column=1, row=1)

complete_order_bt = Button(window, text="Complete Order", command=complete_order)
complete_order_bt.grid(column=2,row=0)

window.mainloop()