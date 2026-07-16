import numpy as np


def exo1():
    number = [5, 10, 15, 20, 25]
    number = np.array(number)
    print(number)


def exo2():
    print(np.zeros(8, int))


def exo3():
    print(np.ones((4, 3), int))


def exo4():
    print(np.full((5, 5), 9))


def exo5():
    print(np.arange(10, 30, 5))


def exo6():
    print(np.linspace(0, 1, 11))


def exo7():
    print(np.linspace(100, 109, 10, dtype=int))


