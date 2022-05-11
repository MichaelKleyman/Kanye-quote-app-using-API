from tkinter import *
import requests

def say_quote():
    quotes = requests.get(url="https://api.kanye.rest")
    quotes.raise_for_status()
    quote = quotes.json()
    canvas.itemconfig(quote_text, text=quote['quote'])

window = Tk()
window.title("Kanye Says...")
window.config(padx=50,pady=50, background="white")

canvas = Canvas(width=300, height=414, highlightthickness=0, bg="white")
img = PhotoImage(file="kanye-quotes-start/background.png")
canvas.create_image(150, 207, image=img)
quote_text = canvas.create_text(150, 207, text="Kanye quote", width=250, fill="white", font=("Arial", 30, "bold"))
canvas.pack()

kanye_img = PhotoImage(file="kanye-quotes-start/kanye.png")
kanye_button = Button(highlightthickness=0, image=kanye_img, borderwidth=0, background="white", command=say_quote)
kanye_button.pack()

window.mainloop()