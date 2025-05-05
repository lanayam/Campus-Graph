def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)
    positions = []
    i = j = 0

    while i < n:
        if pattern[j].lower() == text[i].lower():
            i += 1
            j += 1
            if j == m:
                positions.append(i - j)
                j = lps[j - 1]
        elif j != 0:
            j = lps[j - 1]
        else:
            i += 1
    return positions

# Mapping building codes to full names
building_map = {
    "PL": "Pollak Library",
    "MH": "McCarthy Hall",
    "TSU": "TSU",
    "H": "Humanities",
    "GH": "Gordon Hall",
    "CS": "Computer Science",
    "E": "Engineering",
    "KHS": "Kinesiology and Health Sciences",
    "LH": "Langsdorf Hall",
    "ENPNS": "Eastside North & South Parking Structure",
    "NPS": "Nutwood Parking Structure",
    "SCPS": "State College Parking Structure"
}

def search_buildings(query):
    matches = []
    for code, name in building_map.items():
        if kmp_search(name, query):
            matches.append((code, name))
    return matches