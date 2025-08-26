from . import key_capture

def start_logging(callback=None):
    """Start the key capture listener"""
    if callback:
        key_capture.set_callback(callback)
    key_capture.listener.start()

def stop_logging():
    """Stop the key capture listener"""
    key_capture.listener.stop()