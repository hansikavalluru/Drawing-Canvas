from tkinter import *
from tkinter.colorchooser import askcolor

win = Tk()
win.geometry('400x430')
win.title('Drawing Pad')

# Canvas for drawing
canvas = Canvas(win, bg='white', width=400, height=380)
canvas.grid(row=1, column=0, columnspan=3)

# Drawing state
current_color = 'black'
brush_size = 5
drawing_mode = 'draw'

def start_draw(event):
    canvas.old_x = event.x
    canvas.old_y = event.y

def draw(event):
    if canvas.old_x and canvas.old_y:
        color = 'white' if drawing_mode == 'erase' else current_color
        canvas.create_oval(
            event.x - brush_size, event.y - brush_size,
            event.x + brush_size, event.y + brush_size,
            fill=color, outline=color
        )
    canvas.old_x = event.x
    canvas.old_y = event.y

def reset(event):
    canvas.old_x = None
    canvas.old_y = None

# Mouse events
canvas.bind('<Button-1>', start_draw)
canvas.bind('<B1-Motion>', draw)
canvas.bind('<ButtonRelease-1>', reset)

def choose_color():
    global current_color, drawing_mode
    drawing_mode = 'draw'
    color = askcolor()[1]
    if color:
        current_color = color

def use_eraser():
    global drawing_mode
    drawing_mode = 'erase'

def clear_canvas():
    canvas.delete('all')

# Buttons
b1 = Button(win, text='Eraser', command=use_eraser)
b1.grid(row=0, column=0)

b2 = Button(win, text='Color', command=choose_color)
b2.grid(row=0, column=1)

b3 = Button(win, text='Clear', command=clear_canvas)
b3.grid(row=0, column=2)

win.mainloop()