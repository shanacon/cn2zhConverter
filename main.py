import imp
import tkinter as tk
import tkinter.font as font
from MainPanel import *

window = tk.Tk()
##      font
BtnFont = font.Font(size=20)
EntryFont = font.Font(size=14)

###     main Panel
mainpanel = MainPanel(window, BtnFont, EntryFont)

window.title('zhConverter')
window.geometry("1000x400+500+300")
window.mainloop()