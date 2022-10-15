import tkinter as tk
from PIL import ImageTk, Image
import os
tk.PhotoImage = os.getcwd()
 
root = tk.Tk()
frame = tk.Frame(root)

# creating the tkinter window


# variables
dollarsPerGram = 20
totalMeth = 0
gramsPerBatch = 1
methSaleAmount = 1
money = 0

def make():
	global totalMeth
	totalMeth += gramsPerBatch
	methAmount.config(text = totalMeth)
	return totalMeth
def biggerContainers():
	global gramsPerBatch
	gramsPerBatch += 1
	return gramsPerBatch
def sellMeth():
	global totalMeth, money
	if totalMeth < 1:
		print("not enough meth")
	else:
		totalMeth -= methSaleAmount
		money += methSaleAmount * dollarsPerGram
		cash.config(text = money)
		methAmount.config(text = totalMeth)



# create a Label widget
cash = tk.Label(text = 0)
cash.pack()


methAmount = tk.Label(text = 0)
methAmount.pack()

ww = tk.PhotoImage(file = "os.path.realpath(os.path.join(os.path.dirname(__file__), "Pictures", ww.png"))")
makeMeth = tk.Button(text = "More crystal jesse", image = ww, command = make)
makeMeth.pack()


containers = tk.Button(text = "Bigger Containers jesse", command = biggerContainers)
containers.pack()

gus = tk.PhotoImage(file = r"\Pictures\gus.png")
sell = tk.Button(text = "Sell meth", image = gus, command = sellMeth)
sell.pack()


frame.pack(padx = 5, pady = 5)
root.mainloop()