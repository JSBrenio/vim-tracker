from dataclasses import dataclass
from typing import Optional

# Operators: things that need a motion/text object
OPERATORS = {
    "d": "delete",
    "y": "yank",
    "c": "change",
    "g~": "toggle_case"
}

# Motions: movement commands
MOTIONS = {
    "w": "word",
    "e": "end of word",
    "0": "line start",
    "$": "line end",
    "gg": "buffer start",
    "G": "buffer end"
}

# Text objects (used after `a` or `i`)
TEXT_OBJECTS = {
    "iw": "inner word",
    "aw": "outer word",
    "ip": "inner paragraph",
    "ap": "outer paragraph"
}

@dataclass
class VimCommand:
    count: Optional[int]
    operator: Optional[int]
    motion: Optional[int]
    text_object: Optional[int]

    def __str__(self):
        pass
    