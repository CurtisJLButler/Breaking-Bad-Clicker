import tkinter as tk
import os

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

ww = tk.PhotoImage(file = str(os.getcwd()) + "\Pictures\WW.png")
makeMeth = tk.Button(text = "More crystal jesse", image = ww, command = make)
makeMeth.pack(padx=5, pady=5)


containers = tk.Button(text = "Bigger Containers jesse", command = biggerContainers)
containers.pack(padx=5, pady=5)

gus = tk.PhotoImage(file = str(os.getcwd()) + "\Pictures\gus.png")
sell = tk.Button(text = "Sell meth", image = gus, command = sellMeth)
sell.pack(padx=5, pady=5)


frame.pack(padx = 5, pady = 5)
root.mainloop()