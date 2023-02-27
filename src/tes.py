import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class GUI:
    def __init__(self, master):
        self.master = master
        master.title("Matplotlib Popup")

        # Create button to open Matplotlib popup
        self.button = ttk.Button(master, text="Open Matplotlib Popup", command=self.plot)
        self.button.pack()

    def plot(self):
        # Create Matplotlib figure and canvas
        fig = plt.figure()
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas.draw()

        # Create Matplotlib popup window
        popup_window = tk.Toplevel(self.master)
        popup_window.title("Matplotlib Popup")
        popup_window.geometry("800x600")

        # Add Matplotlib canvas to popup window
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Create GUI window
root = tk.Tk()
gui = GUI(root)
root.mainloop()
