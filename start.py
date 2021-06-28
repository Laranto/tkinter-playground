import tkinter

from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure

import numpy as np

root = tkinter.Tk()
root.wm_title("Embedding in Tk")


fig1 = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig1.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

fig2 = Figure(figsize=(5, 4), dpi=100)
fig2.add_subplot(111).plot(t, 2 * np.tan(2 * np.pi * t))

canvas = FigureCanvasTkAgg(fig1, master=root)  # A tk.DrawingArea.
canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
canvas.draw_idle()

# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.update()
# canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)


def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)


canvas.mpl_connect("key_press_event", on_key_press)

def update(param):
    global canvas
    canvas.get_tk_widget().pack_forget()
    canvas = FigureCanvasTkAgg(fig2, master=root)  # A tk.DrawingArea.
    canvas.get_tk_widget().pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=1)
    canvas.draw_idle()

def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate

buttonFrame = tkinter.Frame(master=root)
buttonFrame.pack(side=tkinter.LEFT)

functionButtons = []
functionButtons.append(tkinter.Button(master=buttonFrame, text="Update", command= lambda: update(1)))
functionButtons.append(tkinter.Button(master=buttonFrame, text="Quit", command=_quit))

for i,button in enumerate(functionButtons):
    button.grid(column=0, row=i,sticky="ew")

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.