"""
Test data for FSM testing
Contains arrays of keystrokes for various vim command patterns
"""

# Basic operator + motion combinations
BASIC_COMMANDS = [
    # Delete commands
    {
        'keys': ['d', 'w'],
        'description': 'delete word',
        'expected': {'operator': 'd', 'motion': 'w'}
    },
    {
        'keys': ['d', 'd'],
        'description': 'delete line',
        'expected': {'operator': 'd', 'motion': 'd'}
    },
    {
        'keys': ['d', '$'],
        'description': 'delete to end of line',
        'expected': {'operator': 'd', 'motion': '$'}
    },
    
    # Yank commands
    {
        'keys': ['y', 'y'],
        'description': 'yank line',
        'expected': {'operator': 'y', 'motion': 'y'}
    },
    {
        'keys': ['y', 'w'],
        'description': 'yank word',
        'expected': {'operator': 'y', 'motion': 'w'}
    },
    
    # Change commands
    {
        'keys': ['c', 'w'],
        'description': 'change word',
        'expected': {'operator': 'c', 'motion': 'w'}
    },
    {
        'keys': ['c', 'c'],
        'description': 'change line',
        'expected': {'operator': 'c', 'motion': 'c'}
    }
]

# Commands with text objects
TEXT_OBJECT_COMMANDS = [
    # Inner text objects
    {
        'keys': ['d', 'i', 'w'],
        'description': 'delete inner word',
        'expected': {'operator': 'd', 'text_object_prefix': 'i', 'text_object': 'w'}
    },
    {
        'keys': ['c', 'i', '('],
        'description': 'change inner parentheses',
        'expected': {'operator': 'c', 'text_object_prefix': 'i', 'text_object': '('}
    },
    {
        'keys': ['y', 'i', '"'],
        'description': 'yank inner quotes',
        'expected': {'operator': 'y', 'text_object_prefix': 'i', 'text_object': '"'}
    },
    
    # Around text objects
    {
        'keys': ['d', 'a', 'w'],
        'description': 'delete around word',
        'expected': {'operator': 'd', 'text_object_prefix': 'a', 'text_object': 'w'}
    },
    {
        'keys': ['c', 'a', '{'],
        'description': 'change around braces',
        'expected': {'operator': 'c', 'text_object_prefix': 'a', 'text_object': '{'}
    },
    {
        'keys': ['y', 'a', 'p'],
        'description': 'yank around paragraph',
        'expected': {'operator': 'y', 'text_object_prefix': 'a', 'text_object': 'p'}
    }
]

# Commands with counts
COUNT_COMMANDS = [
    {
        'keys': ['3', 'd', 'w'],
        'description': 'delete 3 words',
        'expected': {'count': 3, 'operator': 'd', 'motion': 'w'}
    },
    {
        'keys': ['5', 'j'],
        'description': 'move down 5 lines',
        'expected': {'count': 5, 'motion': 'j'}
    },
    {
        'keys': ['1', '0', 'y', 'y'],
        'description': 'yank 10 lines',
        'expected': {'count': 10, 'operator': 'y', 'motion': 'y'}
    },
    {
        'keys': ['2', 'c', 'i', 'w'],
        'description': 'change 2 inner words',
        'expected': {'count': 2, 'operator': 'c', 'text_object_prefix': 'i', 'text_object': 'w'}
    }
]

# G-prefixed commands
G_PREFIX_COMMANDS = [
    {
        'keys': ['g', 'g'],
        'description': 'go to beginning of buffer',
        'expected': {'motion': 'gg'}
    },
    {
        'keys': ['g', 'd'],
        'description': 'go to definition',
        'expected': {'operator': 'gd'}
    },
    {
        'keys': ['g', '~', 'w'],
        'description': 'toggle case of word',
        'expected': {'operator': 'g~', 'motion': 'w'}
    },
    {
        'keys': ['g', 'u', 'i', 'w'],
        'description': 'lowercase inner word',
        'expected': {'operator': 'gu', 'text_object_prefix': 'i', 'text_object': 'w'}
    }
]

# Z-prefixed commands
Z_PREFIX_COMMANDS = [
    {
        'keys': ['z', 'z'],
        'description': 'center cursor line',
        'expected': {'operator': 'zz'}
    },
    {
        'keys': ['z', 'o'],
        'description': 'open fold',
        'expected': {'operator': 'zo'}
    },
    {
        'keys': ['z', 'c'],
        'description': 'close fold',
        'expected': {'operator': 'zc'}
    },
    {
        'keys': ['z', 'f', 'i', 'p'],
        'description': 'create fold around paragraph',
        'expected': {'operator': 'zf', 'text_object_prefix': 'i', 'text_object': 'p'}
    }
]

# Find/till commands
FIND_COMMANDS = [
    {
        'keys': ['f', 'a'],
        'description': 'find character a forward',
        'expected': {'motion': 'f', 'target_char': 'a'}
    },
    {
        'keys': ['F', 'x'],
        'description': 'find character x backward',
        'expected': {'motion': 'F', 'target_char': 'x'}
    },
    {
        'keys': ['t', 'e'],
        'description': 'till character e forward',
        'expected': {'motion': 't', 'target_char': 'e'}
    },
    {
        'keys': ['T', 's'],
        'description': 'till character s backward',
        'expected': {'motion': 'T', 'target_char': 's'}
    },
    {
        'keys': ['d', 'f', 'x'],
        'description': 'delete to find character x',
        'expected': {'operator': 'd', 'motion': 'f', 'target_char': 'x'}
    },
    {
        'keys': ['c', 't', ';'],
        'description': 'change till semicolon',
        'expected': {'operator': 'c', 'motion': 't', 'target_char': ';'}
    }
]

# Register commands
REGISTER_COMMANDS = [
    {
        'keys': ['"', 'a', 'y', 'w'],
        'description': 'yank word to register a',
        'expected': {'register': 'a', 'operator': 'y', 'motion': 'w'}
    },
    {
        'keys': ['"', '+', 'd', 'd'],
        'description': 'delete line to clipboard',
        'expected': {'register': '+', 'operator': 'd', 'motion': 'd'}
    },
    {
        'keys': ['"', '0', 'p'],
        'description': 'paste from register 0',
        'expected': {'register': '0', 'operator': 'p'}
    },
    {
        'keys': ['"', 'b', '3', 'y', 'i', 'w'],
        'description': 'yank 3 inner words to register b',
        'expected': {'register': 'b', 'count': 3, 'operator': 'y', 'text_object_prefix': 'i', 'text_object': 'w'}
    }
]

# Mode change commands
MODE_COMMANDS = [
    {
        'keys': ['i'],
        'description': 'enter insert mode',
        'expected': {'mode_change': 'INSERT'}
    },
    {
        'keys': ['a'],
        'description': 'append (insert after cursor)',
        'expected': {'mode_change': 'INSERT', 'cursor_action': 'after'}
    },
    {
        'keys': ['v'],
        'description': 'enter visual mode',
        'expected': {'mode_change': 'VISUAL'}
    },
    {
        'keys': ['V'],
        'description': 'enter visual line mode',
        'expected': {'mode_change': 'VISUAL_LINE'}
    },
    {
        'keys': [':'],
        'description': 'enter command mode',
        'expected': {'mode_change': 'COMMAND'}
    }
]

# Complex sequences
COMPLEX_COMMANDS = [
    {
        'keys': ['"', 'a', '3', 'd', 'a', 'w'],
        'description': 'delete 3 words around cursor to register a',
        'expected': {
            'register': 'a',
            'count': 3,
            'operator': 'd',
            'text_object_prefix': 'a',
            'text_object': 'w'
        }
    },
    {
        'keys': ['5', 'g', 'u', 'f', 'x'],
        'description': 'lowercase 5 characters until find x',
        'expected': {
            'count': 5,
            'operator': 'gu',
            'motion': 'f',
            'target_char': 'x'
        }
    },
    {
        'keys': ['"', '+', '2', 'z', 'f', 'i', '{'],
        'description': 'create 2 folds around inner braces to clipboard register',
        'expected': {
            'register': '+',
            'count': 2,
            'operator': 'zf',
            'text_object_prefix': 'i',
            'text_object': '{'
        }
    }
]

# Invalid/error sequences
INVALID_COMMANDS = [
    {
        'keys': ['d'],
        'description': 'incomplete delete command',
        'expected_error': 'incomplete_command'
    },
    {
        'keys': ['d', 'd', 'w'],
        'description': 'dd followed by motion (invalid)',
        'expected_error': 'invalid_sequence'
    },
    {
        'keys': ['f'],
        'description': 'find without character',
        'expected_error': 'missing_character'
    },
    {
        'keys': ['"'],
        'description': 'register without name',
        'expected_error': 'missing_register'
    }
]

# All test data combined
ALL_TEST_DATA = {
    'basic_commands': BASIC_COMMANDS,
    'text_object_commands': TEXT_OBJECT_COMMANDS,
    'count_commands': COUNT_COMMANDS,
    'g_prefix_commands': G_PREFIX_COMMANDS,
    'z_prefix_commands': Z_PREFIX_COMMANDS,
    'find_commands': FIND_COMMANDS,
    'register_commands': REGISTER_COMMANDS,
    'mode_commands': MODE_COMMANDS,
    'complex_commands': COMPLEX_COMMANDS,
    'invalid_commands': INVALID_COMMANDS
}
