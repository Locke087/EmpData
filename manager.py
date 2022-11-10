import tkinter as tk
from tkinter import ttk

class WindowManager():
    def __init__(self, frames: list[tk.Frame]=[]) -> None:
        self.frames = frames
        self.wdx = 0
    def load_frame(self, window_dex):
        '''Loads the next window specified here'''
        self.new_window = tk.Toplevel(self.windows[self.wdx].master)
        self.wdx = window_dex
        self.windows[self.wdx].mainloop()
    def add_window(self, window,):
        self.windows.append(window)
    