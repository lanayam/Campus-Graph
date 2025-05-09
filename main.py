#Dev: Alex I and Lizabeth
#
# main file to test everything is working correctly.
#
# This file will test the other files if they are working.
# Asks when ran to run in cmd or open GUI.

import sys

# Core functions
from task_scheduler import run_scheduler
from sorting import quick_sort
from string_matching import kmp_search
from shortest_path import dijkstra
from graph import campus_graph

# --- Utility Functions ---

def parse_time_input(time_str):
    try:
        time_str = time_str.strip().lower()
        if "am" in time_str:
            time = int(time_str.replace("am", "").strip())
            return time if time != 12 else 0
        elif "pm" in time_str:
            time = int(time_str.replace("pm", "").strip())
            return time if time == 12 else time + 12
        else:
            raise ValueError("Missing AM/PM")
    except:
        print("Invalid time format. Use '10 AM' or '3 PM'.")
        return None

def format_time(hour):
    if hour == 0:
        return "12 AM"
    elif 1 <= hour < 12:
        return f"{hour} AM"
    elif hour == 12:
        return "12 PM"
    else:
        return f"{hour - 12} PM"

# --- CLI Testing Functions ---

def schedule_tasks_cli():
    try:
        num_of_tasks = int(input("Enter the number of tasks: "))
    except ValueError:
        print("Invalid number.")
        return

    activities = []

    for _ in range(num_of_tasks):
        name = input("Enter task name: ")

        while True:
            start_input = input(f"Enter start time for {name} (e.g., 10 AM): ")
            start = parse_time_input(start_input)
            if start is not None:
                break

        while True:
            end_input = input(f"Enter end time for {name}: ")
            end = parse_time_input(end_input)
            if end is not None:
                break

        priority_input = input(f"Enter priority for {name} (default = 0): ")
        priority = int(priority_input) if priority_input.strip() else 0

        activities.append({"name": name, "start": start, "end": end, "priority": priority})

    sort_key = input("Sort by 'start', 'end', or 'priority' (default = 'end'): ").lower()
    if sort_key not in ["start", "end", "priority"]:
        sort_key = "end"

    result = run_scheduler(activities, key=sort_key)

    print(f"\nNon-overlapping Tasks (sorted by {sort_key}):")
    for task in result:
        print(f"{task['name']} ({format_time(task['start'])}–{format_time(task['end'])})  P:{task['priority']}")

def test_class_search():
    building_names = [
        "Pollak Library", "McCarthy Hall", "Titan Student Union", "Humanities",
        "Gordon Hall", "Computer Science", "Engineering", "Kinesiology",
        "Langsdorf Hall", "Eastside Parking", "Nutwood Parking", "State College Parking"
    ]
    pattern = input("Enter search pattern (e.g. 'Hall'): ").strip()
    matches = []

    for name in building_names:
        if kmp_search(name.lower(), pattern.lower()):
            matches.append(name)

    print("\nMatches found:")
    for match in matches:
        print("-", match)

def test_shortest_path():
    graph = campus_graph()
    print("Available buildings:", list(graph.nodes))
    start = input("Enter start building code (e.g., PL): ").strip().upper()
    end = input("Enter destination building code: ").strip().upper()

    if start not in graph or end not in graph:
        print("Invalid building code.")
        return

    path, distance = dijkstra(graph, start, end)
    if path:
        print("Shortest path:", " → ".join(path))
        print("Total distance:", distance)
    else:
        print("No path found.")

def test_sorting():
    tasks = [
        {"name": "A", "start": 10, "end": 12, "priority": 2},
        {"name": "B", "start": 9, "end": 11, "priority": 3},
        {"name": "C", "start": 11, "end": 13, "priority": 1}
    ]
    key = input("Sort by 'start', 'end', or 'priority': ").strip().lower()
    sorted_tasks = quick_sort(tasks, key)
    print("\nSorted tasks:")
    for t in sorted_tasks:
        print(f"{t['name']}: {key} = {t[key]}")
#Broken :/
def run_gui():
    import tkinter as tk
    from gui import CampusNavigator  # Import the CampusNavigator class
    root = tk.Tk()
    app = CampusNavigator(root)  # Initialize the CampusNavigator class
    root.mainloop()

# --- Main Menu ---

def main_menu():
    while True:
        print("\n--- Campus Assistant ---")
        print("1. Launch GUI")
        print("2. Run Task Scheduler")
        print("3. Run Class Search (String Matching)")
        print("4. Run Shortest Path (Dijkstra)")
        print("5. Run Custom Sort Test")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            run_gui()
        elif choice == "2":
            schedule_tasks_cli()
        elif choice == "3":
            test_class_search()
        elif choice == "4":
            test_shortest_path()
        elif choice == "5":
            test_sorting()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main_menu()