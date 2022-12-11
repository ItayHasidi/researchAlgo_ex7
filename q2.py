import networkx as nx
import matplotlib.pyplot as plt
from q1 import average_calc

draw_options = {
    "font_size": 10,
    "node_size": 700,
    "node_color": "red",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 1,
    "with_labels": True
}


def print_graph(G):
    for u, v, attr in G.edges.data('weight'):
        print(f'node1 = {u}, node2 = {v} , weight = {attr:.3}')


def random_graph(num_of_nodes, probability_of_edge):
    G = nx.erdos_renyi_graph(num_of_nodes, probability_of_edge, seed=123, directed=False)
    for (u, v) in G.edges():
        G.edges[u, v]['weight'] = 1.0
    # for v in range(1, len(G.nodes())):
    #     if G.degree[v] == 0:
    #         G.add_edge(v, 1, weight=1) if v != 1 else G.add_edge(v, 2, weight=1)
    return G


def compare_approx_to_exact():
    approx = []
    exact = []
    iterations = 100
    for nodes in range(4, iterations):
        prob = 0.1
        while prob <= 0.9:
            G = random_graph(nodes, prob)
            # nx.draw(G,  **draw_options)
            # plt.show()
            if nx.is_connected(G):
                approx.append(nx.approximation.diameter(G))
                exact.append(nx.diameter(G))
            # if approx != exact:
            #     print("nodes: "+str(nodes)+", prob: "+str(prob)+", exact: "+str(exact)+", approx: "+str(approx))
            prob += 0.1
    fig, axs = plt.subplots(3, 3, figsize=(9, 9), constrained_layout=True)
    print(f'exact: {exact}\napprox: {approx}')
    # fig, axs = plt.subplots(1, 3, figsize=(9, 3), sharey=True)

    for ax, prob in zip(axs.flat, [.1, .2, .3, .4, .5, .6, .7, .8, .9]):
        ax.set_title(f'probability={prob}')
        ax.plot(range(4, 828), average_calc(exact), label="exact")
        ax.plot(range(4, 828), average_calc(approx), label="approx")
        ax.set_ylabel("approximation")
        ax.set_xlabel("number of nodes")
        ax.legend()

    # prob = 0.1
    # i = 0
    # while prob <= 0.9:
    #     axs[i].plot(range(4, 54), exact, label="exact")
    #     axs[i].plot(range(4, 54), approx, label="approx")
    # plt.ylabel("probability")
    # plt.xlabel("number of nodes")
    # plt.legend()
    #     # axs[i].suptitle("prob. ", prob)
    #     prob += 0.1
    #     i += 1

    plt.show()


compare_approx_to_exact()
# print("G graph:")
# print_graph(G)
# nx.draw(G,  **draw_options)
# plt.show()

# nx.approximation.diameter()
# nx.diameter()
