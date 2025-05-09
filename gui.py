import customtkinter as ctk
from task_scheduler import activity_selection
from sorting import quick_sort

# appearance settings
ctk.set_appearance_mode("light")  # or "dark"
ctk.set_default_color_theme("green")  # built-in themes: "blue", "green", "dark-blue"

# app setup
app = ctk.CTk()
app.title("✨ CSUF Task Scheduler ✨")

activities = []

# Add task
def add_task():
    name = entry_name.get()
    start = float(entry_start.get())
    end = float(entry_end.get())
    priority = int(entry_priority.get()) if entry_priority.get() else 0

    activities.append({
        "name": name,
        "start": start,
        "end": end,
        "priority": priority
    })

    # clear inputs
    entry_name.delete(0, ctk.END)
    entry_start.delete(0, ctk.END)
    entry_end.delete(0, ctk.END)
    entry_priority.delete(0, ctk.END)

    update_task_display(activities)

# Update display
def update_task_display(activity_list):
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")
    for act in activity_list:
        textbox.insert("end", f"{act['name']} ({act['start']}-{act['end']}) P:{act['priority']}\n")
    textbox.configure(state="disabled")

# Sort tasks
def sort_tasks():
    key = sort_option.get()
    sorted_list = quicksort_tasks(activities, key)
    update_task_display(sorted_list)

# Optimize
def optimize_schedule():
    optimized = activity_selection(activities)
    update_task_display(optimized)

# GUI widgets
entry_name = ctk.CTkEntry(app, placeholder_text="Task Name")
entry_start = ctk.CTkEntry(app, placeholder_text="Start Time")
entry_end = ctk.CTkEntry(app, placeholder_text="End Time")
entry_priority = ctk.CTkEntry(app, placeholder_text="Priority (Optional)")

entry_name.pack(padx=10, pady=5)
entry_start.pack(padx=10, pady=5)
entry_end.pack(padx=10, pady=5)
entry_priority.pack(padx=10, pady=5)

ctk.CTkButton(app, text="Add Task", command=add_task).pack(pady=5)

sort_option = ctk.CTkOptionMenu(app, values=["start", "end", "priority"])
sort_option.set("start")
sort_option.pack(pady=5)

ctk.CTkButton(app, text="Sort Tasks", command=sort_tasks).pack(pady=5)
ctk.CTkButton(app, text="Optimize Schedule", command=optimize_schedule).pack(pady=5)

textbox = ctk.CTkTextbox(app, width=400, height=200)
textbox.pack(padx=10, pady=10)

app.mainloop()
