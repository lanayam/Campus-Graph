
# Select as many tasks as possible that don't overlap
# Greedy Strategy
    # Will always pick the task that ends the earliest (to help with the time constraint)

# 1. Sort tasks by end time (ascending) so it ensures that we always consider the next task that ends soonest
    # and there's no overlap!
# 2. Initialize the tasks we've selected (schedule)

def activity_selection(activities):
    # Step 1 : Sort all talks/activities by end time
    activities.sort(key = lambda x: x["end"])

    # Step 2 : Initialize the selected activities list with
        # the first activity
    # selected_activities = [activities[0]] # The first activity is always selected
    # last_selected = activities[0] # Keeping track of last selected activity
    selected = []
    last_end = -1

    # Step 3: Iterate through the remaining activities
    for activity in activities:
        # Step 4: Check if the start time of the current activity is after...
        if activity["start"] >= last_end:
            selected.append(activity)
            last_end = activity["end"]

    return selected

# Small data example for now

activities = [
    {"name": "Study", "start": 8, "end": 9},
    {"name": "Lecture", "start": 9, "end": 10},
    {"name": "Gym", "start": 10, "end": 11}

]

selected = activity_selection(activities)
for task in selected:
    print(task["name"], task["start"], task["end"])

print("Max set of non-overlapping activities:", len(selected))
    
