import networkx as nx

def campus_graph():
    G = nx.Graph()
    # pollak library to other buildings
    G.add_edge("PL", "MH", weight=3)         # Pollak Library to McCarthy Hall
    G.add_edge("PL", "TSU", weight=8)         # Pollak Library to TSU
    G.add_edge("PL", "H", weight=2)         # Pollak Library to Hummanities
    G.add_edge("PL", "GH", weight=9)         # Pollak Library to Gordon Hall
    G.add_edge("PL", "CS", weight=1)          # Pollak Library to Computer Science
    G.add_edge("PL", "E", weight=7)        # Pollak Library to Engineering
    G.add_edge("PL", "KHS", weight=4)      # Pollak Library to Kinesiology & Health Sciences 
    G.add_edge("PL", "LH", weight=6)       # Pollak Library to Langsdorf Hall
    G.add_edge("PL", "ENPNS", weight=5)        # Pollak Library to Eastside North & South Parking Structure
    G.add_edge("PL", "NPS", weight=3)       # Pollak Library to Nutwood Parking Structure
    G.add_edge("PL", "SCPS", weight=2)        #Pollak Library to State College Parking Structure

    # additional connections between adjacent buildings
    G.add_edge("TSU", "MH", weight=2)
    G.add_edge("TSU", "SCPS", weight=9)
    G.add_edge("MH", "GH", weight=1)
    G.add_edge("GH", "H", weight=8)
    G.add_edge("H", "KHS", weight=3)
    G.add_edge("GH", "LH", weight=7)
    G.add_edge("E", "CS", weight=4)
    G.add_edge("CS", "KHS", weight=6)
    G.add_edge("E", "KHS", weight=2)
    G.add_edge("CS", "MH", weight=3)
    G.add_edge("CS", "GH", weight=5)
    G.add_edge("LH", "ENPNS", weight=9)
    G.add_edge("NPS", "ENPNS", weight=2)
    G.add_edge("KHS", "SCPS", weight=3)

    return G

