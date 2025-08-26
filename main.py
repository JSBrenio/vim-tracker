import vim_parser
import logger
import ui

def main():
    print("Starting Vim Tracker...")
    
    # Initialize parser
    vim_parser.initialize()
    
    # Setup callback connection:
    def setup_logger_callback(ui_callback):
        logger.start_logging(ui_callback)

    # Start UI last (blocking call)
    ui.start_ui(setup_logger_callback)

if __name__ == "__main__":
    main()