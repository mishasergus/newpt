import tkinter as tk


window = tk.Tk()
window.title("Kalculator")

entry = tk.Entry(window,width = 30, font = ("Times New Roman",14))
entry.grid(row = 0,column = 0,columnspan = 4,padx = 10,pady = 10)

buttons = [
    ("7",1,0),("8",1,1),("9",1,2),("/",1,3),
    ("4",2,0),("5",2,1),("6",2,2),("*",2,3),
    ("1",3,0),("2",3,1),("3",3,2),("-",3,3),
    ("0",4,0),(".",4,1),("=",4,2),("+",4,3),
    ("C",5,0)
]

def defoultButton(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + str(symbol))
def calculate():
    try:
        userText = eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,str(userText))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "ERROR")
def clear():
    entry.delete(0, tk.END)

for (text,row,collumn) in buttons:
    if text == "=":
        button = tk.Button(window,text = text,width = 5,height= 5,font = ("Times New Roman",12),command = calculate)
    elif text == "C":
        button = tk.Button(window,text = text,width = 5,height= 5,font = ("Times New Roman",12),command = clear)
    else:
        button = tk.Button(window,text = text, width=5, height=5, font=("Times New Roman", 12), command=lambda x = text:defoultButton(x))
    button.grid(row = row, column = collumn,padx = 5,pady = 5)


window.mainloop()