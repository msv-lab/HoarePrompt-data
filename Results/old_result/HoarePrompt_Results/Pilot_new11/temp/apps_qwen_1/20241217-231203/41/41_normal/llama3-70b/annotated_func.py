#State of the program right berfore the function call: The input consists of n (2 ≤ n ≤ 1000) lines, where each line contains two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 4126). The values represent the rating of the i-th participant before and after the round, respectively, and the participants are listed in order from the top to the bottom of the standings.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `ratings_before` is a list of length `n` containing integers, `ratings_after` is a list of length `n+1` containing integers where `ratings_after[i]` (for `0 <= i < n`) is equal to `ratings_before[i]` and `ratings_after[n]` is the last `ratings_after` value entered.
    rated = False
    unrated = True
    maybe = True
    for i in range(n):
        for j in range(i + 1, n):
            if ratings_before[i] < ratings_before[j] and ratings_after[i
                ] > ratings_after[j]:
                unrated = False
                break
        
        if not unrated:
            break
        
    #State of the program after the  for loop has been executed: `unrated` is `False` if there exists at least one pair `(i, j)` such that `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `unrated` is `False` if there exists at least one index `i` such that `ratings_before[i] < ratings_after[i]`, otherwise `unrated` is `True`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`unrated` is a boolean value. If there exists at least one index `i` such that `ratings_before[i] >= ratings_after[i]`, then `unrated` remains `False`. Otherwise, `unrated` remains `True`.
    #State of the program after the if-else block has been executed: *`unrated` is a boolean value. If there exists at least one index `i` such that `ratings_before[i] < ratings_after[i]`, then `unrated` is `False`. Otherwise, `unrated` remains `True`. Additionally, if the condition `(rated)` is true, the string 'rated' is printed.
#Overall this is what the function does:The function reads a series of participants' ratings before and after a round, stored in two lists. It then checks whether there are any participants whose ratings have decreased and prints 'rated' if at least one participant's rating has increased. If no participant's rating has increased, it prints 'unrated' if all ratings are the same or have decreased, and 'maybe' otherwise. The function does not return anything but prints one of the three possible outcomes: 'rated', 'unrated', or 'maybe'. Potential edge cases include scenarios where all ratings remain the same or decrease, or where at least one rating increases. The function also includes nested loops to check for specific conditions related to the ratings before and after the round.

