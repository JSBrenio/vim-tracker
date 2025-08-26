from typing import Optional
from vim_parser.grammer import (VimCommand, VimError)
from enum import Enum, auto
from .constants import (
    STATES,
    BASIC_OPERATORS,
    G_OPERATORS,
    Z_OPERATORS,
    BASIC_MOTIONS,
    SEARCH_CHARACTER_MOTIONS,
    G_MOTIONS,
    CTRL_COMMANDS,
    DOUBLE_KEY_COMMANDS,
    TEXT_OBJECT_PREFIXES,
    TEXT_OBJECT_TARGETS,
    VIM_MODES,
    MODE_KEYS,
    COMMAND_COMMANDS,
    SPECIAL_KEYS,
    REGISTER_PREFIXES,
    REGISTER_NAMES,
    MARK_PREFIX,
    MARK_NAMES,
    NUMERIC_KEYS,
)

"""
Finite State Machine
    [operator] [count] [motion | text-object]
    [count] [motion]

Parser needs:
    buffer to keep track of current keystrokes
    count
    operator
    text object
    check each case for a valid vim
    if valid vim command -> return VimCommand object
"""
class State(Enum):
    NORMAL = auto()
    OPERATOR_PENDING = auto()
    REGISTER = auto()
    WAITING_FOR_REGISTER = auto()
    WAITING_FOR_CHAR = auto()
    WAITING_FOR_TEXT_OBJECT = auto()
    INSERT = auto()
    VISUAL = auto()
    COMMAND = auto()

    def __str__(self):
        return self.name
class VimParser:
    def __init__(self, callback: Optional[callable] = None):
        self.callback = callback
        self.reset()

    def reset(self):
        self.state = State.NORMAL
        self.count = ""
        self.operator = None
        self.motion = None
        self.text_object = None
        self.register = None
        self.waiting_for_char = None  # For f/F/t/T commands
        self.buffer = []  # keystroke buffer
        
    def feed(self, key: str) -> Optional[VimCommand]:
        """Feed a single keystroke and return complete command if ready"""

        self.buffer.append(key)
        
        match self.state:
            case State.NORMAL:
                return self._handle_normal(key)
            case State.WAITING_FOR_REGISTER:
                return self._handle_register(key)
            case State.WAITING_FOR_CHAR:
                return self._handle_character_target(key)
            case State.WAITING_FOR_TEXT_OBJECT:
                return self._handle_text_object(key)
            case _:
                error = VimError("".join(self.buffer), f"Not Supported yet | STATE: {self.state}")
                self.reset()
                return error
    
    def _handle_normal(self, key: str):
        """Normal Vim commands """
        # Handle count (digits)
        if key in NUMERIC_KEYS and key != "0":  # 0 is motion, not count at start
            self.count += key
            return None
        
        # Handle register prefix
        if key in REGISTER_PREFIXES:
            self.state = State.WAITING_FOR_REGISTER
            return None
        
        # Handle operators
        if key in BASIC_OPERATORS or key in G_MOTIONS:
            self.operator = key
            # Check for double operators (like dd, yy, cc)
            if len(self.buffer) >= 2 and self.buffer[-2] == key:
                return self._create_command(motion=key)
            return None
        
        # Handle character motions (f/F/t/T)
        if key in SEARCH_CHARACTER_MOTIONS:
            self.waiting_for_char = key
            self.state = State.WAITING_FOR_CHAR
            return None
        
        # Handle basic motions
        if key in BASIC_MOTIONS:
            self.motion = key
            return self._create_command()
        
        # Handle text object prefixes (i/a) Text objects need an operator
        if key in TEXT_OBJECT_PREFIXES and self.operator:
            self.state = State.WAITING_FOR_TEXT_OBJECT
            self.text_object = key
            return None
        
        # Invalid key, reset
        error = VimError("".join(self.buffer), f"Malformed Normal | STATE: {self.state}")
        self.reset()
        return error
    
    def _handle_register(self, key: str) -> Optional[VimCommand]:
        if key in REGISTER_NAMES:
            self.register = key
            self.state = "NORMAL"
            return None
        else:
            self.reset()
            return None
    
    def _handle_character_target(self, key: str) -> Optional[VimCommand]:
        # Any character can be a target for f/F/t/T
        self.motion = self.waiting_for_char
        command = self._create_command(target_char=key)
        return command
    
    def _handle_text_object(self, key: str) -> Optional[VimCommand]:
        if key in TEXT_OBJECT_TARGETS:
            self.text_object += key  # Combine prefix + target (e.g., "i" + "w" = "iw")
            return self._create_command()
        else:
            self.reset()
            return None
    
    def _create_command(self, **kwargs) -> VimCommand:
        """Create a VimCommand and reset parser state"""
        count = int(self.count) if self.count else None
        
        command = VimCommand(
            count=count,
            operator=self.operator,
            motion=self.motion or kwargs.get('motion'),
            text_object=self.text_object,
            register=self.register,
            target_char=kwargs.get('target_char')
        )
        
        # Call callback if provided
        if self.callback and command.is_complete():
            self.callback(command)
        
        self.reset()
        return command if command.is_complete() else None

if __name__ == "__main__":
    parser = VimParser()
    keys = ["d", "w", "c", "i", "w", "3", "4", "d", "d", "g", "g"]
    # Should be 
    # Parsed: dw
    # Parsed: ciw
    # Parsed: 3dd
    # Parsed: gg
    for k in keys:
        result = parser.feed(k)
        if result:
            print("Parsed:", result)