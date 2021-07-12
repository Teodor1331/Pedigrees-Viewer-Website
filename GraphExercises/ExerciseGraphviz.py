from graphviz import Digraph

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

graph1 = Digraph("Name Graph DFS", filename = "DepthFirstSearch.gv")
graph2 = Digraph("Name Graph BFS", filename = "BreadthFirstSearch.gv")

for i in range(0, len(associative_matrix1)):
    graph1.node(str(i))
    
for i in range(0, len(associative_matrix2)):
    graph2.node(str(i))

for i in range(0, len(associative_matrix1)):
    for j in range(0, len(associative_matrix1[i])):
        if associative_matrix1[i][j] == 1:
            graph1.edge(str(i), str(j))

for i in range(0, len(associative_matrix2)):
    for j in range(0, len(associative_matrix2[i])):
        if associative_matrix2[i][j] == 1:
            graph2.edge(str(i), str(j))

list_attributes1 = graph1.body
list_attributes2 = graph2.body

print(graph1.source)
print(graph2.source)

graph1.render('DepthFirstSearch.gv', view=True)
graph2.render("BredthFirstSearch.gv", view=True)

list_edges1 = []
list_edges2 = []

adjency_list11 = {}
adjency_list21 = {}
adjency_list12 = {}
adjency_list22 = {}


for i in range(len(list_attributes1)):
    string = str(list_attributes1[i]).replace('\t', '')
    list_attributes1[i] = string

for i in range(len(list_attributes2)):
    string = str(list_attributes2[i]).replace('\t', '')
    list_attributes2[i] = string

print(list_attributes1)
print(list_attributes2)

for i in range(len(list_attributes1)):
    if list_attributes1[i].find("->") == 2:
        list_edges1.append(list_attributes1[i])

for i in range(len(list_attributes2)):
    if list_attributes2[i].find("->") == 2:
        list_edges2.append(list_attributes2[i])

print(list_edges1)
print(list_edges2)


for i in range(0, len(associative_matrix1)):
    adjency_list11[i] = []
    adjency_list12[i] = []

for i in range(0, len(associative_matrix2)):
    adjency_list21[i] = []
    adjency_list22[i] = []

for i in range(0, len(list_edges1)):
    adjency_list11[int(list_edges1[i][0])].append(int(list_edges1[i][len(list_edges1[i]) - 1]))

for i in range(0, len(list_edges2)):
    adjency_list21[int(list_edges2[i][0])].append(int(list_edges2[i][len(list_edges2[i]) - 1]))

print(adjency_list11)
print(adjency_list21)

for i in range(0, len(associative_matrix1)):
    for j in range(0, len(associative_matrix1[i])):
        if associative_matrix1[i][j] == 1:
            adjency_list12[i].append(j)


for i in range(0, len(associative_matrix2)):
    for j in range(0, len(associative_matrix2[i])):
        if associative_matrix2[i][j] == 1:
            adjency_list22[i].append(j)

print(adjency_list12)
print(adjency_list22)