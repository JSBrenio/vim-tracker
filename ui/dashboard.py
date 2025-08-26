import tkinter as tk
from tkinter import scrolledtext

class Dashboard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Vim Tracker Dashboard")
        self.setup_ui()
        
    def setup_ui(self):
        # Title
        title = tk.Label(self.root, text="Vim Tracker Dashboard", font=('Arial', 16, 'bold'))
        title.pack(pady=10)
        
        # Key log display
        log_label = tk.Label(self.root, text="Key Log:")
        log_label.pack(anchor='w', padx=20)
        
        self.log_text = scrolledtext.ScrolledText(self.root, width=60, height=20)
        self.log_text.pack(padx=20, pady=10)
        
    def on_key_event(self, event_type, key, description):
        """Callback function to receive key events from logger"""
        # This needs to be thread-safe since it's called from the key listener thread
        self.root.after(0, lambda: self._update_log(event_type, key, description))
        
    def _update_log(self, event_type, key, description):
        """Update the log display (runs on main thread)"""
        self.log_text.insert(tk.END, f"{description}\n")
        self.log_text.see(tk.END)  # Auto-scroll to bottom
        
    def run(self):
        """Start the GUI main loop"""
        self.root.mainloop()

def launch(key_callback=None):
    dashboard = Dashboard()
    if key_callback:
        key_callback(dashboard.on_key_event)
    dashboard.run()