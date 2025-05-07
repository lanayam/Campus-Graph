# Dev: Alex I
#
# KMP
# To search for building names or rooms numbers
# 

def kmp_search(text, pattern):
    # Compute LPS (Longest Prefix Suffix) array
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0  # length of the previous longest prefix suffix, i.e., lps[i-1]
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length > 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    lps = compute_lps(pattern)
    result = []
    i = j = 0  # i for text, j for pattern, both are indices

    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1

        if j == len(pattern):
            result.append(i - j)  # Match found
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return result

# --- Test Case ---
if __name__ == "__main__":
    campus_text = "Pollak Library, McCarthy Hall, TSU, Humanities, Gordon Hall, Computer Science"
    query = "Science"
    positions = kmp_search(campus_text, query)
    print(f"'{query}' found at positions: {positions}")
