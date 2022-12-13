import tkinter as tk

from login import LoginScreen

if __name__ == '__main__':
    window = tk.Tk()
    window.grid_columnconfigure(2, weight=1) #For debugging the grid purposes only
    login_screen = LoginScreen(window)
    window.mainloop()