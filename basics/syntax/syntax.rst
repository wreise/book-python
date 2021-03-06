*************
Python Syntax
*************


Indentation
===========
.. highlights::
    * Python uses indentation instead of braces
    * :pep:`8`: 4 spaces indentation, `no tabs <https://youtu.be/SsoOG6ZeyUI>`_
    * Python throws ``IndentationError`` exception on problem
    * Code indented on the same level belongs to block

.. code-block:: python

    if True:
       print('First line of the true statement')
       print('Second line of the true statement')
       print('Third line of the true statement')
    else:
       print('This is false')


End of Lines
============
.. highlights::
    * No semicolon (``;``) at the end of lines
    * ``\r\n`` and ``\n`` works
    * :pep:`8`: Use ``\n``

.. doctest::

    >>> print('Hello!\nHow are you?')
    Hello!
    How are you?


Comments
========
.. highlights::
    * Indent must be on the same level as block indent
    * :pep:`8` - Line comments: Hash (``#``), space and then comment
    * :pep:`8` - Inline comments: code, two spaces, hash (``#``), space and then comment
    * :pep:`8` - Multiline comments: If assigned to variable, it serves as multiline ``str``
    * Commented out code:

        * Never!
        * Use Version Control System instead - e.g.: ``git blame``
        * IDE has Local history (modifications) and you can compare file

.. code-block:: python
    :caption: Line comments

    # José Jiménez says hello
    print('My name... José Jiménez')

.. code-block:: python
    :caption: Inline comments

    print('My name... José Jiménez')  # José Jiménez says hello

.. code-block:: python
    :caption: Multiline comments

    """
    We choose to go to the Moon!
    We choose to go to the Moon in this decade and do the other things,
    not because they are easy, but because they are hard;
    because that goal will serve to organize and measure the best of our energies and skills,
    because that challenge is one that we are willing to accept, one we are unwilling to postpone,
    and one we intend to win, and the others, too.
    """


Variables and Constants
=======================
.. highlights::
    * ``NameError`` when using not declared variable
    * ``AttributeError`` when cannot assign to variables
    * Names are case sensitive
    * Python do not distinguish between variables and constants
    * Python allows you to change "constants" but it's a bad practice (good IDE will tell you)
    * Lowercase letters for variable names
    * Uppercase letters for "constant" names
    * Underscore ``_`` is used for multi-word names

.. code-block:: python
    :caption: Variable declaration

    name = 'José Jiménez'
    first_name = 'José'
    last_name = 'Jiménez'

.. code-block:: python
    :caption: "Constant" declaration

    PATH = '/etc/passwd'
    FILE_NAME = '/etc/shadow'

.. code-block:: python
    :caption: Variables vs. constants - Names are case sensitive

    name = 'José Jiménez'
    NAME = 'Иван Иванович'
    Name = 'Jan Twardowski'

.. code-block:: python
    :caption: Python allows you to change "constants" but it's a bad practice (good IDE will tell you)

    NAME = 'José Jiménez'
    NAME = 'Иван Иванович'


Printing Values
===============
.. highlights::
    * ``print()`` adds ``'\n'`` at the end
    * Prints on the screen
    * Variable substitution
    * Special characters
    * More in :ref:`Builtin Printing`

.. code-block:: python

    print('My name... José Jiménez')
    # My name... José Jiménez

.. code-block:: python

    name = 'José Jiménez'


    print('My name... {name}')
    # My name... {name}

    print(f'My name... {name}')
    # My name... José Jiménez

    print(f'My name...\n\t{name}')
    # My name...
    #     José Jiménez


Assignments
===========

Meet Python
-----------
* Complexity level: easy
* Lines of code to write: 2 lines + 2 lines of comment
* Estimated time of completion: 5 min
* Solution: :download:`solution/syntax_python.py`

:English:
    #. Create Python script
    #. At at top, add a multiline comment with program description (todo from this assignments)
    #. Declare variable ``name`` and set its value to your name
    #. Add inline comment to variable declaration with text: "This is my name"
    #. Print "Hello World NAME", where NAME is your name (variable ``name``)
    #. Next line under ``print`` statement add line comment, with expected output

:Polish:
    #. Stwórz skrypt Python
    #. Na górze pliku dodaj wielolinijkowy komentarz z opisem programu (punkty do wykonia z tego zadania)
    #. Zadeklaruj zmienną ``name`` i ustaw jej wartość na Twoje imię
    #. Dodaj komentarz "inline" do zmiennej o treści: "This is my name"
    #. Wypisz "Hello World NAME", gdzie NAME to Twoje imię (zmienna ``name``)

:The whys and wherefores:
    * Tworzenie skryptów Python
    * Deklaracja zmiennych
    * Komentowanie kodu
    * Wyświetlanie wartości zmiennych

:Hint:
    * ``print()``
