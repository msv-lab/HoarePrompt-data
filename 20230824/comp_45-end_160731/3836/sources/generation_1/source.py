n = int(input())

spectators = []
for _ in range(n):
    s, a = input().split()
    a = int(a)
    spectators.append((s, a))

alice_supporters = []
bob_supporters = []
neutral_supporters = []
both_supporters = []

for s, a in spectators:
    if s == "10":
        alice_supporters.append(a)
    elif s == "01":
        bob_supporters.append(a)
    elif s == "00":
        neutral_supporters.append(a)
    elif s == "11":
        both_supporters.append(a)

alice_supporters.sort(reverse=True)
bob_supporters.sort(reverse=True)
neutral_supporters.sort(reverse=True)
both_supporters.sort(reverse=True)

total_influence = 0
alice_count = 0
bob_count = 0

for i in range(min(len(alice_supporters), len(bob_supporters))):
    total_influence += alice_supporters[i]
    total_influence += bob_supporters[i]
    alice_count += 1
    bob_count += 1

remaining_alice = len(alice_supporters) - alice_count
remaining_bob = len(bob_supporters) - bob_count

for i in range(min(len(neutral_supporters), remaining_alice)):
    total_influence += neutral_supporters[i]
    alice_count += 1

for i in range(min(len(neutral_supporters), remaining_bob)):
    total_influence += neutral_supporters[i]
    bob_count += 1

for i in range(min(len(both_supporters), remaining_alice, remaining_bob)):
    total_influence += both_supporters[i]
    alice_count += 1
    bob_count += 1

if alice_count >= n/2 and bob_count >= n/2:
    print(total_influence)
else:
    print(0)