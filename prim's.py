# Use a programming language of your choice to implement the algorithm (Prim's algorithm).

import sys

# adjacency matrix method
vertices = 7
input_graph = [
    [0, 28, 0, 0, 0, 10, 0], 
    [28, 0, 16, 0, 0, 0, 14],
    [0, 16, 0, 12, 0, 0, 0], 
    [0, 0, 12, 0, 0, 0, 18],
    [0, 0, 0, 22, 0, 25, 24], 
    [10, 0, 0, 0, 25, 0, 0],
    [0, 14, 0, 18, 24, 0, 0]
]

# initialize all key values as INT_MAX
key_values = [sys.maxsize] * 7
selected_node = [False] * 7

# assign key value as 0 for the first vertex so that it is picked first
key_values[5] = 0
selected_node[5] = True

# print edge and weight
print('\nEdge \tWeight\n')

edges = 0 
weight_sum = 0

# loop through all the edges in input graph
while edges < vertices - 1:
    minimum = sys.maxsize
    a = 0
    b = 0
    # loop through vertices in input graph
    for i in range(vertices):
        # split first set of vertices included in MST
        if selected_node[i]:
            # split second set of vertices not yet included in MST
            for j in range(vertices):
                # check edge connecting two sets
                # if unselected vertex and there is an edge
                if ((not selected_node[j]) and input_graph[i][j]):
                    # pick minimum weight edge
                    if minimum > input_graph[i][j]: 
                        minimum = input_graph[i][j]
                        a = i
                        b = j

    weight_sum += input_graph[a][b]
    # print edges and weights
    print(str(a + 1) + " -> " + str(b + 1) + " \t " + str(input_graph[a][b]))

    # update first set included in MST
    selected_node[b] = True
    edges += 1

print("\nSum of weights:", weight_sum)
print('\n')
