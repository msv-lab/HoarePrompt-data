n = int(input())
s = input()
platforms = [i for i, c in enumerate(s) if c == '*']

good = False
for i in range(len(platforms) - 4):
    delta = platforms[i + 1] - platforms[i]
    if all(platforms[i + j] - platforms[i + j - 1] == delta for j in range(2, 5)):
        good = True
        break

print("yes" if good else "no")
