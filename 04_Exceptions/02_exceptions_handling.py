#!/usr/bin/python3
"""
Purpose: Exception Handling

NOTE: Syntax errors cant be handled by except

"""

# import builtins

# print(dir(builtins))

# ['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BaseExceptionGroup', 'BlockingIOError',
#  'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError',
#  'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning',
#  'EnvironmentError', 'Exception', 'ExceptionGroup', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError',
#  'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError',
#  'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError',
#  'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError',
#  'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError',
#  'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration',
#  'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit',  'TabError', 'TimeoutError', 'True', 'TypeError',
#  'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError',
#  'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError',

#  '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__',

#  'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable',
#  'chr',  'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod',
#  'enumerate', 'eval',  'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr',
#  'hash', 'help', 'hex', 'id',  'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals',
#  'map', 'max', 'memoryview', 'min',   'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit',
#  'range', 'repr', 'reversed', 'round', 'set',    'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
#  'super', 'tuple', 'type', 'vars', 'zip']


num1 = 10
#  num2 = 20  # IndentationError: unexpected indent

# for i in range(20):
# print(i)
# IndentationError: expected an indented block after 'for' statement on line 40


# 10 / 0  # ZeroDivisionError: division by zero
# 10 % 0  # ZeroDivisionError: integer modulo by zero
# 10 // 0 # ZeroDivisionError: integer division or modulo by zero


# 10 + '20'  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# 10.0 + '20'# TypeError: unsupported operand type(s) for +: 'float' and 'str'



# num1.upper()  # AttributeError: 'int' object has no attribute 'upper'

mydict = {"a": "apple"}
# mydict['b']  # KeyError: 'b'

# num3 = int(input('Enter number:'))  # 12.3
# ValueError: invalid literal for int() with base 10: '12.3'
