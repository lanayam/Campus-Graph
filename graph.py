# Weights in minutes it takes to get to building?
# Redid the buildings with help of ChatGPT since this takes awhile by hand.

import networkx as nx

def campus_graph():
    G = nx.Graph()

    # Define building acronyms and full names
    building_names = {
        "PL": "Pollak Library",
        "MH": "McCarthy Hall",
        "TSU": "Titan Student Union",
        "H": "Humanities",
        "GH": "Gordon Hall",
        "CS": "Computer Science",
        "E": "Engineering",
        "KHS": "Kinesiology & Health Sciences",
        "LH": "Langsdorf Hall",
        "ENPNS": "Eastside North & South Parking Structure",
        "NPS": "Nutwood Parking Structure",
        "SCPS": "State College Parking Structure",
        "B": "Becker Amphitheater",
        "I": "Information Technology Building",
        "EC": "Education Classroom Building",
        "VA": "Visual Arts Building",
        "TG": "Tuffy Lawn",
        "SHCC": "Student Health and Counseling Center",
        "GAS": "Golf Course",
        "GC": "Golf Course",
        "DBH": "Dan Black Hall",
        "F": "Fitness Center"
    }

    # Add edges for Pollak Library to other buildings
    G.add_edge("PL", "MH", weight=3)         # Pollak Library to McCarthy Hall
    G.add_edge("PL", "TSU", weight=2)        # Pollak Library to TSU
    G.add_edge("PL", "H", weight=2)          # Pollak Library to Humanities
    G.add_edge("PL", "GH", weight=3)         # Pollak Library to Gordon Hall
    G.add_edge("PL", "CS", weight=3)         # Pollak Library to Computer Science
    G.add_edge("PL", "E", weight=2)          # Pollak Library to Engineering
    G.add_edge("PL", "KHS", weight=2)        # Pollak Library to Kinesiology & Health Sciences
    G.add_edge("PL", "LH", weight=4)         # Pollak Library to Langsdorf Hall
    G.add_edge("PL", "ENPNS", weight=5)      # Pollak Library to Eastside North & South Parking Structure
    G.add_edge("PL", "NPS", weight=3)        # Pollak Library to Nutwood Parking Structure
    G.add_edge("PL", "SCPS", weight=2)      # Pollak Library to State College Parking Structure

    # Additional connections between adjacent buildings
    G.add_edge("TSU", "MH", weight=2)
    G.add_edge("TSU", "SCPS", weight=3)
    G.add_edge("MH", "GH", weight=1)
    G.add_edge("GH", "H", weight=1)
    G.add_edge("H", "KHS", weight=3)
    G.add_edge("GH", "LH", weight=1)
    G.add_edge("E", "CS", weight=1)
    G.add_edge("CS", "KHS", weight=2)
    G.add_edge("E", "KHS", weight=2)
    G.add_edge("CS", "MH", weight=3)
    G.add_edge("CS", "GH", weight=2)
    G.add_edge("LH", "ENPNS", weight=2)
    G.add_edge("NPS", "ENPNS", weight=2)
    G.add_edge("KHS", "SCPS", weight=3)

    # Add new buildings and their connections
    G.add_edge("PL", "B", weight=2)          # Pollak Library to Becker Amphitheater
    G.add_edge("PL", "I", weight=3)          # Pollak Library to Information Technology Building
    G.add_edge("PL", "EC", weight=2)        # Pollak Library to Education Classroom Building
    G.add_edge("PL", "VA", weight=4)         # Pollak Library to Visual Arts Building
    G.add_edge("PL", "TG", weight=3)         # Pollak Library to Tuffy Lawn
    G.add_edge("PL", "SHCC", weight=3)       # Pollak Library to Student Health and Counseling Center
    G.add_edge("PL", "GAS", weight=5)        # Pollak Library to Golf Course
    G.add_edge("PL", "GC", weight=3)         # Pollak Library to Golf Course
    G.add_edge("PL", "DBH", weight=2)        # Pollak Library to Dan Black Hall
    G.add_edge("PL", "F", weight=4)          # Pollak Library to Fitness Center

    return G, building_names