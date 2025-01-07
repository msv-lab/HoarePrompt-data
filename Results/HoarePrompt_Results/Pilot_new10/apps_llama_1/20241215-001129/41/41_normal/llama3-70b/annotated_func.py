#State of the program right berfore the function call: the input is a list of pairs of integers representing the ratings of participants before and after a round, where each pair is (a, b) such that a and b are the ratings of a participant before and after the round, respectively, and the participants are listed in order from the top to the bottom of the standings, and there are at least 2 participants.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ratings_before` is a list of `n` input integers, `ratings_after` is a list of `n` input integers.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ratings_before` and `ratings_after` are lists of `n` input integers, `rated` is `False`, `maybe` is `True`, and `unrated` is `False` if there exists a pair of indices `i` and `j` in `range(n)` such that `ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ratings_before` and `ratings_after` are lists of `n` input integers, `rated` is `True` if there exists an `i` in `range(n)` such that `ratings_before[i]` is not equal to `ratings_after[i]`, otherwise `rated` is `False`, `maybe` is `True`, and `unrated` is `False` if there exists a pair of indices `i` and `j` in `range(n)` such that `ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `ratings_before` and `ratings_after` are lists of `n` input integers, `rated` is `False`, `maybe` is `True`, for all `i` in `range(n)`, `ratings_before[i]` is equal to `ratings_after[i]`. If there does not exist a pair of indices `i` and `j` in `range(n)` such that `ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]`, then `unrated` is `True` and 'unrated' has been printed to the console. Otherwise, `unrated` is `False` and 'maybe' has been printed to the console.
    #State of the program after the if-else block has been executed: `n` is a non-negative integer, `ratings_before` and `ratings_after` are lists of `n` input integers. If there exists an `i` in `range(n)` such that `ratings_before[i]` is not equal to `ratings_after[i]`, then `rated` is `True` and 'rated' has been printed. If for all `i` in `range(n)`, `ratings_before[i]` is equal to `ratings_after[i]`, then `rated` is `False`. In both cases, `maybe` is `True`. If there exists a pair of indices `i` and `j` in `range(n)` such that `ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]`, then `unrated` is `False`. Otherwise, `unrated` is `True` and 'unrated' has been printed if `rated` is `False`, or `unrated` is `True` with no additional output if `rated` is `True`. If `rated` is `False` and `unrated` is `False`, then 'maybe' has been printed.
#Overall this is what the function does:The function accepts a list of pairs of integers representing the ratings of participants before and after a round, checks for rating changes and inconsistent rating updates, and prints 'rated' if any rating changed, 'unrated' if no ratings changed and updates are consistent, and 'maybe' if no ratings changed but updates are inconsistent.

