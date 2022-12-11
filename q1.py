import numpy as np
import cvxpy as cp
import timeit
import matplotlib.pyplot as plt


def average_calc(lst: list):
    """
    Calculates the average of a list

    >>> average_calc([1, 2, 3])
    2.0
    >>> average_calc([-1, 0, 1])
    0.0
    >>> average_calc([1, 0.5, 0.25, 0.125, 0.0625])
    0.3875
    """
    return sum(lst) / len(lst)


def generate_linear_equation(n: int):
    """
    Generates a linear equation of n parameters
    """
    np.random.seed(10)
    y = np.random.randn(n)
    x = np.random.randn(n)
    return x, y


def numpy_solver(x, y):
    """
    Solves a linear equation using numpy lib.
    """
    x = np.array(x)
    y = np.array(y)
    prob = x @ y
    return prob


def cvxpy_solver(x, y):
    """
    Solves a linear equation using cvxpy lib.
    """
    prob = cp.Problem(cp.Minimize(y @ x))
    prob.solve()
    return prob.value


def solve_linear_equation(iterations):
    """
    Solves a randomly generated linear equation using two different libraries: numpy, cvxpy

    >>> x = np.array((1, 2, 3))
    >>> y = np.array((1, 2, 3))
    >>> numpy_ans = numpy_solver(x, y)
    >>> cvxpy_ans = cvxpy_solver(x, y)
    >>> numpy_ans == cvxpy_ans
    True
    >>> x = np.array((1, 2, 3))
    >>> y = np.array((1.2, 2.5, 0.3))
    >>> numpy_ans = numpy_solver(x, y)
    >>> cvxpy_ans = cvxpy_solver(x, y)
    >>> numpy_ans == cvxpy_ans
    True
    >>> numpy_ans = numpy_solver(x, y)
    >>> cvxpy_ans = cvxpy_solver(y, y)
    >>> numpy_ans != cvxpy_ans
    True
    """
    numpy_times = []
    cvxpy_times = []
    for i in range(1, iterations):
        x, y = generate_linear_equation(i)
        start_numpy = timeit.default_timer()
        numpy_solver(x, y)
        stop_numpy = timeit.default_timer()
        numpy_times.append(stop_numpy - start_numpy)
        start_cvxpy = timeit.default_timer()
        cvxpy_solver(x, y)
        stop_cvxpy = timeit.default_timer()
        cvxpy_times.append(stop_cvxpy - start_cvxpy)
    numpy_avg = average_calc(numpy_times)
    cvxpy_avg = average_calc(cvxpy_times)
    print("numpy was better by: " + str(cvxpy_avg / numpy_avg) if numpy_avg <= cvxpy_avg else
          "cvxpy was better by: " + str(numpy_avg / cvxpy_avg))
    plt.plot(range(1, iterations), numpy_times, label="numpy")
    plt.plot(range(1, iterations), cvxpy_times, label="cvxpy")
    plt.ylabel("time")
    plt.xlabel("number of x's")
    plt.legend()
    plt.show()


# solve_linear_equation(1000)
