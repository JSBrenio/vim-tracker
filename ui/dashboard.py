import tkinter as tk

def launch():
    root = tk.Tk()
    root.title("Logger")
    lbl = tk.Label(root, text="Vim Tracker Dashboard")
    lbl.pack(padx=20, pady=20)
    root.mainloop()
    
if __name__ == "__main__":
    launch()