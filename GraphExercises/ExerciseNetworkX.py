import networkx as nx
import matplotlib.pyplot as plt

graph1 = nx.DiGraph()
graph2 = nx.DiGraph()
graph3 = nx.Graph()

associative_matrix1 = [
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0]
]

associative_matrix2 = [
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 0, 0, 1],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

associative_matrix3 = [
    [0, 6, 2, 3, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 7, 9],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0]
]

for i in range(0, len(associative_matrix1)):
    graph1.add_node(i)

for i in range(0, len(associative_matrix2)):
    graph2.add_node(i)

for i in range(0, len(associative_matrix3)):
    graph3.add_node(i)

for i in range(0, len(associative_matrix1)):
    for j in range(0, len(associative_matrix1[i])):
        if associative_matrix1[i][j] == 1:
            graph1.add_edge(i, j)

for i in range(0, len(associative_matrix2)):
    for j in range(0, len(associative_matrix2[i])):
        if associative_matrix2[i][j] == 1:
            graph2.add_edge(i, j)

for i in range(0, len(associative_matrix3)):
    for j in range(0, len(associative_matrix3[i])):
        if associative_matrix3[i][j] > 0:
            graph3.add_edge(i, j, weight=associative_matrix3[i][j])

print("Graph 1: ", graph1.nodes)
print("Graph 1: ", graph1.edges)

print("Graph 2: ", graph2.nodes)
print("Graph 2: ", graph2.edges)

print("Graph 3: ", graph3.nodes)
print("Graph 3: ", graph3.edges)

print('\n\n\n')

print("DFS - Graph 1: ", list(nx.dfs_edges(graph1, source = 0)))
print("BFS - Graph 2: ", list(nx.bfs_edges(graph2, source = 0)))
print("Dijkstra - Graph 3: ", list(nx.dijkstra_path(graph3, 0, 5)), "Length: : ", nx.dijkstra_path_length(graph3, 0, 5))

plt.subplot(121)
nx.draw(graph1)

plt.subplot(122)
nx.draw(graph2)

plt.show()