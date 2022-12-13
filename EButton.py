import tkinter as tk
from idlelib.tooltip import Hovertip
    
app = tk.Tk()
myBtn = tk.Button(app,text='?')
myBtn.pack(pady=30)
myTip = Hovertip(myBtn,'This is \na multiline tooltip.')
app.mainloop()