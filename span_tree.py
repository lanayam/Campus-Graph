import heapq
from graph import campus_graph

def prim_mst(graph): 
    nodes = list(graph.nodes)
    visited = {node: False for node in nodes}
    start_node = nodes[0]

    min_heap = [(0, start_node, None)] 
    total_cost = 0
    mst_edges = []

    while min_heap:
        weight, current_node, from_node = heapq.heappop(min_heap) 

        if visited[current_node]:
            continue

        visited[current_node] = True
        total_cost += weight

        if from_node:
            mst_edges.append((from_node, current_node, weight))

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