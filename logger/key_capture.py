from pynput import keyboard

"""snippet code from official pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html"""

def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))

def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# ...or, in a non-blocking fashion:
# A keyboard listener is a threading.Thread, and all callbacks will be invoked from the thread.
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)