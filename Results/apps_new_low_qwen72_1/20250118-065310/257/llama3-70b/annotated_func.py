#State of the program right berfore the function call: The input is a list of four lists, each containing two integers a_i and b_i where 1 ≤ a_i, b_i ≤ 100, representing the defence and attack skills of the i-th player, respectively.
def func():
    a1, b1 = map(int, input().split())

a2, b2 = map(int, input().split())

a3, b3 = map(int, input().split())

a4, b4 = map(int, input().split())

team1_defence = max(a1, a2)

team1_attack = max(b1, b2)

team2_defence = max(a3, a4)

team2_attack = max(b3, b4)
    if (team1_defence > team2_attack and team1_attack > team2_defence) :
        print('Team 1')
    else :
        if (team2_defence > team1_attack and team2_attack > team1_defence) :
            print('Team 2')
        else :
            print('Draw')
        #State of the program after the if-else block has been executed: *a1, b1, a2, b2, a3, b3, a4, b4 are integers where 1 ≤ a_i, b_i ≤ 100, team1_defence is max(a1, a2), team1_attack is max(b1, b2), team2_defence is max(a3, a4), team2_attack is max(b3, b4). If team2_defence > team1_attack and team2_attack > team1_defence, 'Team 2' is printed. Otherwise, either team1_defence ≤ team2_attack or team1_attack ≤ team2_defence, and either team2_defence ≤ team1_attack or team2_attack ≤ team1_defence, and 'Draw' is printed.
    #State of the program after the if-else block has been executed: *a1, b1, a2, b2, a3, b3, a4, b4 are integers where 1 ≤ a_i, b_i ≤ 100, team1_defence is max(a1, a2), team1_attack is max(b1, b2), team2_defence is max(a3, a4), team2_attack is max(b3, b4). If team1_defence > team2_attack and team1_attack > team2_defence, 'Team 1' is printed. If team2_defence > team1_attack and team2_attack > team1_defence, 'Team 2' is printed. Otherwise, if either team1_defence ≤ team2_attack or team1_attack ≤ team2_defence, and either team2_defence ≤ team1_attack or team2_attack ≤ team1_defence, 'Draw' is printed.
#Overall this is what the function does:The function reads the defence and attack skills of four players, each represented by two integers between 1 and 100. It then determines the strongest defence and attack skills within two teams of two players each. Based on these values, it prints 'Team 1' if Team 1's strongest defence is greater than Team 2's strongest attack and Team 1's strongest attack is greater than Team 2's strongest defence. It prints 'Team 2' if Team 2's strongest defence is greater than Team 1's strongest attack and Team 2's strongest attack is greater than Team 1's strongest defence. If neither condition is met, it prints 'Draw'. The function does not return any value; it only prints the result to the console.

