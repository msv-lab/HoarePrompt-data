N = int(input())
sizes = list(map(int, input().split()))

sizes.sort(reverse=True)

alice, bob = 0, 0
decider = True

for size in sizes:
    if decider:
        alice += size
    else:
        bob += size
    decider = not decider

print(alice, bob)
