**************************
Multiple figures and plots
**************************


Multiple Plots on one Figure
============================
.. code-block:: python

    import matplotlib.pyplot as plt
    import numpy as np


    x1 = [x * 0.01 for x in range(0, 628)]
    y1 = [np.sin(x * 0.01) + np.random.normal(0.0, 0.1) for x in range(0, 628)]

    x2 = [x * 0.5 for x in range(0, round(63 / 5))]
    y2 = [np.cos(x * 0.5) for x in range(0, round(63 / 5))]

    plt.plot(x1, y1)
    plt.plot(x2, y2, 'o-')

    plt.show()

.. figure:: img/multi-sine.png
    :scale: 100%
    :align: center


Multiple Figures with single Plots
==================================
.. code-block:: python

    import numpy as np
    import matplotlib.pyplot as plt

    def func(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, func(t1), 'bo', t2, func(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.show()

.. figure:: img/matplotlib-plt-subplot.png
    :scale: 100%
    :align: center

    Working with multiple figures and axes


Multiple Charts in Grid
=======================
.. literalinclude:: src/matplotlib-multiple-charts.py
    :language: python
    :caption: Multiple Charts in Grid

.. figure:: img/subplot-multiple.png
    :scale: 100%
    :align: center


``plt.plot()`` vs ``ax.plot()``
===============================
* https://stackoverflow.com/questions/43482191/matplotlib-axes-plot-vs-pyplot-plot

.. code-block:: python

    fig = plt.figure()
    plt.plot(data)
    fig.show()

#. Takes the current figure and axes (if none exists it will create a new one) and plot into them:

    .. code-block:: python

        line = plt.plot(data)

#. In your case, the behavior is same as before with explicitly stating the axes for plot:

    .. code-block:: python

        ax = plt.axes()
        line = ax.plot(data)

#. This approach of using ``ax.plot(...)`` is a must, if you want to plot into multiple axes (possibly in one figure). For example when using a subplots. Explicitly creates new figure - you will not add anything to previous one. Explicitly creates a new axes with given rectangle shape and the rest is the same as with 2:

    .. code-block:: python

        fig = plt.figure()
        ax = fig.add_axes([0,0,1,1])
        line = ax.plot(data)

    possible problem using ``figure.add_axes`` is that it may add a new axes object to the figure, which will overlay the first one (or others). This happens if the requested size does not match the existing ones.
