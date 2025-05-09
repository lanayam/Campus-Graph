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
        "B": "Book Store",
        "I": "Parking Lot 1",
        "EC": "Education Classroom Building",
        "VA": "Visual Arts Building",
        "TG": "Titan Gym",
        "SHCC": "Student Health and Counseling Center",
        "GAS": "Gas Station",
        "GC": "Green House Complex",
        "DBH": "Dan Black Hall",
        "F": "Parking Lot 2"
    }

    # Add edges with updated weights
    G.add_edge("PL", "MH", weight=4)         # Pollak Library to McCarthy Hall
    G.add_edge("PL", "TSU", weight=3)        # Pollak Library to TSU
    G.add_edge("PL", "H", weight=3)          # Pollak Library to Humanities
    G.add_edge("PL", "GH", weight=4)         # Pollak Library to Gordon Hall
    G.add_edge("PL", "CS", weight=5)         # Pollak Library to Computer Science
    G.add_edge("PL", "E", weight=4)          # Pollak Library to Engineering
    G.add_edge("PL", "KHS", weight=3)        # Pollak Library to Kinesiology & Health Sciences
    G.add_edge("PL", "LH", weight=5)         # Pollak Library to Langsdorf Hall
    G.add_edge("PL", "ENPNS", weight=6)      # Pollak Library to Eastside North & South Parking Structure
    G.add_edge("PL", "NPS", weight=4)        # Pollak Library to Nutwood Parking Structure
    G.add_edge("PL", "SCPS", weight=3)      # Pollak Library to State College Parking Structure
    G.add_edge("PL", "B", weight=3)          # Pollak Library to Becker Amphitheater
    G.add_edge("PL", "I", weight=4)          # Pollak Library to Parking Lot 1
    G.add_edge("PL", "EC", weight=3)        # Pollak Library to Education Classroom Building
    G.add_edge("PL", "VA", weight=5)         # Pollak Library to Visual Arts Building
    G.add_edge("PL", "TG", weight=4)         # Pollak Library to Titan Gym
    G.add_edge("PL", "SHCC", weight=4)       # Pollak Library to Student Health and Counseling Center
    G.add_edge("PL", "GAS", weight=6)        # Pollak Library to Gas
    G.add_edge("PL", "GC", weight=4)         # Pollak Library to Green House
    G.add_edge("PL", "DBH", weight=3)        # Pollak Library to Dan Black Hall
    G.add_edge("PL", "F", weight=5)          # Pollak Library to Parking Lot 2

    # Additional connections between adjacent buildings
    G.add_edge("TSU", "MH", weight=3)
    G.add_edge("TSU", "SCPS", weight=4)
    G.add_edge("MH", "GH", weight=2)
    G.add_edge("GH", "H", weight=2)
    G.add_edge("H", "KHS", weight=4)
    G.add_edge("GH", "LH", weight=2)
    G.add_edge("E", "CS", weight=2)
    G.add_edge("CS", "KHS", weight=3)
    G.add_edge("E", "KHS", weight=3)
    G.add_edge("CS", "MH", weight=4)
    G.add_edge("CS", "GH", weight=3)
    G.add_edge("LH", "ENPNS", weight=3)
    G.add_edge("NPS", "ENPNS", weight=3)
    G.add_edge("KHS", "SCPS", weight=4)

    G.add_edge("TSU", "H", weight=3)
    G.add_edge("TSU", "GH", weight=2)
    G.add_edge("MH", "H", weight=3)
    G.add_edge("MH", "KHS", weight=4)
    G.add_edge("GH", "KHS", weight=3)
    G.add_edge("GH", "CS", weight=3)
    G.add_edge("H", "CS", weight=4)
    G.add_edge("H", "E", weight=3)
    G.add_edge("KHS", "E", weight=4)
    G.add_edge("KHS", "LH", weight=3)
    G.add_edge("LH", "SCPS", weight=3)
    G.add_edge("ENPNS", "SCPS", weight=4)
    G.add_edge("NPS", "SCPS", weight=3)
    G.add_edge("NPS", "GH", weight=4)
    G.add_edge("SCPS", "GH", weight=3)
    G.add_edge("SCPS", "MH", weight=4)

    return G, building_names