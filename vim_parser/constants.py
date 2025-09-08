# Single-key operators that need a motion/text object
BASIC_OPERATORS = {
    "d": "delete",
    "y": "yank",
    "c": "change",
    ">": "indent",
    "<": "outdent",
    "=": "format",
    "!": "filter through external command"
}

# G-prefixed operators (after pressing 'g')
G_OPERATORS = {
    "~": "toggle case",
    "u": "lowercase",
    "U": "uppercase",
    "d": "go to definition",
    "q": "format text",
    "h": "show hover tooltip",
    "c": "toggle line comment",
    "C": "toggle block comment",
    "f": "go to file under cursor"
}

# Z-prefixed operators (after pressing 'z')
Z_OPERATORS = {
    "f": "create fold",
    "o": "open fold",
    "c": "close fold",
    "d": "delete fold",
    "R": "open all folds",
    "M": "close all folds",
    "z": "center cursor line",
    "t": "cursor line to top",
    "b": "cursor line to bottom"
}

# Basic motions (single keystroke)
BASIC_MOTIONS = {
    # Word navigation
    "w": "word forward",
    "W": "WORD forward",
    "e": "end of word",
    "E": "end of WORD",
    "b": "word backward",
    "B": "WORD backward",
    
    # Single movements
    "h": "left",
    "j": "down",
    "k": "up",
    "l": "right",
    
    "p": "paste after cursor",
    "P": "paste before cursor",
    
    # Line navigation
    "0": "line start",
    "^": "first non-blank character",
    "$": "line end",
    "+": "first character of next line",
    "-": "first character of previous line",
    "_": "first non-blank of current line",
    
    ";": "repeat last f, F, t, T",
    ",": "repeat last f, F, t, T in opposite direction",
    
    # File navigation (single key)
    "{": "paragraph backward",
    "}": "paragraph forward",
    "H": "top of visible window",
    "M": "middle of visible window",
    "L": "bottom of visible window",
    "G": "buffer end",
    
    # Search navigation (mode changers)
    "/": "search forward",
    "?": "search backward",
    "*": "search word under cursor forward",
    "#": "search word under cursor backward",
    "n": "repeat search",
    "N": "repeat search in opposite direction"
}

# Character navigation requiring a second character
SEARCH_CHARACTER_MOTIONS = {
    "f": "find character forward",
    "F": "find character backward",
    "t": "till character forward",
    "T": "till character backward",
}

# G-prefixed motions (after pressing 'g')
G_MOTIONS = {
    "g": "buffer start",  # gg
    "e": "end of previous word",
    "E": "end of previous WORD",
    "j": "move cursor down across wrapped line",
    "k": "move cursor up across wrapped line",
    ";": "go to last edit location"
}

# Control key commands
CTRL_COMMANDS = {
    "o": "go to older position",
    "i": "go to newer position",
    "f": "scroll forward full screen",
    "b": "scroll backward full screen",
    "d": "scroll down half screen",
    "u": "scroll up half screen",
    "e": "scroll down one line",
    "y": "scroll up one line"
}

# Commands that need two identical keystrokes
DOUBLE_KEY_COMMANDS = {
    "'": "jump to last position",  # ''
    "`": "jump to position of last change",  # ``
    "g": "buffer start"  # gg
}

# Text object prefixes
TEXT_OBJECT_PREFIXES = {
    "i": "inner", 
    "a": "around"
}

# Text object targets (after prefix i or a)
TEXT_OBJECT_TARGETS = {
    # Word/block objects
    "w": "word",
    "W": "WORD",
    "s": "sentence",
    "p": "paragraph",
    
    # Quotes and brackets
    "\"": "double quotes",
    "'": "single quotes",
    "`": "backticks",
    "(": "parentheses",
    ")": "parentheses",
    "[": "square brackets",
    "]": "square brackets",
    "{": "curly braces",
    "}": "curly braces",
    "<": "angle brackets",
    ">": "angle brackets",
    "t": "XML/HTML tag",
    
    # VSCode specific
    "i": "indentation level (excluding empty lines)",
    "f": "function (VSCodeVim extension)"
}

# Vim Modes (values represent the state in the FSM)
VIM_MODES = {
    "NORMAL": "Normal mode",
    "INSERT": "Insert mode", 
    "VISUAL": "Visual mode",
    "VISUAL_LINE": "Visual Line mode",
    "VISUAL_BLOCK": "Visual Block mode",
    "COMMAND": "Command mode",
    "REPLACE": "Replace mode",
    "TERMINAL": "Terminal mode"
}

# Mode change keys (keys that trigger mode transitions)
MODE_KEYS = {
    "i": "INSERT",       # Normal -> Insert
    "I": "INSERT",       # Normal -> Insert at line start
    "a": "INSERT",       # Normal -> Insert after cursor
    "A": "INSERT",       # Normal -> Insert at end of line
    "v": "VISUAL",       # Normal -> Visual
    "V": "VISUAL_LINE",  # Normal -> Visual Line
    "Ctrl+v": "VISUAL_BLOCK",  # Normal -> Visual Block
    ":": "COMMAND",      # Normal -> Command
    "r": "REPLACE",      # Normal -> Replace (single character)
    "R": "REPLACE",      # Normal -> Replace mode
    "Ctrl+c": "NORMAL",  # Any -> Normal
}

# Command mode commands (after : prefix)
COMMAND_COMMANDS = {
    "w": "save",
    "q": "close editor",
    "wq": "save and close",
    "e": "open file"
}

# Special keys that need specific handling
SPECIAL_KEYS = {
    "Escape": "exit current mode",
    "Enter": "confirm/execute",
    "Backspace": "delete previous character",
    "Delete": "delete character at cursor",
    "Tab": "indent in visual mode",
    "Shift+Tab": "outdent in visual mode"
}

# Register categories (for FSM)
REGISTER_PREFIXES = {
    "\"": "register selection",
    "@": "macro execution"
}

# Register values (after " prefix)
REGISTER_NAMES = {
    # Number registers
    "0": "last yanked text",
    "1": "first historical delete",
    "2": "second historical delete",
    "3": "third historical delete",
    "4": "fourth historical delete",
    "5": "fifth historical delete",
    "6": "sixth historical delete",
    "7": "seventh historical delete",
    "8": "eighth historical delete",
    "9": "ninth historical delete",
    
    # Named registers
    "a": "named register a",
    "b": "named register b",
    "c": "named register c",
    "d": "named register d",
    "e": "named register e",
    "f": "named register f",
    "g": "named register g",
    "h": "named register h",
    "i": "named register i",
    "j": "named register j",
    "k": "named register k",
    "l": "named register l",
    "m": "named register m",
    "n": "named register n",
    "o": "named register o",
    "p": "named register p",
    "q": "named register q",
    "r": "named register r",
    "s": "named register s",
    "t": "named register t",
    "u": "named register u",
    "v": "named register v",
    "w": "named register w",
    "x": "named register x",
    "y": "named register y",
    "z": "named register z",
    
    # Special registers
    "+": "system clipboard",
    "*": "selection clipboard",
    "_": "black hole register",
    "%": "current file name",
    "#": "alternate file name",
    ".": "last inserted text",
    ":": "last command-line",
    "/": "last search pattern"
}

# Mark prefix
MARK_PREFIX = {
    "m": "set mark",
    "'": "go to mark line",
    "`": "go to mark position"
}

# Mark names (after m/' prefix)
MARK_NAMES = {
    # Lowercase marks (buffer local)
    "a": "mark a",
    "b": "mark b",
    "c": "mark c",
    "d": "mark d",
    "e": "mark e",
    "f": "mark f",
    "g": "mark g",
    "h": "mark h",
    "i": "mark i",
    "j": "mark j",
    "k": "mark k",
    "l": "mark l",
    "m": "mark m",
    "n": "mark n",
    "o": "mark o",
    "p": "mark p",
    "q": "mark q",
    "r": "mark r",
    "s": "mark s",
    "t": "mark t",
    "u": "mark u",
    "v": "mark v",
    "w": "mark w",
    "x": "mark x",
    "y": "mark y",
    "z": "mark z",
    
    # Uppercase marks (global)
    "A": "global mark A",
    "B": "global mark B",
    "C": "global mark C",
    "D": "global mark D",
    "E": "global mark E",
    "F": "global mark F",
    "G": "global mark G",
    "H": "global mark H",
    "I": "global mark I",
    "J": "global mark J",
    "K": "global mark K",
    "L": "global mark L",
    "M": "global mark M",
    "N": "global mark N",
    "O": "global mark O",
    "P": "global mark P",
    "Q": "global mark Q",
    "R": "global mark R",
    "S": "global mark S",
    "T": "global mark T",
    "U": "global mark U",
    "V": "global mark V",
    "W": "global mark W",
    "X": "global mark X",
    "Y": "global mark Y",
    "Z": "global mark Z",

    # Special marks
    ".": "position where last change occurred",
    "^": "position where last insertion stopped",
    "[": "start of last change or yank",
    "]": "end of last change or yank",
    "<": "start of last visual selection",
    ">": "end of last visual selection"
}

# Numeric keys for count
NUMERIC_KEYS = {
    "0": "0",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

# FSM transition examples
"""
Example state transitions for FSM:

NORMAL -> [0-9] -> COUNT_PENDING
COUNT_PENDING -> [0-9] -> COUNT_PENDING (accumulate)
COUNT_PENDING -> [operator] -> OPERATOR_PENDING
COUNT_PENDING -> [motion] -> NORMAL (execute motion with count)

NORMAL -> [operator] -> OPERATOR_PENDING
OPERATOR_PENDING -> [motion] -> NORMAL (execute operator+motion)
OPERATOR_PENDING -> [text object prefix] -> TEXT_OBJECT_PREFIX
TEXT_OBJECT_PREFIX -> [text object target] -> NORMAL (execute operator+text object)

NORMAL -> g -> G_PREFIX
G_PREFIX -> [g_motion/g_operator] -> NORMAL (execute g command)

NORMAL -> f/F/t/T -> WAITING_FOR_CHAR
WAITING_FOR_CHAR -> [any char] -> NORMAL (execute find/till)

NORMAL -> " -> REGISTER
REGISTER -> [register name] -> REGISTER_PENDING
REGISTER_PENDING -> [operator] -> OPERATOR_PENDING (with register)

NORMAL -> : -> COMMAND
COMMAND -> [command text] + Enter -> NORMAL (execute command)
"""

# Example how to use these constants in a FSM
"""
Example parser code:

class VimParser:
    def __init__(self):
        self.state = "NORMAL"
        self.count = ""
        self.operator = None
        self.register = None
        self.buffer = []
        
    def process_key(self, key):
        if self.state == "NORMAL":
            if key in NUMERIC_KEYS and (not self.count or self.count != "0"):
                self.count += key
                self.state = "COUNT_PENDING"
                return
                
            if key in BASIC_OPERATORS:
                self.operator = key
                self.state = "OPERATOR_PENDING"
                return
                
            if key == "g":
                self.state = "G_PREFIX"
                return
                
            if key == "z":
                self.state = "Z_PREFIX"
                return
                
            if key in ["f", "F", "t", "T"]:
                self.operator = key
                self.state = "WAITING_FOR_CHAR"
                return
                
            # Handle other cases...
            
        elif self.state == "COUNT_PENDING":
            if key in NUMERIC_KEYS:
                self.count += key
                return
                
            if key in BASIC_OPERATORS:
                self.operator = key
                self.state = "OPERATOR_PENDING"
                return
                
            # Execute motion with count...
            
        elif self.state == "OPERATOR_PENDING":
            # Handle operator + motion combination
            
        # And so on for other states...
"""

