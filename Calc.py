import tkinter as tk
import tkinter.messagebox

def add():
    try:
        z.set((x.get() + y.get()))
    except Exception as e:
        tkinter.messagebox.showwarning('Error', e)
root = tk.Tk()
x = tk.IntVar(0)
y = tk.IntVar(0)
z = tk.IntVar(0)
e1 = tk.Entry(root, textvariable=y)
e1.grid(row=0, column=0)
e2 = tk.Entry(root, textvariable=x)
e2.grid(row=1, column=0 )
b1 = tk.Button(root, text='add', command=add)
b1.grid(row=0, column=1)
res = tk.Label(root, textvariable=z)
res.grid(row=1, column=1)


root.mainloop()
