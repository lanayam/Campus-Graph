#  Dev: Alex I
# 
# gui to display campus map

import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk, ImageDraw
import networkx as nx
import matplotlib.pyplot as plt
import io
from graph import campus_graph
from shortest_path import dijkstra
from string_matching import kmp_search
from task_scheduler import run_scheduler

# --- Global Graph Initialization ---
G, building_names = campus_graph()

# --- Helper Functions ---
def draw_path(path):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))

    # Draw all nodes and edges
    nx.draw(G, pos, with_labels=True, node_color='lightgray', edge_color='gray')

    # Highlight path
    if path:
        edges_in_path = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='orange')
        nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='red', width=2)

    # Save to memory and display on Tkinter canvas
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    return Image.open(buf)

def find_building_matches(user_input):
    buildings = list(G.nodes)
    matches = [b for b in buildings if kmp_search(b.lower(), user_input.lower())]

    # Check full names as well
    for acronym, full_name in building_names.items():
        if kmp_search(full_name.lower(), user_input.lower()):
            matches.append(acronym)

    return matches

# --- GUI Application ---
class CampusNavigator:
    def __init__(self, root):
        self.root = root
        root.title("Campus Navigator")

        # Load static map image
        self.map_image = Image.open("campus_map.png")
        self.tk_map = ImageTk.PhotoImage(self.map_image)
        self.canvas = tk.Canvas(root, width=self.map_image.width, height=self.map_image.height)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_map)
        self.canvas.pack()

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack()

        tk.Button(button_frame, text="Schedule Tasks", command=self.schedule_tasks).pack(side="left")
        tk.Button(button_frame, text="Search for Building", command=self.search_building).pack(side="left")
        tk.Button(button_frame, text="Find Shortest Path", command=self.shortest_path_ui).pack(side="left")

    def schedule_tasks(self):
        popup = tk.Toplevel(self.root)
        popup.title("Task Scheduler")
        popup.attributes("-topmost", True)

        tasks = []

        def add_task():
            name = name_entry.get()
            start = parse_time_input(start_entry.get())
            end = parse_time_input(end_entry.get())
            priority = int(priority_entry.get()) if priority_entry.get().strip() else 0
            if None in (start, end):
                messagebox.showerror("Invalid Input", "Start or end time format incorrect.")
                return
            tasks.append({"name": name, "start": start, "end": end, "priority": priority})
            name_entry.delete(0, 'end')
            start_entry.delete(0, 'end')
            end_entry.delete(0, 'end')
            priority_entry.delete(0, 'end')

        def show_schedule():
            sort_key = sort_var.get()
            result = run_scheduler(tasks, key=sort_key)
            output = "\n".join(f"{t['name']} ({format_time(t['start'])}–{format_time(t['end'])}) P:{t['priority']}" for t in result)
            messagebox.showinfo("Scheduled Tasks", output)

        tk.Label(popup, text="Task Name:").pack()
        name_entry = tk.Entry(popup)
        name_entry.pack()

        tk.Label(popup, text="Start Time (e.g. 10AM):").pack()
        start_entry = tk.Entry(popup)
        start_entry.pack()

        tk.Label(popup, text="End Time (e.g. 12PM):").pack()
        end_entry = tk.Entry(popup)
        end_entry.pack()

        tk.Label(popup, text="Priority (0–5):").pack()
        priority_entry = tk.Entry(popup)
        priority_entry.pack()

        tk.Button(popup, text="Add Task", command=add_task).pack()

        sort_var = tk.StringVar(value="end")
        tk.OptionMenu(popup, sort_var, "start", "end", "priority").pack()
        tk.Button(popup, text="Schedule", command=show_schedule).pack()

    def search_building(self):
        query = simpledialog.askstring("Building Search", "Enter building code or part of it:")
        if query:
            matches = find_building_matches(query)
            if matches:
                messagebox.showinfo("Matches", ", ".join(matches))
            else:
                messagebox.showinfo("No Matches", "No buildings matched that search.")

    def shortest_path_ui(self):
        start = simpledialog.askstring("Path Start", "Enter starting building code:")
        end = simpledialog.askstring("Path End", "Enter destination building code:")

        if start not in G.nodes or end not in G.nodes:
            messagebox.showerror("Error", "One or both buildings not found in graph.")
            return

        path, distance = dijkstra(G, start, end)

        if not path:
            messagebox.showinfo("No Path", f"No path found from {start} to {end}.")
            return

        # Draw the path on the map
        self.display_path_on_map(path)

        messagebox.showinfo("Path Info", f"Shortest path: {' -> '.join(path)}\nTotal distance: {distance}")

    def display_path_on_map(self, path):
        # Load the map image
        map_image = Image.open("campus_map.png")
        draw = ImageDraw.Draw(map_image)

        # Define building coordinates
        building_coords = {
            "PL": (437, 277),
            "MH": (438, 493),
            "TSU": (105, 210),
            "H": (556, 388),
            "GH": (562, 482),
            "CS": (735, 155),
            "E": (675, 155),
            "KHS": (345, 102),
            "LH": (503, 570),
            "ENPNS": (792, 372),
            "NPS": (77, 552),
            "SCPS": (77, 49),
            "B": (285, 194),
            "I": (685, 250),
            "EC": (537, 261),
            "VA": (44, 362),
            "TG": (398, 33),
            "SHCC": (561, 69),
            "GAS": (835, 36),
            "GC": (265, 504),
            "DBH": (385, 570),
            "F": (200, 46)
        }

        # Debug: Print the path and coordinates
        print("Path:", path)
        for i in range(len(path) - 1):
            start = path[i]
            end = path[i + 1]
            coord1 = building_coords.get(start)
            coord2 = building_coords.get(end)
            print(f"Drawing line from {start} ({coord1}) to {end} ({coord2})")

            if coord1 and coord2:
                draw.line([coord1, coord2], fill="red", width=4)
                draw.ellipse((coord1[0]-5, coord1[1]-5, coord1[0]+5, coord1[1]+5), fill="blue")
                draw.ellipse((coord2[0]-5, coord2[1]-5, coord2[0]+5, coord2[1]+5), fill="blue")

        # Display the map with the path
        self.tk_map = ImageTk.PhotoImage(map_image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.tk_map)
        self.canvas.image = self.tk_map  # Keep a reference to avoid garbage collection



# --- Time Utilities ---
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

# --- Main Launch ---
if __name__ == "__main__":
    root = tk.Tk()
    app = CampusNavigator(root)
    root.mainloop()

