(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
(a3, b3) = map(int, input().split())
(a4, b4) = map(int, input().split())
team1_defence = max(a1, a2)
team1_attack = max(b1, b2)
team2_defence = max(a3, a4)
team2_attack = max(b3, b4)
if team1_defence > team2_attack and team1_attack > team2_defence:
    print('Team 1')
elif team2_defence > team1_attack and team2_attack > team1_defence:
    print('Team 2')
else:
    print('Draw')