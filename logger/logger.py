from pynput import keyboard
from collections.abc import Callable
import threading

class Logger:
    
    def __init__(self, gui_callback: Callable | None = None, parser_callback: Callable | None = None):
        self.gui_callback = gui_callback
        self.parser_callback = parser_callback
        self.listener = keyboard.Listener(on_press=self.on_press)
    
    def on_press(self, key: keyboard.KeyCode | keyboard.Key):
        if not isinstance(key, (keyboard.KeyCode, keyboard.Key)):
            print(type(key).__name__, type(key), repr(key), str(key))
            raise Exception("NOT a supported key stroke")
        
        if isinstance(key, keyboard.KeyCode):
            key_str = key.char
            description = f"alphanumeric key {key_str} pressed"
        elif isinstance(key, keyboard.Key):
            key_str = str(key)
            description = f"special key {key_str} pressed"

        if self.parser_callback:
            self.parser_callback(key_str)
        if self.gui_callback:
            self.gui_callback('press', key_str, description)

    def start(self):
        t = threading.Thread(target=self.listener.start, daemon=True)
        t.start()