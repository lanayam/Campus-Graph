#
# Output of the full Spanning Tree of graph.py
#

import heapq
from graph import campus_graph #import the graph structure

def prim_mst(graph): 
    nodes = list(graph.nodes) #get a list of all nodes in the graph
    visited = {node: False for node in nodes} #track nodes
    start_node = nodes[0] 

    min_heap = [(0, start_node, None)] #select the smallest edge weight at each step
    total_cost = 0
    mst_edges = []

    while min_heap: #prim's algorithm main loop
        weight, current_node, from_node = heapq.heappop(min_heap) 

        if visited[current_node]:
            continue
    #mark nodes as visited
        visited[current_node] = True
        total_cost += weight

        if from_node:
            mst_edges.append((from_node, current_node, weight))
    #look at all unvisited neighbors and add to heap
        for neighbor in graph.neighbors(current_node):
            if not visited[neighbor]:
                edge_weight = graph[current_node][neighbor]['weight']
                heapq.heappush(min_heap, (edge_weight, neighbor, current_node))

    return total_cost, mst_edges

if __name__ == "__main__":
    G = campus_graph()
    cost, edges = prim_mst(G)
    print("Minimum cost to connect all buildings:", cost)
    print("Edges in MST:")
    for u, v, w in edges:
        print(f"{u} -- {v} (weight {w})")