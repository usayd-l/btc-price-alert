import requests
import tkinter as tk
from datetime import datetime


def trackBitcoin():
    url = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
    response = requests.get(url).json()
    price = response["USD"]
    time = datetime.now().strftime("%H:%M")

    labelPrice.config(text = str(price) + " $")
    labelTime.config(text= "Updated at: " + time)
    labelName.config(text= "@Username here")
    
    canvas.after(1000, trackBitcoin)


canvas = tk.Tk()
canvas.geometry("400x500")
canvas.title("btcalert")

f1 = ("poppins", 35, "bold")
f2 = ("poppins", 24, "bold")
f3 = ("poppins", 18, "normal")
f4 = ("poppins", 10, "normal")


label = tk.Label(canvas, text = "Bitcoin Price", font = f1)
label.pack(pady = 20)

labelPrice = tk.Label(canvas, font = f2)
labelPrice.pack(pady = 20)

labelTime = tk.Label(canvas, font = f3)
labelTime.pack(pady = 20)

labelName = tk.Label(canvas, font = f4)
labelName.pack(pady = 20)

trackBitcoin()

canvas.mainloop()