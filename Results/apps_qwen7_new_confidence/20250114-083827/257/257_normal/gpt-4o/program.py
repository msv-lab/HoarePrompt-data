# Read input
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())
a4, b4 = map(int, input().split())

# Function to determine if team1 can beat team2
def can_team1_win(a1, b1, a2, b2, a3, b3, a4, b4):
    # Team 1 combinations
    team1_defence_1 = a1
    team1_attack_1 = b2
    team1_defence_2 = a2
    team1_attack_2 = b1
    
    # Team 2 combinations (based on team 1's choice)
    team2_defence_1 = a3
    team2_attack_1 = b4
    team2_defence_2 = a4
    team2_attack_2 = b3

    # Check all combinations and if there is a guaranteed win for team 1
    if (team1_defence_1 > team2_attack_1 and team1_attack_1 > team2_defence_1) or (team1_defence_1 > team2_attack_2 and team1_attack_1 > team2_defence_2):
        return True
    
    if (team1_defence_2 > team2_attack_1 and team1_attack_2 > team2_defence_1) or (team1_defence_2 > team2_attack_2 and team1_attack_2 > team2_defence_2):
        return True
    
    return False

# Function to determine if team2 can beat team1
def can_team2_win(a1, b1, a2, b2, a3, b3, a4, b4):
    # Team 1 combinations
    team1_defence_1 = a1
    team1_attack_1 = b2
    team1_defence_2 = a2
    team1_attack_2 = b1
    
    # Team 2 combinations (based on team 1's choice)
    team2_defence_1 = a3
    team2_attack_1 = b4
    team2_defence_2 = a4
    team2_attack_2 = b3

    # Check all combinations and if there is a guaranteed win for team 2
    if (team2_defence_1 > team1_attack_1 and team2_attack_1 > team1_defence_1) or (team2_defence_1 > team1_attack_2 and team2_attack_1 > team1_defence_2):
        return True
    
    if (team2_defence_2 > team1_attack_1 and team2_attack_2 > team1_defence_1) or (team2_defence_2 > team1_attack_2 and team2_attack_2 > team1_defence_2):
        return True
    
    return False

# Determine the result
team1_wins = can_team1_win(a1, b1, a2, b2, a3, b3, a4, b4)
team2_wins = can_team2_win(a1, b1, a2, b2, a3, b3, a4, b4)

if team1_wins and not team2_wins:
    print("Team 1")
elif team2_wins and not team1_wins:
    print("Team 2")
else:
    print("Draw")
