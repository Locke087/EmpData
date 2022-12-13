import tkinter as tk

class HoverButton(tk.Frame):
    def __init__(self,btn_txt,hov_txt, cmd, *args,font=('Arial', 25), background='#007385', **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self['bg'] = background
        self.hov_txt = hov_txt
        self.l1 = tk.Button(self, text=btn_txt, command=cmd,font=font, background=background)
        self.l2 = tk.Label(self, text="", width=40, background=background)
        self.l1.pack(side="top")
        self.l2.pack(side=tk.RIGHT, fill=tk.X)

        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self.l2.configure(text=self.hov_txt)
        self.l2.config(bg='#8a8d00')

    def on_leave(self, e):
        self.l2.configure(text="")
        self.l2.configure(background=self.l1['bg'])

def nothing():
    print("Running")
if __name__ == "__main__":
    root = tk.Tk()
    HoverButton("Clicke me!!",nothing, root).grid()
    root.mainloop()