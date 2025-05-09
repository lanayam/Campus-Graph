# Select as many tasks as possible that don't overlap
# Greedy Strategy
    # Will always pick the task that ends the earliest (to help with the time constraint)

from sorting import quick_sort

def activity_selection(activities):

    selected = []
    last_end = -1

    for activity in activities:
        if activity["start"] >= last_end:
            selected.append(activity)
            last_end = activity["end"]

    return selected

# Function combines sorting & scheduling
def run_scheduler(activities, key="end"):
    sorted_tasks = quick_sort(activities, key)
    return activity_selection(sorted_tasks)
