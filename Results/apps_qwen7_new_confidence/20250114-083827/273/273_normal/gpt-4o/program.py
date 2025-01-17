def find_swaps(s, t):
    if len(s) != len(t):
        return -1

    pairs = {}
    used = set()
    swaps = []

    for i in range(len(s)):
        if s[i] == t[i]:
            continue
        if s[i] in used or t[i] in used:
            return -1
        if s[i] in pairs and pairs[s[i]] != t[i]:
            return -1
        if t[i] in pairs and pairs[t[i]] != s[i]:
            return -1
        pairs[s[i]] = t[i]
        pairs[t[i]] = s[i]
        used.add(s[i])
        used.add(t[i])

    for key, value in pairs.items():
        if key < value:
            swaps.append((key, value))

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Read input
s = input()
t = input()

# Call the function
find_swaps(s, t)
