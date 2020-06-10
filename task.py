import tkinter
import tkinter.messagebox
win = tkinter.Tk()
win.title("ApP")
win.resizable(1,1)

def ee():
    win.destroy()

def item():
    for i, lss in enumerate(ls.get(0, tkinter.END)):
        if itemm.get() in lss:
            tkinter.messagebox.showerror("Message","Item already in the list")
    else:
            
            ls.insert(tkinter.END,"{} ${}".format(itemm.get(),str(prc.get())))

t1=tkinter.Label(win,text="Item Name",fg="green")
t1.pack()

ld1 = tkinter.LabelFrame(win,font=("monospace", 15, "italic"))
ld1.pack(fill="x")

itemm = tkinter.StringVar()
e1=tkinter.Entry(ld1,textvariable=itemm)
e1.pack(fill="x",ipady=10)

t2=tkinter.Label(ld1,text="Item price",fg="green")
t2.pack()

ld2 = tkinter.LabelFrame(ld1,font=("monospace", 15, "italic"))
ld2.pack(fill="x")

prc = tkinter.IntVar()
e2=tkinter.Entry(ld2,textvariable=prc)
e2.pack(fill="x",ipady=10)

btn = tkinter.Button(ld2,text="Add Item",bg="green",fg="white",command=item)
btn.pack()

lb=tkinter.Label(ld2,text="All Items",font=("monospace", 11))
lb.pack()

ls=tkinter.Listbox(ld2)
ls.config(bg="yellow")
ls.pack(fill="x")

bt1=tkinter.Button(ld2,text="Exit",bg="red",command=ee)
bt1.pack(fill="x")


win.geometry("720x520")
win.mainloop()
