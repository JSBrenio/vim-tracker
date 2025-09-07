from pynput import keyboard
from collections.abc import Callable
import threading

class Logger:
    
    def __init__(self, gui_callback: Callable | None = None, parser_callback: Callable | None = None):
        self.gui_callback = gui_callback
        self.parser_callback = parser_callback
        self.listener = keyboard.Listener(on_press=self.on_press)
    
    def on_press(self, key):
        try:
            key_str = key.char
            event = f"alphanumeric key {key_str} pressed"
        except AttributeError:
            key_str = str(key)
            event = f"special key {key_str} pressed"

        if self.parser_callback:
            self.parser_callback(key_str)
        if self.gui_callback:
            self.gui_callback('press', key_str, event)

    def start(self):
        t = threading.Thread(target=self.listener.start, daemon=True)
        t.start()