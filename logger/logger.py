from pynput import keyboard
from collections.abc import Callable
import threading

class Logger:
    
    def __init__(self, gui_callback: Callable | None = None, parser_callback: Callable | None = None):
        self.gui_callback = gui_callback
        self.parser_callback = parser_callback
        self.pressed_keys = {}
        self.listener = keyboard.Listener(on_press=self.on_press, on_release=self.on_release)
    
    def on_press(self, key: keyboard.KeyCode | keyboard.Key):
        if not isinstance(key, (keyboard.KeyCode, keyboard.Key)):
            print(type(key).__name__, type(key), repr(key), str(key))
            raise Exception(key, "NOT a supported key stroke")
        key_str = ""
        description = "" 
        
        self.pressed_keys[key] = True
        
        if combination := self._check_combinations():
            key_str, description = combination
        elif isinstance(key, keyboard.KeyCode):
            key_str = key.char
            description = f"alphanumeric key {key_str} pressed"
        elif isinstance(key, keyboard.Key):
            key_str = str(key)
            description = f"special key {key_str} pressed"

        if self.parser_callback:
            self.parser_callback(key_str)
        if self.gui_callback:
            self.gui_callback('press', key_str, description)
            
    def on_release(self, key: keyboard.KeyCode | keyboard.Key):
        self.pressed_keys[key] = False
        self.pressed_keys = {key: val for key, val in self.pressed_keys.items() if val}
        
    def _check_combinations(self) -> tuple[str, str] | None:
        # Check if Ctrl is pressed
        ctrl_pressed = self.pressed_keys.get(keyboard.Key.ctrl, True)
        
        if ctrl_pressed:
            # Look for 'c' key (which will be a KeyCode object)
            for key, pressed in self.pressed_keys.items():
                if pressed and isinstance(key, keyboard.KeyCode) and key.char == 'c':
                    return "ctrl+c", "Ctrl+C combination pressed"
                elif pressed and isinstance(key, keyboard.KeyCode) and key.char == 'v':
                    return "ctrl+v", "Ctrl+V combination pressed"
                elif pressed and isinstance(key, keyboard.KeyCode) and key.char == 's':
                    return "ctrl+s", "Ctrl+S combination pressed"
        
        # If no specific combination found
        # pressed_keys = [key for key, val in self.pressed_keys.items() if val]
        # if len(pressed_keys) > 1:
        #     return f"combo: {pressed_keys}", "Combination not specifically handled"
        
        return None

    def start(self):
        t = threading.Thread(target=self.listener.start, daemon=True)
        t.start()