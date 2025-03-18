n = int(input())
a = list(map(int, input().split()))
alice_turn = True
while True:
    max_stones = max(a)
    if max_stones == 0:
        break
    piles_to_remove = n // 2
    piles_removed = 0
    for i in range(n):
        if a[i] > 0 and piles_removed < piles_to_remove:
            a[i] -= 1
            piles_removed += 1
    alice_turn = not alice_turn
if alice_turn:
    print("Bob")
else:
    print("Alice")
