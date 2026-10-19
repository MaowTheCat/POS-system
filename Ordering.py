# Made by Maow
# https://github.com/MaowTheCat

# Don't worry about this stuff scroll down
from tkinter import *
from tkinter import messagebox
import os

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

def order_alc(item):
    alcohol = Toplevel(window)
    alcohol.title("Alcohol Configuration")
    alcohol.geometry('400x200')
    alcohol.tk.call('tk', 'scaling', 2.0)
    
    def close_window():
        alcohol.destroy()

    confirm_alc = Button(
        alcohol, 
        text="Alcohol", 
        command=lambda: [order(item + " (Alcohol)"), close_window()]
    )
    confirm_alc.grid(column=0, row=0, padx=20, pady=20)
    
    deny_alc = Button(
        alcohol, 
        text="No Alcohol", 
        command=lambda: [order(item + " (No Alcohol)"), close_window()]
    )
    deny_alc.grid(column=1, row=0, padx=20, pady=20)

def complete_order():
    global order_number
    if not items_ordered:
        messagebox.showwarning("Empty Order", "No items have been selected yet!")
        return
        
    order_number += 1
    
    log_dir = r"order logs"
    path = os.path.join(log_dir, f"order_{order_number}.txt")
    
    try:
        # Create directory structure if it doesn't exist
        if not os.path.exists(log_dir) and log_dir != "Your Drive\\order logs":
            os.makedirs(log_dir)
            
        with open(path, "w") as file:
            for item in items_ordered:
                file.write(item + "\n")
        
        messagebox.showinfo("Success", f"Order #{order_number} saved successfully!")
        items_ordered.clear()
        print("Order saved.")
    except Exception as e:
        messagebox.showerror("Error", f"Could not save file. Verify your file path layout.\nError: {e}")

def order_delete():
    items_ordered.clear()
    print("Order deleted.", items_ordered)

# Menu
drinks_lb = Label(window, text="Drinks")
drinks_lb.grid(column=0)

drink1 = Button(window, text="The Lobster", command=lambda: order("The Lobster"))
drink1.grid(column=0, row=1)

drink2 = Button(window, text="Strawberry Mojito", command=lambda: order_alc("Strawberry Mojito"))
drink2.grid(column=0, row=2)

drink3 = Button(window, text="Raspberry Mojito", command=lambda: order_alc("Raspberry Mojito"))
drink3.grid(column=0, row=3)

drink4 = Button(window, text="Watermelon Mojito", command=lambda: order_alc("Watermelon Mojito"))
drink4.grid(column=0, row=4)

drink5 = Button(window, text="Pina Colada", command=lambda: order_alc("Pina Colada"))
drink5.grid(column=0, row=5)

drink6 = Button(window, text="Mixed Fruit Mojito", command=lambda: order_alc("Mixed Fruit Mojito"))
drink6.grid(column=0, row=6)

shots_lb = Label(window, text="Shots")
shots_lb.grid(column=0, row=7)

shot1 = Button(window, text="White Rum", command=lambda: order("White Rum Shot"))
shot1.grid(column=0, row=8)

shot2 = Button(window, text="Vodka", command=lambda: order("Vodka Shot"))
shot2.grid(column=0, row=9)

shot3 = Button(window, text="Gin", command=lambda: order("Gin Shot"))
shot3.grid(column=0, row=10)

food_lb = Label(window, text="Food")
food_lb.grid(column=1, row=0)

food1 = Button(window, text="Fries with Sauce", command=lambda: order("Fries with Sauce"))
food1.grid(column=1, row=1)

food2 = Button(window, text="Grapes", command=lambda: order("Grapes"))
food2.grid(column=1, row=2)

food3 = Button(window, text="Pizza Toast", command=lambda: order("Pizza Toast"))
food3.grid(column=1, row=3)

complete_order_bt = Button(window, text="Complete Order", command=complete_order)
complete_order_bt.grid(column=2, row=0)

delete_order_bt = Button(window, text="Delete Order", command=order_delete)
delete_order_bt.grid(column=2, row=1)

window.mainloop()