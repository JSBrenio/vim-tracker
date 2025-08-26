from . import key_capture

# Global callback for UI updates
_ui_callback = None

def start_logging(ui_callback=None):
    """Start the key capture listener"""
    global _ui_callback
    _ui_callback = ui_callback
    
    # Set up key capture callback
    key_capture.set_callback(_on_key_event)
    key_capture.listener.start()

def _on_key_event(event_type, key, description):
    """Process raw key events"""
    if _ui_callback:
        _ui_callback(event_type, key, description)

def stop_logging():
    """Stop the key capture listener"""
    key_capture.listener.stop()

def set_key_callback(callback):
    """Allow external modules to override the key processing callback"""
    key_capture.set_callback(callback)