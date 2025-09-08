from vim_parser import VimParser
from logger import Logger
from gui import GUI

def main():
    print("Starting Vim Tracker...")
    
    gui = GUI()
    parser = VimParser(gui_callback=gui.on_key_event) # parser pushes to GUI
    logger = Logger(
        gui_callback=gui.on_key_event, # logger pushes to GUI
        parser_callback=parser.feed) # logger pushes to parser

    # threaded
    logger.start()

    # blocking
    gui.run()
    
if __name__ == "__main__":
    main()