import vim_parser
import logger
import gui

def main():
    print("Starting Vim Tracker...")
    
    # Initialize parser
    vim_parser.initialize()
    
    # Setup callback connection
    def setup_logger_callback(ui_callback):
        # Store the UI callback first
        logger._ui_callback = ui_callback
        
        # Now attach vim parser to logger (it can access the UI callback)
        parsing_callback = vim_parser.attach_to_logger(logger)
        
        # Set the parsing callback and start listener
        logger.set_key_callback(parsing_callback)
        logger.key_capture.listener.start()
    
    # Start UI (which will start logging with vim parsing)
    print("Initializing GUI")
    gui.start_gui(setup_logger_callback)

if __name__ == "__main__":
    main()