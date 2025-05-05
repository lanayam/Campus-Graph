# Dev: Alex I
#
# Dijkstra's algorithm
# shortest path between two buildings  
#

def dijkstra(graph, start, end):
    import heapq  # For priority queue

    # Priority queue to hold (distance, node)
    queue = [(0, start)] 
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    previous_nodes = {}

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        # Stop if we reached destination
        if current_node == end:
            break

        # Explore neighbors
        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight

            # If found a shorter path to neighbor, update distances and previous nodes
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    # Reconstruct the shortest path, if it exists
    path = []
    current = end
    while current in previous_nodes:
        path.insert(0, current)
        current = previous_nodes[current]
    if path:
        path.insert(0, start)

    return path, distances[end]