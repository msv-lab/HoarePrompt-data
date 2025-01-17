def vind_speler(n, m, x, throws):
    mogelijke_posities = set([x])
    for r, c in throws:
        new_positie = set()
        for pos in mogelijke_posities:
            if c == '0' or c == '?':
                new_positie .add((pos + r - 1) % n + 1)
            if c == '1' or c == '?':
                new_positie .add((pos - r - 1) % n + 1)
        mogelijke_posities = new_positie 
    return sorted(mogelijke_posities)

# Lees het aantal testgevallen
t = int(input())
resultaat = []

# Verwerk elk testgeval
for _ in range(t):
    n, m, x = map(int, input().split())
    throws = [input().split() for _ in range(m)]
    throws = [(int(r), c) for r, c in throws]
    mogelijke_spelers = vind_speler(n, m, x, throws)
    resultaat.append((len(mogelijke_spelers), mogelijke_spelers))

# Print de resultaten
for k, spelers in resultaat:
    print(k)
    print(' '.join(map(str, spelers)))