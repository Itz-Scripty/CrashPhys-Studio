import tkinter as tk

from ui import CrashPhysUI



class CrashPhysStudio:


    def __init__(self):

        self.window = tk.Tk()

        self.ui = CrashPhysUI(
            self.window
        )



    def run(self):

        self.window.mainloop()