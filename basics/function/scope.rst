************************
Function Variables Scope
************************


Access Scope
============
.. code-block:: python
    :caption: Functions has access to global values

    DATA = [1, 2, 3]

    def add():
        return sum(DATA)

    print(add())
    # 6

.. code-block:: python
    :caption: Shadowing

    DATA = [1, 2, 3]

    def add():
        DATA = [10, 20, 30]
        return sum(DATA)

    print(add())
    # 60

    print(DATA)
    # [1, 2, 3]

.. code-block:: python
    :caption: Modify global, BAD PRACTICE!!

    DATA = [1, 2, 3]

    def add():
        global DATA
        DATA = [10, 20, 30]
        return sum(DATA)


    print(add())
    # 60

    print(DATA)
    # [10, 20, 30]


Global Scope
============
.. highlights::
    * All variables in main program
    * Variables are available inside all functions

.. code-block:: python

    print(globals())
    # {'__builtins__': {'ArithmeticError': <class 'ArithmeticError'>,
    #                   'AssertionError': <class 'AssertionError'>,
    #                   'AttributeError': <class 'AttributeError'>,
    #                   'BaseException': <class 'BaseException'>,
    #                   'BlockingIOError': <class 'BlockingIOError'>,
    #                   'BrokenPipeError': <class 'BrokenPipeError'>,
    #                   'BufferError': <class 'BufferError'>,
    #                   'BytesWarning': <class 'BytesWarning'>,
    #                   'ChildProcessError': <class 'ChildProcessError'>,
    #                   'ConnectionAbortedError': <class 'ConnectionAbortedError'>,
    #                   'ConnectionError': <class 'ConnectionError'>,
    #                   'ConnectionRefusedError': <class 'ConnectionRefusedError'>,
    #                   'ConnectionResetError': <class 'ConnectionResetError'>,
    #                   'DeprecationWarning': <class 'DeprecationWarning'>,
    #                   'EOFError': <class 'EOFError'>,
    #                   'Ellipsis': Ellipsis,
    #                   'EnvironmentError': <class 'OSError'>,
    #                   'Exception': <class 'Exception'>,
    #                   'False': False,
    #                   'FileExistsError': <class 'FileExistsError'>,
    #                   'FileNotFoundError': <class 'FileNotFoundError'>,
    #                   'FloatingPointError': <class 'FloatingPointError'>,
    #                   'FutureWarning': <class 'FutureWarning'>,
    #                   'GeneratorExit': <class 'GeneratorExit'>,
    #                   'IOError': <class 'OSError'>,
    #                   'ImportError': <class 'ImportError'>,
    #                   'ImportWarning': <class 'ImportWarning'>,
    #                   'IndentationError': <class 'IndentationError'>,
    #                   'IndexError': <class 'IndexError'>,
    #                   'InterruptedError': <class 'InterruptedError'>,
    #                   'IsADirectoryError': <class 'IsADirectoryError'>,
    #                   'KeyError': <class 'KeyError'>,
    #                   'KeyboardInterrupt': <class 'KeyboardInterrupt'>,
    #                   'LookupError': <class 'LookupError'>,
    #                   'MemoryError': <class 'MemoryError'>,
    #                   'ModuleNotFoundError': <class 'ModuleNotFoundError'>,
    #                   'NameError': <class 'NameError'>,
    #                   'None': None,
    #                   'NotADirectoryError': <class 'NotADirectoryError'>,
    #                   'NotImplemented': NotImplemented,
    #                   'NotImplementedError': <class 'NotImplementedError'>,
    #                   'OSError': <class 'OSError'>,
    #                   'OverflowError': <class 'OverflowError'>,
    #                   'PendingDeprecationWarning': <class
    #                   'PendingDeprecationWarning'>,
    #                   'PermissionError': <class 'PermissionError'>,
    #                   'ProcessLookupError': <class 'ProcessLookupError'>,
    #                   'RecursionError': <class 'RecursionError'>,
    #                   'ReferenceError': <class 'ReferenceError'>,
    #                   'ResourceWarning': <class 'ResourceWarning'>,
    #                   'RuntimeError': <class 'RuntimeError'>,
    #                   'RuntimeWarning': <class 'RuntimeWarning'>,
    #                   'StopAsyncIteration': <class 'StopAsyncIteration'>,
    #                   'StopIteration': <class 'StopIteration'>,
    #                   'SyntaxError': <class 'SyntaxError'>,
    #                   'SyntaxWarning': <class 'SyntaxWarning'>,
    #                   'SystemError': <class 'SystemError'>,
    #                   'SystemExit': <class 'SystemExit'>,
    #                   'TabError': <class 'TabError'>,
    #                   'TimeoutError': <class 'TimeoutError'>,
    #                   'True': True,
    #                   'TypeError': <class 'TypeError'>,
    #                   'UnboundLocalError': <class 'UnboundLocalError'>,
    #                   'UnicodeDecodeError': <class 'UnicodeDecodeError'>,
    #                   'UnicodeEncodeError': <class 'UnicodeEncodeError'>,
    #                   'UnicodeError': <class 'UnicodeError'>,
    #                   'UnicodeTranslateError': <class 'UnicodeTranslateError'>,
    #                   'UnicodeWarning': <class 'UnicodeWarning'>,
    #                   'UserWarning': <class 'UserWarning'>,
    #                   'ValueError': <class 'ValueError'>,
    #                   'Warning': <class 'Warning'>,
    #                   'ZeroDivisionError': <class 'ZeroDivisionError'>,
    #                   '_': <Recursion on dict with id=4575702144>,
    #                   '__build_class__': <built-in function __build_class__>,
    #                   '__debug__': True,
    #                   '__doc__': 'Built-in functions, exceptions, and other '
    #                              'objects.\n'
    #                              '\n'
    #                              "Noteworthy: None is the `nil' object;
    #                              Ellipsis "
    #                              "represents `...' in slices.",
    #                   '__import__': <bound method ImportHookManager.do_import
    #                   of <module '_pydev_bundle.pydev_import_hook.import_hook'>>,
    #                   '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
    #                   '__name__': 'builtins',
    #                   '__package__': '',
    #                   '__spec__': ModuleSpec(name='builtins', loader=<class
    #                   '_frozen_importlib.BuiltinImporter'>),
    #                   'abs': <built-in function abs>,
    #                   'all': <built-in function all>,
    #                   'any': <built-in function any>,
    #                   'ascii': <built-in function ascii>,
    #                   'bin': <built-in function bin>,
    #                   'bool': <class 'bool'>,
    #                   'breakpoint': <built-in function breakpoint>,
    #                   'bytearray': <class 'bytearray'>,
    #                   'bytes': <class 'bytes'>,
    #                   'callable': <built-in function callable>,
    #                   'chr': <built-in function chr>,
    #                   'classmethod': <class 'classmethod'>,
    #                   'compile': <built-in function compile>,
    #                   'complex': <class 'complex'>,
    #                   'copyright': Copyright (c) 2001-2019 Python Software Foundation.,
    #                   'delattr': <built-in function delattr>,
    #                   'dict': <class 'dict'>,
    #                   'dir': <built-in function dir>,
    #                   'divmod': <built-in function divmod>,
    #                   'enumerate': <class 'enumerate'>,
    #                   'eval': <built-in function eval>,
    #                   'exec': <built-in function exec>,
    #                   'execfile': <function execfile at 0x1107e93b0>,
    #                   'exit': Use exit() or Ctrl-D (i.e. EOF) to exit,
    #                   'filter': <class 'filter'>,
    #                   'float': <class 'float'>,
    #                   'format': <built-in function format>,
    #                   'frozenset': <class 'frozenset'>,
    #                   'getattr': <built-in function getattr>,
    #                   'globals': <built-in function globals>,
    #                   'hasattr': <built-in function hasattr>,
    #                   'hash': <built-in function hash>,
    #                   'help': Type help() for interactive help, or help(
    #                   object) for help about object.,
    #                   'hex': <built-in function hex>,
    #                   'id': <built-in function id>,
    #                   'input': <built-in function input>,
    #                   'int': <class 'int'>,
    #                   'isinstance': <built-in function isinstance>,
    #                   'issubclass': <built-in function issubclass>,
    #                   'iter': <built-in function iter>,
    #                   'len': <built-in function len>,
    #                   'license': Type license() to see the full license text,
    #                   'list': <class 'list'>,
    #                   'locals': <built-in function locals>,
    #                   'map': <class 'map'>,
    #                   'max': <built-in function max>,
    #                   'memoryview': <class 'memoryview'>,
    #                   'min': <built-in function min>,
    #                   'next': <built-in function next>,
    #                   'object': <class 'object'>,
    #                   'oct': <built-in function oct>,
    #                   'open': <built-in function open>,
    #                   'ord': <built-in function ord>,
    #                   'pow': <built-in function pow>,
    #                   'print': <built-in function print>,
    #                   'property': <class 'property'>,
    #                   'quit': Use quit() or Ctrl-D (i.e. EOF) to exit,
    #                   'range': <class 'range'>,
    #                   'repr': <built-in function repr>,
    #                   'reversed': <class 'reversed'>,
    #                   'round': <built-in function round>,
    #                   'runfile': <function runfile at 0x110bb24d0>,
    #                   'set': <class 'set'>,
    #                   'setattr': <built-in function setattr>,
    #                   'slice': <class 'slice'>,
    #                   'sorted': <built-in function sorted>,
    #                   'staticmethod': <class 'staticmethod'>,
    #                   'str': <class 'str'>,
    #                   'sum': <built-in function sum>,
    #                   'super': <class 'super'>,
    #                   'tuple': <class 'tuple'>,
    #                   'type': <class 'type'>,
    #                   'vars': <built-in function vars>,
    #                   'zip': <class 'zip'>},
    #  '__doc__': None,
    #  '__file__': '<input>',
    #  '__loader__': <_frozen_importlib_external.SourceFileLoader object at
    #  0x100dea9d0>,
    #  '__name__': '__main__',
    #  '__package__': None,
    #  '__spec__': None}


Local Scope
===========
.. highlights::
    * Variables defined inside function
    * Variables are not available from outside
    * If outside the function, will return the same as ``globals()``

.. code-block:: python

    print(locals())
    # {...}

.. code-block:: python

    def echo():
        a = 1
        print(locals())

    echo()
    # {'a': 1}

.. code-block:: python

    def echo(a, b=2):
        c = 3
        print(locals())

    echo(1)
    # {'a':1, 'b':2, 'c':3}


Assignments
===========

Wanted
------
* Complexity level: easy
* Lines of code to write: 5 lines
* Estimated time of completion: 5 min
* Solution: :download:`solution/scope_wanted.py`

:English:
    #. Separate header (first line) from data
    #. For given input data (see below)
    #. Define ``wanted: Set[str]`` with 'setosa' and 'versicolor'
    #. Iterate over data and split row into ``features`` and ``label`` (last)
    #. Define function which sums ``features``, only when ``label`` is in ``wanted``
    #. When ``label`` is not in ``wanted`` return ``0`` (zero)
    #. Print sum

:Polish:
    #. Oddziel nagłówek (pierwsza linia) od danych
    #. Dla danych wejściowych (patrz sekcja input)
    #. Zdefiniuj ``wanted: Set[str]`` z 'setosa' oraz 'versicolor'
    #. Iterując po danych rozdziel wiersz na ``features`` i ``label`` (ostatni)
    #. Zdefiniuj funkcję sumującą ``features``, tylko gdy ``label`` jest w ``wanted``
    #. Gdy ``label`` nie występuje w ``wanted`` zwróć ``0`` (zero)
    #. Wypisz sumę

:Input:
    .. code-block:: python

        INPUT = [
            ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
            (5.8, 2.7, 5.1, 1.9, 'virginica'),
            (5.1, 3.5, 1.4, 0.2, 'setosa'),
            (5.7, 2.8, 4.1, 1.3, 'versicolor'),
            (6.3, 2.9, 5.6, 1.8, 'virginica'),
            (6.4, 3.2, 4.5, 1.5, 'versicolor'),
            (4.7, 3.2, 1.3, 0.2, 'setosa'),
            (7.0, 3.2, 4.7, 1.4, 'versicolor'),
            (7.6, 3.0, 6.6, 2.1, 'virginica'),
            (4.9, 3.0, 1.4, 0.2, 'setosa'),
        ]

:Output:
    .. code-block:: python

        OUTPUT: float
        # 74.9

Roman numbers
-------------
* Complexity level: hard
* Lines of code to write: 15 lines
* Estimated time of completion: 15 min
* Solution: :download:`solution/scope_roman.py`

:English:
    #. Define function converting roman numerals to integer
    #. Define function converting integer to roman numerals

:Polish:
    #. Zdefiniuj funkcję przeliczającą liczbę rzymską na całkowitą
    #. Zdefiniuj funkcję przeliczającą liczbę całkowitą na rzymską

:Input:
    .. code-block:: python

        CONVERSION_TABLE = {
            'I': 1,
            'II': 2,
            'III': 3,
            'IV': 4,
            'V': 5,
            'VI': 6,
            'VII': 7,
            'VIII': 8,
            'IX': 9,
            'X': 10,
            'XX': 20,
            'XXX': 30,
            'XL': 40,
            'L': 50,
            'LX': 60,
            'LXX': 70,
            'LXXX': 80,
            'XC': 90,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

:The whys and wherefores:
    * Defining and calling functions
    * Checking for corner cases
    * Passing function arguments
    * Cleaning data from user input
    * ``dict`` lookups
