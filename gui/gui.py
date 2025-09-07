import tkinter as tk
from tkinter import scrolledtext

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vim Tracker GUI")
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Vim Tracker GUI", font=('Arial', 16, 'bold'))
        title.pack(pady=10)
        
        # Key log display
        log_label = tk.Label(self.root, text="Raw Key Log:")
        log_label.pack(anchor='w', padx=20)
        
        self.key_log = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.key_log.pack(padx=20, pady=5)
        
        # Command log display
        cmd_label = tk.Label(self.root, text="Vim Commands:")
        cmd_label.pack(anchor='w', padx=20)
        
        self.cmd_log = scrolledtext.ScrolledText(self.root, width=60, height=10)
        self.cmd_log.pack(padx=20, pady=5)
        
    def on_key_event(self, event_type, key, description):
        """Callback function to receive events from logger"""
        self.root.after(0, lambda: self._update_display(event_type, key, description))
        
    def _update_display(self, event_type, key, description):
        """Update the appropriate display (thread-safe)"""
        # print(key)
        if event_type == 'command':
            self.cmd_log.insert(tk.END, f"{description}\n")
            self.cmd_log.see(tk.END)
        else:
            # Handle raw key events (press/release)
            self.key_log.insert(tk.END, f"{description}\n")
            self.key_log.see(tk.END)
        
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()