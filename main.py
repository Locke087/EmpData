import tkinter as tk
from tkinter import ttk

from login import LoginScreen

if __name__ == '__main__':
    window = tk.Tk()
    login_screen = LoginScreen(window)
    window.mainloop()