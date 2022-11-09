import tkinter as tk
from tkinter import ttk
from manager import WindowManager
from login import LoginScreen

window_manager = WindowManager()
login_screen = LoginScreen(window_manager)

window_manager.add_window(login_screen)
window_manager.load_window(0)