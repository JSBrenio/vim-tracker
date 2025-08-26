

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

class VimParser:
    def __init__(self):
        pass
    
    def reset(self):
        pass
    
    def feed(self, key: str):
        pass
    
    