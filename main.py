import vim_parser
import logger
import ui

def main():
    print("Starting Vim Tracker...")
    
    # Initialize parser
    vim_parser.initialize()
    
    # Start logging first (non-blocking)
    logger.start_logging()
    
    # Start UI last (blocking call)
    ui.start_ui()

if __name__ == "__main__":
    main()