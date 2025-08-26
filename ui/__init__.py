from . import dashboard

def start_ui(setup_callback=None):
    """Start the dashboard UI with optional setup callback"""
    dashboard.launch(setup_callback)