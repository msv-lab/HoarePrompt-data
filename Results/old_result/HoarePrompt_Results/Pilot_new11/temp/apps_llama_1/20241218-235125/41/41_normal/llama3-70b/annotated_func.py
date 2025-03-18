#State of the program right berfore the function call: The function takes no arguments, but the input to the program is a list of pairs of integers representing the rating of each participant before and after the round, with the participants listed in order from the top to the bottom of the standings, and the number of participants is a known integer between 2 and 1000.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings_before` is a list of `n` input integers, `ratings_after` is a list of `n` input integers
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings_before` and `ratings_after` are lists of `n` input integers, `rated` is `False`, `maybe` is `True`, and `unrated` is `False` if there exists a pair of elements in `ratings_before` and `ratings_after` where `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings_before` and `ratings_after` are lists of `n` input integers, `maybe` is `True`, `unrated` is `False` if there exists a pair of elements in `ratings_before` and `ratings_after` where `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`, and `rated` is `True` if any element in `ratings_before` is not equal to the corresponding element in `ratings_after`, otherwise `rated` is `False`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: `n` is an integer between 2 and 1000, `ratings_before` and `ratings_after` are lists of `n` input integers, `maybe` is `True`, if for all pairs of elements in `ratings_before` and `ratings_after`, `ratings_before[i] < ratings_before[j]` implies `ratings_after[i] <= ratings_after[j]`, then `unrated` is `True`, 'unrated' has been printed, and `rated` is `False`; otherwise, `unrated` is `False`, `rated` is `False`, and 'maybe' has been printed, indicating the existence of at least one pair of elements in `ratings_before` and `ratings_after` where `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, `ratings_before` and `ratings_after` are lists of `n` input integers, `maybe` is `True`. If `rated` is `True`, then 'rated' has been printed to the console and `unrated` is `False` if there exists a pair of elements in `ratings_before` and `ratings_after` where `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`, otherwise `unrated` is `True`. If `rated` is `False`, then either 'unrated' has been printed and `unrated` is `True` if for all pairs of elements in `ratings_before` and `ratings_after`, `ratings_before[i] < ratings_before[j]` implies `ratings_after[i] <= ratings_after[j]`, or 'maybe' has been printed and `unrated` is `False`, indicating the existence of at least one pair of elements in `ratings_before` and `ratings_after` where `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`.
#Overall this is what the function does:The function takes no arguments but reads a list of pairs of integers representing the rating of each participant before and after a round from the input, and then classifies the round as 'rated', 'unrated', or 'maybe' based on the ratings. It first determines if any participant's rating has changed by checking if any pair of elements in the 'ratings_before' and 'ratings_after' lists are not equal. If a change is found, it prints 'rated'. If no changes are found, it checks if the ratings before and after the round are in a consistent order (i.e., a participant with a lower initial rating does not end up with a higher final rating than a participant with a higher initial rating). If the order is consistent, it prints 'unrated'; otherwise, it prints 'maybe'. The function does not handle cases where the input is invalid (e.g., non-integer values, incorrect number of participants), and it assumes that the input is well-formed and that the number of participants is between 2 and 1000. After execution, the function will have printed one of 'rated', 'unrated', or 'maybe' to the console, indicating the classification of the round based on the input ratings.

