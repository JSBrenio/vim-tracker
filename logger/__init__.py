from . import key_capture

def start_logging():
    """Start the key capture listener"""
    key_capture.listener.start()

def stop_logging():
    """Stop the key capture listener"""
    key_capture.listener.stop()