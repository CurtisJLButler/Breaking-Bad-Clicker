import tkinter as tk
import os

root = tk.Tk()
frame = tk.Frame(root)
dir = str(os.getcwd())
root.geometry("1000x1000")
# creating the tkinter window


# variables
dollarsPerGram = 20
totalMeth = 0
gramsPerBatch = 1
money = 0
timesSold = 0
amountSell = 1

def make():
	global totalMeth
	totalMeth += gramsPerBatch
	methAmount.config(text = "Grams of meth: " + str(totalMeth))
	return totalMeth
def biggerContainers():
	global gramsPerBatch
	global money
	if int(money) > 60 or money == 60:
		gramsPerBatch += 1
		money -= 60
		cash.config(text = "Money: " + str(money))
		batchAmount.config(text = "Grams per batch: " + str(gramsPerBatch))
		return gramsPerBatch, money
def sellMeth():
	global totalMeth, money, timesSold, amountSell
	if totalMeth < 1:
		print("not enough meth")
	else:
		totalMeth -= amountSell
		money += amountSell * dollarsPerGram
		cash.config(text = "Money: " + str(money))
		methAmount.config(text = "Grams of meth: " + str(totalMeth))
		if timesSold < 9:
			timesSold += 1
		elif timesSold == 9:
			timesSold = 0
			amountSell += 1




# create a Label widget
cash = tk.Label(text = "Money: 0")
cash.pack()


methAmount = tk.Label(text = "Grams of meth: 0")
methAmount.pack()

batchAmount = tk.Label(text = "Grams of meth per batch: 1")
batchAmount.pack()

ww = tk.PhotoImage(file = dir + "\Pictures\ww.png")
makeMeth = tk.Button(text = "More crystal jesse", image = ww, command = make)
makeMeth.pack(anchor="nw")

JP = tk.PhotoImage(file = dir + "\Pictures\JP.png")
containers = tk.Button(text = "Bigger Containers jesse", image = JP, command = biggerContainers)
containers.pack(anchor="ne")

gus = tk.PhotoImage(file = dir + "\Pictures\gus.png")
sell = tk.Button(text = "Sell meth", image = gus, command = sellMeth)
sell.pack(anchor="sw")

frame.pack(padx = 5, pady = 5)
root.mainloop()