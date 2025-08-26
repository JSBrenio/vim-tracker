from . import parser, grammer
from .parser import VimParser

# Global parser instance
_parser_instance = None

def initialize():
    """Initialize the vim parser components"""
    global _parser_instance
    _parser_instance = VimParser()
    print("vim_parser initialized")

def attach_to_logger(logger_module):
    """Attach vim parser to logger for real-time parsing"""
    global _parser_instance
    if _parser_instance is None:
        initialize()
    
    def vim_parsing_callback(event_type, key, description):
        # Get the current UI callback from logger
        ui_callback = getattr(logger_module, '_ui_callback', None)
        
        # Process through vim parser if it's a key press
        if event_type == 'press' and len(key) == 1:
            command = _parser_instance.feed(key)
            if command:
                # Send parsed command to UI
                if ui_callback:
                    ui_callback('command', str(command), f"Vim Command: {command}")
        
        # Always send raw key events too
        if ui_callback:
            ui_callback(event_type, key, description)
    
    # Return the callback function for logger to use
    return vim_parsing_callback

def get_parser():
    """Get the global parser instance"""
    global _parser_instance
    if _parser_instance is None:
        initialize()
    return _parser_instance