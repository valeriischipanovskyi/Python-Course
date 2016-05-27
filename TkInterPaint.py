import tkinter as tk

x = y = None
def draw(e):
    global x, y
    if x and y:
        c.create_line(x, y, e.x, e.y)
    x, y = e.x, e.y

def release(e):
    global x, y
    x = y = None


root = tk.Tk()
root.geometry('600x400')
c = tk.Canvas(root)
c.pack(fill=tk.BOTH, expand=1)
c.bind('<B1-Motion>', draw)
c.bind('<ButtonRelease-1>', release)

root.mainloop()
