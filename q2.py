import networkx as nx
import matplotlib.pyplot as plt
# from q1 import average_calc

draw_options = {
    "font_size": 10,
    "node_size": 700,
    "node_color": "red",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 1,
    "with_labels": True
}


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


def random_graph(num_of_nodes, probability_of_edge):
    """
    Generates a random connected graph using erdos renyi algorithm

    >>> G = random_graph(5, .5)
    >>> nx.is_connected(G)
    True

    >>> G = random_graph(50, .5)
    >>> nx.is_connected(G)
    True
    """
    G = nx.erdos_renyi_graph(num_of_nodes, probability_of_edge, seed=123, directed=False)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = 1.0
    return G


def compare_approx_to_exact():
    """
    Calculates an approximation of a diameter and an exact diameter of a graph and shows the difference
    for each probability in (0.1, 0.2, ..., 0.9)
    """
    approx = []
    exact = []
    iterations = 50
    for nodes in range(4, iterations):
        prob = 0.1
        while prob <= 0.9:
            G = random_graph(nodes, prob)
            if nx.is_connected(G):
                approx.append(nx.approximation.diameter(G))
                exact.append(nx.diameter(G))
            prob += 0.1
    fig, axs = plt.subplots(3, 3, figsize=(9, 9), constrained_layout=True)
    for ax, prob in zip(axs.flat, [.1, .2, .3, .4, .5, .6, .7, .8, .9]):
        ax.set_title(f'probability={prob}')
        ax.plot(range(4, 382), exact, label="exact")
        ax.plot(range(4, 382), approx, label="approx")
        ax.set_ylabel("approximation")
        ax.set_xlabel("number of nodes")
        ax.legend()
    plt.show()


compare_approx_to_exact()
