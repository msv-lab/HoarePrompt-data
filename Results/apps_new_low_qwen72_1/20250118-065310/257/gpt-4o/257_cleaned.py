(a1, b1) = map(int, input().split())
(a2, b2) = map(int, input().split())
(a3, b3) = map(int, input().split())
(a4, b4) = map(int, input().split())

def func_1(a1, b1, a2, b2, a3, b3, a4, b4):
    team1_defence_1 = a1
    team1_attack_1 = b2
    team1_defence_2 = a2
    team1_attack_2 = b1
    team2_defence_1 = a3
    team2_attack_1 = b4
    team2_defence_2 = a4
    team2_attack_2 = b3
    if team1_defence_1 > team2_attack_1 and team1_attack_1 > team2_defence_1 or (team1_defence_1 > team2_attack_2 and team1_attack_1 > team2_defence_2):
        return True
    if team1_defence_2 > team2_attack_1 and team1_attack_2 > team2_defence_1 or (team1_defence_2 > team2_attack_2 and team1_attack_2 > team2_defence_2):
        return True
    return False

def func_2(a1, b1, a2, b2, a3, b3, a4, b4):
    team1_defence_1 = a1
    team1_attack_1 = b2
    team1_defence_2 = a2
    team1_attack_2 = b1
    team2_defence_1 = a3
    team2_attack_1 = b4
    team2_defence_2 = a4
    team2_attack_2 = b3
    if team2_defence_1 > team1_attack_1 and team2_attack_1 > team1_defence_1 or (team2_defence_1 > team1_attack_2 and team2_attack_1 > team1_defence_2):
        return True
    if team2_defence_2 > team1_attack_1 and team2_attack_2 > team1_defence_1 or (team2_defence_2 > team1_attack_2 and team2_attack_2 > team1_defence_2):
        return True
    return False
team1_wins = func_1(a1, b1, a2, b2, a3, b3, a4, b4)
team2_wins = func_2(a1, b1, a2, b2, a3, b3, a4, b4)
if team1_wins and (not team2_wins):
    print('Team 1')
elif team2_wins and (not team1_wins):
    print('Team 2')
else:
    print('Draw')