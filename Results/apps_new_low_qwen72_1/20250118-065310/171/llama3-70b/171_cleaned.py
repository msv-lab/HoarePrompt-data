n = int(input())
k1 = int(input())
deck1 = list(map(int, input().split()))
k2 = int(input())
deck2 = list(map(int, input().split()))

def func_1(deck1, deck2):
    seen = set()
    while deck1 and deck2:
        state = (tuple(deck1), tuple(deck2))
        if state in seen:
            return -1
        seen.add(state)
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)
        if card1 > card2:
            deck1.extend([card1, card2])
        else:
            deck2.extend([card2, card1])
    return (len(seen), 1) if deck1 else (len(seen), 2)
print(*func_1(deck1, deck2))