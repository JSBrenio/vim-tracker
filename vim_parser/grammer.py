from dataclasses import dataclass
from typing import Optional

"""
VIM Structure:
Formal Language: regular

FOR NORMAL:

    basic/common
        [operator] [count] [motion | text-object]
        [count] [motion]

    Ex commands from Normal
        :command

    extended commands
        g

    registers
        "{register}

    recording
        q{register}
        
FOR VISUAL:

    [operator]
    g
    :
    
FOR INSERT:

    registers
        <C-r>
    
"""

"""
Note on @dataclass
- The @dataclass decorator (from the standard library's dataclasses module)
  is a convenience that reduces boilerplate when creating classes meant to
  primarily store data.
- What @dataclass gives you automatically:
    - An __init__ method that assigns constructor arguments to instance
      attributes based on the declared fields and types.
    - A helpful __repr__ for debugging that prints field names and values.
    - Comparison methods (__eq__, etc.) when requested, allowing value-based
      comparisons between instances.
    - Options to customize behavior: frozen=True to make instances immutable,
      order=True to generate ordering methods, and default_factory for
      mutable default values.
- Educational note: using @dataclass makes intent explicit — this class is
  a lightweight data holder. It does not change runtime typing, but it
  simplifies writing, reading, and testing code that manipulates structured
  data like parsed Vim commands.
Examples
- Representing "dw" (delete a word): VimCommand(count=None, operator='d',
  motion='w', text_object=None)
- Representing "2gg" (go to buffer start twice — effectively same as 'gg'
  but with count): VimCommand(count=2, operator=None, motion='gg', text_object=None)
- Representing "ciw" (change inner word): VimCommand(count=None, operator='c',
  motion=None, text_object='iw')
"""
@dataclass
class VimCommand:
    count: Optional[int]
    operator: Optional[int]
    motion: Optional[int]
    text_object: Optional[int]

    def __str__(self):
        pass
    