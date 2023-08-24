t = int(input())

for _ in range(t):
    cards = input()

    num_x = cards.count('X')  # number of 'X' cards

    possible_pairs = []  # list to store all possible pairs (a, b)

    # iterate through all possible values of a and b
    for a in range(1, 13):
        if 12 % a == 0:
            b = 12 // a
            if cards[:b].count('X') == b and cards[-b:].count('X') == b:
                possible_pairs.append((a, b))

    num_possible_pairs = len(set(possible_pairs))

    print(num_possible_pairs, end=' ')
    for pair in possible_pairs:
        print(f"{pair[0]}x{pair[1]}", end=' ')
    print()