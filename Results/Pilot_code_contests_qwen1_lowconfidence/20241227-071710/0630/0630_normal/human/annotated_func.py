#State of the program right berfore the function call: The input consists of an integer n followed by n lines, each containing a player's name (a string of lower-case Latin letters with the length from 1 to 32) and a score (an integer between -1000 and 1000, inclusive), representing the points gained or lost in each round. The rounds are listed in chronological order, and it is guaranteed that at the end of the game at least one player has a positive number of points.
def func_1():
    n = int(input())
    rounds = [input().split() for _ in range(n)]
    rounds = [(name, int(score)) for name, score in rounds]
    final_scores = defaultdict(int)
    for (name, score) in rounds:
        final_scores[name] += score
        
    #State of the program after the  for loop has been executed: `rounds` is a list of sublists, where each sublist contains a player's name (string) and their score (integer), `final_scores` is a dictionary where the key is the player's name and the value is the total score accumulated from all sublists in `rounds`.
    m = max(final_scores.values())
    winner_candidates = {player for player, score in final_scores.items() if 
    score == m}
    curr_scores = defaultdict(int)
    for (name, score) in rounds:
        curr_scores[name] += score
        
        if curr_scores[name] >= m and name in winner_candidates:
            print(name)
            break
        
    #State of the program after the  for loop has been executed: `rounds` is a non-empty list where each element is a sublist containing a string and an integer; `curr_scores` is a defaultdict with a default value of 0; if there exists at least one player whose accumulated score in `curr_scores` is greater than or equal to `m` and that player is in `winner_candidates`, the player's name is printed at least once and the loop breaks; otherwise, the loop does not execute and the variables retain their original values.
#Overall this is what the function does:The function accepts input consisting of an integer `n` followed by `n` lines of player names and scores. It processes these inputs to calculate the final scores of each player and determine the player(s) with the highest score at the end of the game. If multiple players have the same highest score, it prints the first one it encounters. If no player has a positive score, it does not print anything. The function does not return any value.

