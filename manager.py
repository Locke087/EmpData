import tkinter as tk
from tkinter import ttk

class WindowManager():
    def __init__(self, windows: list[tk.Tk]=[]) -> None:
        self.windows = windows
        self.wdx = 0
    def load_window(self, window_dex):
        '''Loads the next window specified here'''
        self.windows[self.wdx].quit()
        self.wdx = window_dex
        self.windows[self.wdx].mainloop()
    def add_window(self, window):
        self.windows.append(window)
    