import tkinter as tk
from typing import ItemsView

import pandas as pd
from matplotlib import pyplot as plt


root = tk.Tk()
root.geometry("1000x450")
root.title("Expenditure_Tracker")
root.configure(background="#232323")

item_list = []


def add_item():
    #print("I want to add item")
    item= item_text.get()
    quantity = quantity_text.get()
    cost = cost_text.get()
    total = int(quantity) * int(cost)
    print(item,quantity,cost,total)

    single_item={"Item": item,"Quantity": quantity,"Cost": cost,"Total Amount":total}
    single_item_lbl = tk.Label(frame2, text=f"{item}\t\t{quantity}\t\t{cost}\t\t{total}", bg="#232323",fg="#ffffff",font="Arial 15")
    item_list.append(single_item)
    single_item_lbl.pack(pady=5)

def clear_item():
    item_text.delete(0,"end")
    quantity_text.delete(0,"end")
    cost_text.delete(0,"end")

def analyse():

    df = pd.DataFrame(item_list)
    items = df["Item"]
    total = df["Total Amount"]
    fig = plt.figure(figsize=(10,5))
    plt.bar(items, total, color='red', width=0.4)
    plt.ylabel("Cost of items")
    plt.xlabel("Items purchase")
    plt.title("Expenditure_Tracker Analyses")
    plt.show()






title_lbl =tk.Label(root,text="Expenditure Tracker", bg="#232323",fg="#ffffff",font="Arial 20")
title_lbl.pack(pady=20)

item_Label=tk.Label(root,text="Item",bg="#232323",fg="#ffffff",font="Arial 15")
item_Label.pack(pady=(20,5))

item_text=tk.Entry(root,font="Arial 15")
item_text.pack()

quantity_Label=tk.Label(root,text="Quantity",bg="#232323",fg="#ffffff",font="Arial 15")
quantity_Label.pack(pady=(20,5))

quantity_text=tk.Entry(root,font="Arial 15")
quantity_text.pack()

cost_Label=tk.Label(root,text="Cost per unit",bg="#232323",fg="#ffffff",font="Arial 15")
cost_Label.pack(pady=(20,5))

cost_text=tk.Entry(root,font="Arial 15")
cost_text.pack()


frame1 = tk.Frame(root,bg="#232323")


add_btn=tk.Button(frame1,text="Add Item", bg="#2a2a2a", fg="#ffffff", font="Arial 15",command=add_item)
add_btn.pack(padx=10, pady=20, side=tk.LEFT)



clear_btn=tk.Button(frame1,text="Clear", bg="#2a2a2a",fg="#ffffff",font="Arial 15",command=clear_item)
clear_btn.pack(side=tk.RIGHT)

frame1.pack()

display_lbl =tk.Label(root,text="Expenses",bg="#232323",fg="#ffffff",font="Arial 15")
display_lbl.pack(pady=(20,5))

frame2= tk.Frame(root,bg="#232323")

heading_lbl=tk.Label(frame2,text="Item\t\tQuantity\t\tUnit Cost\t\tTotal", bg="#232323",fg="#ffffff",font="Arial 15")
heading_lbl.pack(pady=5)


frame2.pack()

analyse_btn = tk.Button(root,text="Analyse",bg="#2a2a2a",fg="#ffffff",font="Arial 15",command=analyse)
analyse_btn.pack(pady=20)





root.mainloop()
