# Campus-Graph
Smart Campus Navigation and Task Scheduler

**Objective**: Develop a system to assist CSUF students in navigating the campus efficiently
and managing their daily tasks.


**Key Features**:
• Graph Representation: Model the campus as a graph where buildings are nodes and pathways are edges. Use adjacency lists or matrices.

• Shortest Path Algorithm: Implement Dijkstra’s algorithm to find the shortest path between two buildings. Refer to dijkstra algorithm.py.

• Minimum Spanning Tree (MST): Use Prim’s or Kruskal’s algorithm to determine optimal maintenance routes covering all buildings. See prim algorithm.py and
kruskal algorithm.py.

• Task Scheduling: Apply the Activity Selection Problem (greedy approach) to schedule tasks without overlaps. Refer to activity selection.py.

• String Matching: Implement KMP or Boyer-Moore algorithms to search for building names or room numbers. See kmp algorithm.py and boyer moore.py.

• Sorting: Use Merge Sort or Quick Sort to organize tasks by priority or time. Refer to merge sort.py and quick sort.py.


**Hints**:

• Start by mapping out a simplified version of the campus with 5–10 buildings.

• Create sample data for student schedules and tasks.

• Visualize the graph using libraries like networkx and matplotlib.

• Ensure modular code for each algorithm to facilitate testing and integration.
**Expected Outcomes:**

• A user interface (CLI or GUI) allowing input of current location and desired destination, displaying the shortest path.

• A scheduler that inputs tasks with start and end times and outputs an optimized, non-overlapping schedule.

• Search functionality to find specific buildings or rooms.

• Sorted list of tasks based on user-defined criteria.
