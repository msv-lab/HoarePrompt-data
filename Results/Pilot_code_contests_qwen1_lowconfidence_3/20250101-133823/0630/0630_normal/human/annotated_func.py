#State of the program right berfore the function call: The input consists of an integer n indicating the number of rounds played, followed by n lines of text, each containing a player's name (a string of lowercase Latin letters with a length from 1 to 32) and a score (an integer between -1000 and 1000). The number of rounds played is between 1 and 1000, inclusive. At the end of the game, at least one player has a positive number of points, and there is a unique player or a tie for the highest score where one of the tied players had the highest score first.
def func_1():
    n = int(input())
    rounds = [input().split() for _ in range(n)]
    rounds = [(name, int(score)) for name, score in rounds]
    final_scores = defaultdict(int)
    for (name, score) in rounds:
        final_scores[name] += score
        
    #State of the program after the  for loop has been executed: `n` is 3, `rounds` is `[('Alice', 10), ('Bob', 20), ('Charlie', 30)]`, `final_scores` is a defaultdict with default factory int and value `{'Alice': 10, 'Bob': 40, 'Charlie': 60}`, `name` is the last name processed in the loop, `score` is the score associated with that name in the last round processed.
    m = max(final_scores.values())
    winner_candidates = {player for player, score in final_scores.items() if 
    score == m}
    curr_scores = defaultdict(int)
    for (name, score) in rounds:
        curr_scores[name] += score
        
        if curr_scores[name] >= m and name in winner_candidates:
            print(name)
            break
        
    #State of the program after the  for loop has been executed: `rounds` is `[('Alice', 10), ('Bob', 20), ('Charlie', 30)]`, `curr_scores` is a dictionary where each name's score is the sum of their respective scores from `rounds`, `name` is the last name processed, `score` is the last score processed, `m` is 60, `winner_candidates` is `{'Charlie'}`, and if `curr_scores['Charlie']` is greater than or equal to 60, the name `Charlie` will be printed, otherwise, the loop will finish without printing anything.
#Overall this is what the function does:The function accepts an integer `n` indicating the number of rounds played, followed by `n` lines of text. Each line contains a player's name (a string of lowercase Latin letters with a length from 1 to 32) and a score (an integer between -1000 and 1000). It calculates the final scores of each player across all rounds, identifies the player(s) with the highest score, and prints the name of the first player to reach or exceed the highest score. If there is a tie for the highest score, it ensures that the player who initially achieved the highest score first is identified. If no player meets the condition of having a score that reaches or exceeds the highest score, the function will not print anything.

