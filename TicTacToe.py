from tkinter import *

root=Tk()
root.geometry("500x500")
root.title("Calculator")
turn = IntVar()
turn.set(1)
Winner = StringVar()
Winner.set("none")

def playerTurn(event):
    btn = event.widget
    if btn["text"] == "" and Winner.get()=="none":
        if int(turn.get()) % 2 == 1:
            btn["text"]="X"
        else:
            btn["text"]="O"
        turn.set(turn.get()+1)
        if turn.get() == 10 and Winner.get() == "none":
            print(turn.get())
            lblWinner = Label(text="Draw", font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
    if btn1["text"] != "":
        if btn1["text"] == btn2["text"] and btn2["text"] == btn3["text"]:
            lblWinner = Label(text=(btn1["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn1["text"])
        if btn1["text"] == btn4["text"] and btn4["text"] == btn7["text"]:
            lblWinner = Label(text=(btn1["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn1["text"])
        if btn1["text"] == btn5["text"] and btn5["text"] == btn9["text"]:
            lblWinner = Label(text=(btn1["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn1["text"])
    if btn2["text"] != "":
        if btn2["text"] == btn5["text"] and btn5["text"] == btn8["text"]:
            lblWinner = Label(text=(btn2["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn2["text"])
    if btn3["text"] != "":
        if btn3["text"] == btn6["text"] and btn6["text"] == btn9["text"]:
            lblWinner = Label(text=(btn3["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn3["text"])
        if btn3["text"] == btn5["text"] and btn5["text"] == btn7["text"]:
            lblWinner = Label(text=(btn3["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn3["text"])
    if btn4["text"] != "":
        if btn4["text"] == btn5["text"] and btn5["text"] == btn6["text"]:
            lblWinner = Label(text=(btn4["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn4["text"])
    if btn7["text"] != "":
        if btn7["text"] == btn8["text"] and btn8["text"] == btn9["text"]:
            lblWinner = Label(text=(btn7["text"]+" wins"), font=("ARIEL", 20))
            lblWinner.grid(row=3, column=0, columnspan=3)
            Winner.set(btn7["text"])
    


btn1 = Button(text="", height=4, width=5)
btn1.grid(row=0, column=0)
btn1.bind("<Button-1>", playerTurn)

btn2 = Button(text="", height=4, width=5)
btn2.grid(row=0, column=1)
btn2.bind("<Button-1>", playerTurn)

btn3 = Button(text="", height=4, width=5)
btn3.grid(row=0, column=2)
btn3.bind("<Button-1>", playerTurn)

btn4 = Button(text="", height=4, width=5)
btn4.grid(row=1, column=0)
btn4.bind("<Button-1>", playerTurn)

btn5 = Button(text="", height=4, width=5)
btn5.grid(row=1, column=1)
btn5.bind("<Button-1>", playerTurn)

btn6 = Button(text="", height=4, width=5)
btn6.grid(row=1, column=2)
btn6.bind("<Button-1>", playerTurn)

btn7 = Button(text="", height=4, width=5)
btn7.grid(row=2, column=0)
btn7.bind("<Button-1>", playerTurn)

btn8 = Button(text="", height=4, width=5)
btn8.grid(row=2, column=1)
btn8.bind("<Button-1>", playerTurn)

btn9 = Button(text="", height=4, width=5)
btn9.grid(row=2, column=2)
btn9.bind("<Button-1>", playerTurn)

root.mainloop()