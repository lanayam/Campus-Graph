import networkx as nx
from graph import campus_graph
from shortest_path import dijkstra
from task_scheduler import activity_selection
from string_matching import kmp_search

def display_shortest_path():
    # Get input for current location and destination
    start_location = input("Enter current location (building name): ")
    end_location = input("Enter desired destination (building name): ")
    
    # Get the campus graph
    graph = campus_graph()
    
    # Find the shortest path
    path, distance = dijkstra(graph, start_location, end_location)
    
    if path:
        print(f"Shortest path from {start_location} to {end_location}:")
        print(" -> ".join(path))
        print(f"Path distance: {distance}")
    else:
        print(f"No path found between {start_location} and {end_location}")

def schedule_tasks():
    # Get input for tasks
    num_tasks = int(input("Enter the number of tasks: "))
    activities = []
    
    for _ in range(num_tasks):
        name = input("Enter task name: ")
        start = int(input(f"Enter start time for {name}: "))
        end = int(input(f"Enter end time for {name}: "))
        activities.append({"name": name, "start": start, "end": end})
    
    # Select non-overlapping tasks using the Activity Selection Problem
    selected_tasks = activity_selection(activities)
    
    print("\nSelected non-overlapping tasks:")
    for task in selected_tasks:
        print(f"{task['name']} (Start: {task['start']}, End: {task['end']})")

def search_building():
    # Get input for building search
    text = "PL MH TSU H GH CS E KHS LH ENPNS NPS SCPS"  # Example campus buildings list
    pattern = input("Enter building name or room number to search for: ")

    # Perform KMP search
    matches = kmp_search(text, pattern)
    
    if matches:
        print(f"Found '{pattern}' at positions: {matches}")
    else:
        print(f"'{pattern}' not found in the building list.")

def sort_tasks():
    # Get input for sorting tasks
    num_tasks = int(input("Enter the number of tasks: "))
    activities = []
    
    for _ in range(num_tasks):
        name = input("Enter task name: ")
        start = int(input(f"Enter start time for {name}: "))
        end = int(input(f"Enter end time for {name}: "))
        activities.append({"name": name, "start": start, "end": end})
    
    # Sort tasks by start time 
    activities.sort(key=lambda x: x["start"])

    print("\nSorted tasks by start time:")
    for task in activities:
        print(f"{task['name']} (Start: {task['start']}, End: {task['end']})")

def main():
    while True:
        print("\nWelcome to the Smart Campus Navigation and Task Scheduler!")
        print("1. Find the shortest path between two buildings")
        print("2. Schedule tasks")
        print("3. Search for a building")
        print("4. Sort tasks by priority or time")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            display_shortest_path()
        elif choice == "2":
            schedule_tasks()
        elif choice == "3":
            search_building()
        elif choice == "4":
            sort_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()