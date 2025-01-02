#State of the program right berfore the function call: The input consists of an integer n followed by n lines of text. Each line contains a player's name (a string of lowercase Latin letters with a length from 1 to 32) and a score (an integer between -1000 and 1000, inclusive), representing the points gained or lost in each round. The rounds are listed in chronological order. It is guaranteed that at the end of the game, at least one player has a positive number of points, and if multiple players have the maximum number of points, the winner is the one who first reached that score.
def func_1():
    n = int(input())
    rounds = [input().split() for _ in range(n)]
    rounds = [(name, int(score)) for name, score in rounds]
    final_scores = defaultdict(int)
    for (name, score) in rounds:
        final_scores[name] += score
        
    #State of the program after the  for loop has been executed: `n` is the integer input by the user, `rounds` is a list of tuples, `final_scores` is a defaultdict with keys as strings and values representing the total scores accumulated for each player, where each value is the sum of all scores associated with the respective player's name in `rounds`.
    m = max(final_scores.values())
    winner_candidates = {player for player, score in final_scores.items() if 
    score == m}
    curr_scores = defaultdict(int)
    for (name, score) in rounds:
        curr_scores[name] += score
        
        if curr_scores[name] >= m and name in winner_candidates:
            print(name)
            break
        
    #State of the program after the  for loop has been executed: - `rounds` is a list of tuples, and the loop has processed all tuples.
    #- `curr_scores[name]` is the cumulative score for each player `name` as updated by the loop.
    #- If the loop printed any name, it means that player's score has reached or exceeded `m` and the player is in `winner_candidates`.
    #- `final_scores` remains unchanged and still holds the total scores for each player.
    #- `m` remains the maximum value among the values in `final_scores`.
    #- `winner_candidates` contains the names of players whose scores have reached or exceeded `m`.
    #
    #Thus, the output state after all iterations of the loop have finished is:
    #
    #Output State:
#Overall this is what the function does:The function processes an input consisting of an integer `n` followed by `n` lines of text, where each line contains a player's name and a score. It calculates the total scores for each player and identifies the player(s) with the highest score at the end of the game. In case of a tie, it prints the name of the player who first reached the highest score. The function prints the name of the winning player and returns nothing. Potential edge cases include scenarios where the game ends with no player having a positive score, or multiple players having the same highest score simultaneously.

