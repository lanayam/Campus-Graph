from task_scheduler import *

# Now converting AM/PM to 24-hour format 
def parse_time_input(time_str):
    try:
        time_str = time_str.strip().lower()                     # makes input lowercase

        if "am" in time_str:
            time = int(time_str.replace("am", "").strip())      # removes 'am' or 'pm' and converts it to int
            return time if time != 12 else 0                    # 12 AM is set to 0 (used later)

        elif "pm" in time_str:
            time = int(time_str.replace("pm", "").strip()) 
            return time if time == 12 else time + 12            # 12PM is 12 and anything else is added 12 (24 hour format conversion)

        else:
            raise ValueError("Missing AM/PM")

    except:
        print("Invalid time format. Use '12PM' or '10AM'.")
        return None


# Formatting time back to AM/PM so it is readable

def format_time(hour):
    if hour == 0:
        return "12 AM"

    elif 1 <= hour < 12:
        return f"{hour} AM"

    elif hour == 12:
        return "12 PM"

    else:
        return f"{hour - 12} PM"


# When program starts, this function gets called
# It gets user input, then parses and stores tasks - sorts them - then outputs
def schedule_tasks():
    num_of_tasks = int(input("Enter the number of tasks: "))
    activities = []

    for _ in range(num_of_tasks):
        name = input("Enter a task name: ")

        while True:
            start_input = input(f"Enter start time for {name} (e.g. 10 AM): ")
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

        # Stores the tasks as a dict
        activities.append({"name": name, "start": start, "end": end, "priority": priority})

    # Given the option to sort the tasks 3 different ways
    sort_key = input("Sort by 'start', 'end', or 'priority' (default = 'end'): ").lower()
    if sort_key not in ["start", "end", "priority"]:
        sort_key = "end"

    result = run_scheduler(activities, key=sort_key)

    print(f"\nNon-overlapping Tasks (sorted by {sort_key}):")

    for task in result:
        print(f"{task['name']} ({format_time(task['start'])}–{format_time(task['end'])})  P:{task['priority']}")

if __name__ == "__main__":
    schedule_tasks()