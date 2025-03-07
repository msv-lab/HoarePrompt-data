"""
https://codeforces.com/problemset/problem/1970/F1
F1. Playing Quidditch (Easy)
"""
 
n, m = [int(x) for x in input().split()]
players = dict()
goals = {"B": [], "R": []}
mouvements = {"L": (-1, 0), "R": (1, 0), "U": (0, -1), "D": (0, 1)}
pointsb, pointsr = 0, 0
 
for y in range(n):
    s = input().split()
    for x in range(m):
        if s[x] == ".." or s[x] == ".Q":
            continue
        elif s[x] == "RG":
            goals["R"].append((x, y))
        elif s[x] == "BG":
            goals["B"].append((x, y))
        else:
            players[s[x]] = (x, y)
 
 
def add(a, b):
    x, y = a
    dx, dy = b
    return x + dx, y + dy
 
 
moves = int(input())
for i in range(moves):
    mo = input().split()
    if mo[1] in "ULDR":
        players[mo[0]] = add(players[mo[0]], mouvements[mo[1]])
    elif mo[1] == "T":
        if players[mo[0]] in goals["R"]:
            pointsb += 1
            print(i, "BLUE GOAL")
        if players[mo[0]] in goals["B"]:
            pointsr += 1
            print(i, "RED GOAL")
 
 
print("FINAL SCORE:", pointsr, pointsb)