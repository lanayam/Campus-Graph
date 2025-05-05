from graph import campus_graph
from shortest_path import dijkstra, get_shortest_path
from span_tree import prim_mst
from string_matching import search_buildings
import heapq

def display_shortest_path():
    print("\n--- Shortest Path ---")
    start = input("Enter the start building code (e.g., PL, TSU, H): ").strip().upper()
    end = input("Enter the destination building code (e.g., PL, TSU, H): ").strip().upper()

    # Create campus graph
    G = campus_graph()

    # Run Dijkstra's algorithm to find the shortest path
    distances, predecessors = dijkstra(G, start)
    if distances[end] == float('inf'):
        print(f"No path found from {start} to {end}.")
    else:
        path = get_shortest_path(predecessors, start, end)
        print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
        print(f"Path distance: {distances[end]}")


def search_for_buildings():
    print("\n--- Search for Buildings ---")
    query = input("Enter part of the building name to search: ").strip()
    matches = search_buildings(query)
    
    if matches:
        print("Found the following buildings:")
        for code, name in matches:
            print(f"{code}: {name}")
    else:
        print("No buildings found.")


def main():
    while True:
        print("\n--- Smart Campus Navigation & Task Scheduler ---")
        print("1. Find shortest path between buildings")
        print("2. Task Scheduler")
        print("3. Search for buildings")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            display_shortest_path()
        elif choice == '2':
            task_scheduler()
        elif choice == '3':
            search_for_buildings()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()