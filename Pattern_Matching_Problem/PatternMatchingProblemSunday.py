def naive_algorithm(pattern, text):
    text_length = len(text)
    pattern_length = len(pattern)
    occurrences = []

    for i in range(0, text_length - pattern_length + 1):
        j = 0
        while j < pattern_length:
            if text[i + j] != pattern[j]:
                break
            j += 1
            if j == pattern_length:
                occurrences.append(i)
    return occurrences


def sunday_algorithm(pattern, text):
    text_length = len(text)
    pattern_length = len(pattern)
    occurrences = []

    shifts = {}
    for i in range(pattern_length):
        shifts[pattern[i]] = pattern_length - i
        print(shifts)

    i = 0
    while i <= text_length - pattern_length:
        j = 0
        while j < pattern_length:
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == pattern_length:
            occurrences.append(i)

        if i + pattern_length < text_length:
            i += shifts.get(text[i + pattern_length], pattern_length + 1)
        else:
            break
    return occurrences


def sunday_algorithm_pairs(pattern, text):
    text_length = len(text)
    pattern_length = len(pattern)
    occurrences = []
    shifts = {}

    for i in range(pattern_length - 1):
        pair = pattern[i:i + 2]
        shifts[pair] = pattern_length - i - 1

    print("Pattern:", pattern)
    print("Shift table for letter pairs:")
    for pair, shift in shifts.items():
        print(f"  {pair} -> {shift}")

    i = 0
    while i <= text_length - pattern_length:
        j = 0
        while j < pattern_length:
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == pattern_length:
            occurrences.append(i)

        if i + pattern_length + 1 <= text_length:
            text_pair = text[i + pattern_length - 1 : i + pattern_length + 1]
            i += shifts.get(text_pair, pattern_length)
        else:
            break
    return occurrences


def knuth_morris_pratt(pattern, text):
    pattern_length = len(pattern)
    prefix_suffix_table = [0] * pattern_length
    j = 0

    for i in range(1, pattern_length):
        while j > 0 and pattern[i] != pattern[j]:
            j = prefix_suffix_table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        prefix_suffix_table[i] = j

    print("Prefix-suffix table:", prefix_suffix_table)

    matches = []
    j = 0

    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = prefix_suffix_table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == pattern_length:
            matches.append(i - pattern_length + 1)
            j = prefix_suffix_table[j - 1]

    return matches


text = "BACABADEABADDEAABCCABAD"
pattern = "ABAD"

print("\nText to search: " + text)
print("Pattern: " + pattern)
print("---------------------------------------\n")
print("[Naive Algorithm]:")
print(naive_algorithm(pattern, text))
print("\n---------------------------------------\n")
print("[Sunday Algorithm]:")
print(sunday_algorithm(pattern, text))
print("\n---------------------------------------\n")
print("[Sunday Algorithm (Letter Pairs)]:")
print(sunday_algorithm_pairs(pattern, text))
print("\n---------------------------------------\n")
print("[Knuth-Morris-Pratt Algorithm]:")
print(knuth_morris_pratt(pattern, text))
