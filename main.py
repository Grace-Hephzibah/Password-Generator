# These are external libraries
import tkinter as tk
from tkinter import ttk

# These are self created code imports
from windows import set_dpi_awareness
import StrongPassword as SP
import reply as r
import color as c

set_dpi_awareness()

Refresh = "Click Refresh"
Password = Refresh

root = tk.Tk()
root.geometry("500x300")
root.resizable(False, False)
root.title("PWD Gen")
root.configure(bg='#34c3eb')

label = ttk.Label(root, text = Password, padding = 20, background = "#34c3eb", foreground = "white")
label.config(font = ("Segoe UI", 20))
label.pack()
    
def refresh():
    Password = SP.PWD()
    label["text"] = Password
    confirmation["text"] = r.reply()
    refresh_button["bg"] = "white"
    root.clipboard_clear()
    root.clipboard_append(Password)
    
    LightColorChoice = c.color_light()
    refresh_button["bg"] = LightColorChoice

    DarkColorChoice = c.color_dark()
    
    if LightColorChoice == DarkColorChoice:
        DarkColorChoice = "#a62d92"
    root["bg"] = DarkColorChoice
    confirmation["background"] = DarkColorChoice
    label["background"] = DarkColorChoice
    

buttons = ttk.Frame(root)
buttons.pack()

refresh_button = tk.Button(buttons, text = "Refresh", command = refresh, bg = "#eb3477", fg = "black", height = 2, width = 15)
refresh_button.pack(side = "left", fill = "x", expand = True)

confirmation = ttk.Label(root, padding = 20, background = "#34c3eb", foreground = "white", text = Refresh)
confirmation.config(font = ("Segoe UI", 20))
confirmation.pack()

root.mainloop()
