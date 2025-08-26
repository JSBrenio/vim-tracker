from pynput import keyboard

# Global callback for key events
_key_callback = None

def set_callback(callback_func):
    """Set the callback function to receive key events"""
    global _key_callback
    _key_callback = callback_func

def on_press(key):
    try:
        key_str = key.char
        event = f"alphanumeric key {key_str} pressed"
    except AttributeError:
        key_str = str(key)
        event = f"special key {key_str} pressed"
    
    # Send to callback if set
    if _key_callback:
        _key_callback('press', key_str, event)

# ...or, in a non-blocking fashion:
# A keyboard listener is a threading.Thread, and all callbacks will be invoked from the thread.
listener = keyboard.Listener(
    on_press=on_press)
