import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize


def f1(x, b0, b1, b2):
    return b0 + b1 * np.exp(-b2 * x ** 2)


def g1(beta):
    return y_data - f1(x_data, *beta)


def f2(x, a, b, c):
    return np.sin(a * x + b) + c


def g2(abc):
    return y_data - f2(x_data, *abc)


if __name__ == '__main__':
    x_data = np.fromfile("x3.txt", float, sep='\n')
    y_data = np.fromfile("y3.txt", float, sep='\n')

    start_values = np.array((1, 1, 1))

    beta = scipy.optimize.leastsq(g1, start_values)[0]
    y1 = f1(x_data, *beta)

    abc = scipy.optimize.curve_fit(f2, x_data, y_data)[0]
    y2 = f2(x_data, *abc)

    fig, ax = plt.subplots()
    ax.scatter(x_data, y_data, c='cadetblue', label='Початкові дані')
    ax.plot(x_data, y1, 'greenyellow', label='Крива 1')
    ax.plot(x_data, y2, 'orange', label='Крива 2')
    ax.legend()
    ax.set_xlabel(r'$x$', fontsize=18)
    ax.set_ylabel(r'$f(x, \beta)$', fontsize=18)
    plt.show()
