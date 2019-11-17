.. _Basic Comprehensions:

**************
Comprehensions
**************


Syntax
======
.. code-block:: python

    output = [<RETURN> for <VARIABLE> in <SEQUENCE>]

.. code-block:: python

    [x for x in range(0,5)]
    # [1, 2, 3, 4]

    [x**2 for x in range(0,5)]
    # [1, 2, 4, 16]


Generator expressions vs. Comprehensions
========================================
.. highlights::
    * Comprehensions executes instantly
    * Generator expression executes lazily

.. code-block:: python

    list(x for x in range(0,5))        # [0, 1, 2, 3, 4]
    [x for x in range(0,5)]            # [0, 1, 2, 3, 4]

    set(x for x in range(0,5))         # {0, 1, 2, 3, 4}
    {x for x in range(0,5)}            # {0, 1, 2, 3, 4}

    {x: x for x in range(0,5)}         # {0: 0, 1: 1, 2: 2, 3: 3, 4: 4}

    tuple(x for x in range(0,5))       # (0, 1, 2, 3, 4)
    (x for x in range(0,5))            # <generator object <genexpr> at 0x118c1aed0>

    all(x for x in range(0,5))         # False
    any(x for x in range(0,5))         # True
    sum(x for x in range(0,5))         # 10


Simple usage
============

Traditional
-----------
.. code-block:: python
    :caption: Iterative approach to applying function to elements

    numbers = []

    for x in range(0, 5):
        numbers.append(x+10)

    print(numbers)
    # [10, 11, 12, 13, 14]

List Comprehension
------------------
.. code-block:: python
    :caption: ``list`` Comprehension approach to applying function to elements

    [x+10 for x in range(0, 5)]
    # [10, 11, 12, 13, 14]

Set Comprehension
-----------------
.. code-block:: python
    :caption: ``set`` Comprehension approach to applying function to elements

    {x+10 for x in range(0, 5)}
    # {10, 11, 12, 13, 14}

Dict Comprehension
------------------
.. code-block:: python
    :caption: ``dict`` Comprehension approach to applying function to elements

    {x: x+10 for x in range(0, 5)}
    # {0:10, 1:11, 2:12, 3:13, 4:14}

.. code-block:: python
    :caption: ``dict`` Comprehension approach to applying function to elements

    {x+10: x for x in range(0, 5)}
    # {10:0, 11:1, 12:2, 13:3, 14:4}

.. code-block:: python
    :caption: ``dict`` Comprehension approach to applying function to elements

    {x+10: x+10 for x in range(0, 5)}
    # {10:10, 11:11, 12:12, 13:13, 14:14}

Tuple Comprehension?!
---------------------
.. highlights::
    * Tuple Comprehension vs. Generator Expression
    * More in chapter :ref:`Generators`

.. code-block:: python
    :caption: Tuple Comprehension

    tuple(x for x in range(0,5))
    # (0, 1, 2, 3, 4)

.. code-block:: python
    :caption: Generator Expression

    (x+10 for x in range(0, 5))
    # <generator object <genexpr> at 0x11eaef570>


Conditional Comprehension
=========================
.. code-block:: python
    :caption: Iterative approach to applying function to selected elements

    even_numbers = []

    for x in range(0, 5):
        if x % 2 == 0:
            even_numbers.append(x)

    print(even_numbers)
    # [0, 2, 4]

.. code-block:: python
    :caption: ``list`` Comprehensions approach to applying function to selected elements

    [x for x in range(0, 5) if x % 2 == 0]
    # [0, 2, 4]

Filtering ``dict`` items
------------------------
.. code-block:: python

    DATA = [
        {'first_name': 'Иван', 'last_name': 'Иванович', 'agency': 'Roscosmos'},
        {'first_name': 'Jose', 'last_name': 'Jimenez', 'agency': 'NASA'},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'agency': 'NASA'},
        {'first_name': 'Alex', 'last_name': 'Vogel', 'agency': 'ESA'},
        {'first_name': 'Mark', 'last_name': 'Watney', 'agency': 'NASA'},
    ]

    nasa_astronauts = [(astro['first_name'], astro['last_name'])
                            for astro in DATA
                                if astro['agency'] == 'NASA']
    # [
    #   ('Jose', 'Jimenez'),
    #   ('Melissa', 'Lewis'),
    #   ('Mark', 'Watney')
    # ]


Applying function
=================
.. code-block:: python
    :caption: Applying function to each output element

    [float(x) for x in range(0, 5)]
    # [0.0, 1.0, 2.0, 3.0, 4.0]

    [float(x) for x in range(0, 5) if x % 2 == 0]
    # [0.0, 2.0, 4.0]

.. code-block:: python
    :caption: Applying function to each output element

    [pow(x, 2) for x in range(0, 5)]
    # [0, 1, 4, 9, 16]

    [pow(x, 2) for x in range(0, 5) if x % 2 == 0]
    # [0, 4, 16]


Nested Comprehensions
=====================
.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set()

    fieldnames.update(key for record in DATA for key in record.keys())
    # {'born', 'last_name', 'first_step', 'first_name'}

.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set()

    fieldnames.update(key
        for record in DATA
            for key in record.keys()
    )
    # {'born', 'last_name', 'first_step', 'first_name'}

.. code-block:: python

   DATA = [
        {'last_name': 'Jiménez'},
        {'first_name': 'Mark', 'last_name': 'Watney'},
        {'first_name': 'Иван'},
        {'first_name': 'Jan', 'last_name': 'Twardowski', 'born': 1961},
        {'first_name': 'Melissa', 'last_name': 'Lewis', 'first_step': 1969},
    ]

    fieldnames = set(key
        for record in DATA
            for key in record.keys()
    )
    # {'born', 'last_name', 'first_step', 'first_name'}


Examples
========

Filtering results
-----------------
.. code-block:: python
    :caption: Using ``list`` comprehension for result filtering

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]

    setosa = [m for *m,s in DATA if s == 'setosa']
    # [
    #   [5.1, 3.5, 1.4, 0.2],
    #   [4.7, 3.2, 1.3, 0.2],
    # ]

Filtering with complex expressions
----------------------------------
.. code-block:: python
    :caption: Using ``list`` comprehension for result filtering with more complex expression

    DATA = [
        ('Sepal length', 'Sepal width', 'Petal length', 'Petal width', 'Species'),
        (5.8, 2.7, 5.1, 1.9, 'virginica'),
        (5.1, 3.5, 1.4, 0.2, 'setosa'),
        (5.7, 2.8, 4.1, 1.3, 'versicolor'),
        (6.3, 2.9, 5.6, 1.8, 'virginica'),
        (6.4, 3.2, 4.5, 1.5, 'versicolor'),
        (4.7, 3.2, 1.3, 0.2, 'setosa'),
        (7.0, 3.2, 4.7, 1.4, 'versicolor'),
    ]


    def is_setosa(species):
        if species == 'setosa':
            return True
        else:
            return False


    measurements = [m for *m,s in DATA if is_setosa(s)]
    # [
    #   [5.1, 3.5, 1.4, 0.2],
    #   [4.7, 3.2, 1.3, 0.2],
    # ]

Quick parsing lines
-------------------
.. code-block:: python
    :caption: Quick parsing lines

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

    output = []

    for row in DATA:
        row = row.split(',')
        output.append(row)


    print(output)
    # [
    #   ['5.8', '2.7', '5.1', '1.9', 'virginica'],
    #   ['5.1', '3.5', '1.4', '0.2', 'setosa'],
    #   ['5.7', '2.8', '4.1', '1.3', 'versicolor']
    # ]

.. code-block:: python
    :caption: Quick parsing lines

    DATA = [
        '5.8,2.7,5.1,1.9,virginica',
        '5.1,3.5,1.4,0.2,setosa',
        '5.7,2.8,4.1,1.3,versicolor',
    ]

    output = [row.split(',') for row in DATA]

    print(output)
    # [
    #   ['5.8', '2.7', '5.1', '1.9', 'virginica'],
    #   ['5.1', '3.5', '1.4', '0.2', 'setosa'],
    #   ['5.7', '2.8', '4.1', '1.3', 'versicolor']
    # ]

Reversing ``dict`` keys with values
-----------------------------------
.. code-block:: python
    :caption: Reversing ``dict`` keys with values

    DATA = {'a': 1, 'b': 2}

    DATA.items()
    # [
    #    ('a', 1),
    #    ('b', 2),
    # ]

.. code-block:: python
    :caption: Reversing ``dict`` keys with values

    DATA = {'a': 1, 'b': 2}

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'b'}

.. code-block:: python
    :caption: Value collision while reversing ``dict``

    DATA = {'a': 1, 'b': 2, 'c': 2}

    {v:k for k,v in DATA.items()}
    # {1:'a', 2:'c'}


Assignments
===========

Split train/test
----------------
* Complexity level: easy
* Lines of code to write: 8 lines
* Estimated time of completion: 15 min
* Filename: :download:`solution/comprehension_split_train_test.py`

:English:
    #. For given data structure ``INPUT: List[tuple]`` (see below)
    #. Separate header from data
    #. Calculate pivot point: length of data times given percent
    #. Using List Comprehension split data to:

        * ``features: List[Tuple[float]]`` - list of measurements (each measurement row is a tuple)
        * ``labels: List[str]`` - list of species names

    #. Split those data structures with proportion:

        * ``features_train: List[Tuple[float]]`` - features to train - 60%
        * ``features_test: List[Tuple[float]]`` - features to test - 40%
        * ``labels_train: List[str]`` - labels to train - 60%
        * ``labels_test: List[str]`` - labels to test - 40%

    #. Create ``OUTPUT: Tuple[list, list, list, list]`` with features (training and test) and labels (training and test)
    #. Print ``OUTPUT``

:Polish:
    #. Dana jest struktura danych ``INPUT: List[tuple]`` (patrz poniżej)
    #. Odseparuj nagłówek do danych
    #. Wylicz punkt podziału: długość danych razy zadany procent
    #. Używając List Comprehension podziel dane na:

        - ``features: List[Tuple[float]]`` - lista pomiarów (każdy wiersz z pomiarami ma być tuple)
        - ``labels: List[str]`` - lista nazw gatunków

    #. Podziel te struktury danych w proporcji:

        - ``features_train: List[Tuple[float]]`` - features do uczenia - 60%
        - ``features_test: List[Tuple[float]]`` - features do testów - 40%
        - ``labels_train: List[str]`` - labels do uczenia - 60%
        - ``labels_test: List[str]`` - labels do testów - 40%

    #. Stwórz ``OUTPUT: Tuple[list, list, list, list]`` z cechami (treningowymi i testowymi) oraz labelkami (treningowymi i testowymi)
    #. Wypisz ``OUTPUT``

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
            (4.9, 2.5, 4.5, 1.7, 'virginica'),
            (7.1, 3.0, 5.9, 2.1, 'virginica'),
            (4.6, 3.4, 1.4, 0.3, 'setosa'),
            (5.4, 3.9, 1.7, 0.4, 'setosa'),
            (5.7, 2.8, 4.5, 1.3, 'versicolor'),
            (5.0, 3.6, 1.4, 0.3, 'setosa'),
            (5.5, 2.3, 4.0, 1.3, 'versicolor'),
            (6.5, 3.0, 5.8, 2.2, 'virginica'),
            (6.5, 2.8, 4.6, 1.5, 'versicolor'),
            (6.3, 3.3, 6.0, 2.5, 'virginica'),
            (6.9, 3.1, 4.9, 1.5, 'versicolor'),
            (4.6, 3.1, 1.5, 0.2, 'setosa'),
        ]

:The whys and wherefores:
    * Iterating over nested data structures
    * Using slices
    * Type casting
    * List comprehension
    * Magic Number