def cutting_game():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    t = int(data[index])
    index += 1
    results = []

    for _ in range(t):
        a = int(data[index])
        b = int(data[index + 1])
        n = int(data[index + 2])
        m = int(data[index + 3])
        index += 4

        chips = []
        for i in range(n):
            x = int(data[index])
            y = int(data[index + 1])
            chips.append((x, y))
            index += 2

        alice_score = 0
        bob_score = 0

        # Apply the moves
        for _ in range(m):
            c = data[index]
            k = int(data[index + 1])
            index += 2

            if c == 'U':
                chips = chips[k:]
            elif c == 'D':
                chips = chips[:-k]
            elif c == 'L':
                new_chips = [(x, y) for x, y in chips if y >= k]
                chips = new_chips
            elif c == 'R':
                new_chips = [(x, y) for x, y in chips if y < b - k]
                chips = new_chips

        if len(chips) % 2 == 1:
            alice_score += 1
        else:
            bob_score += 1

        results.append(f"{alice_score} {bob_score}")

    print("\n".join(results))

cutting_game()