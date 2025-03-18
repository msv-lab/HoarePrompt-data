#State of the program right berfore the function call: the input consists of a single integer n (2 ≤ n ≤ 1000) followed by n lines, each containing two integers a_i and b_i (1 ≤ a_i, b_i ≤ 4126), representing the rating of the i-th participant before and after the round, respectively, listed in order from the top to the bottom of the standings.
def func():
    n = int(input())
    ratings = []
    is_rated = False
    is_unrated = False
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings.append((a, b))
        
        if a != b:
            is_rated = True
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, inclusive, `ratings` is a list of `n` tuples of integers, `is_rated` is `True` if any input pair `(a, b)` had `a` not equal to `b`, otherwise `False`, and `is_unrated` is `False`.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, inclusive, `ratings` is a list of `n` tuples of integers, `is_rated` is `False`, and `is_unrated` is `True` if there exists at least one pair of consecutive tuples in `ratings` where the first element of the first tuple is less than the first element of the second tuple; otherwise, `is_unrated` is `False`.
    #State of the program after the if block has been executed: *`n` is an integer between 2 and 1000, inclusive, `ratings` is a list of `n` tuples of integers. If `is_rated` is `False`, then `is_unrated` is `True` if there exists at least one pair of consecutive tuples in `ratings` where the first element of the first tuple is less than the first element of the second tuple; otherwise, `is_unrated` is `False`. If `is_rated` is `True`, then the state of `is_unrated` remains unchanged as `False`.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, inclusive, `ratings` is a list of `n` tuples of integers, `is_rated` is `False`. If there exists at least one pair of consecutive tuples in `ratings` where the first element of the first tuple is less than the first element of the second tuple, then `is_unrated` is `True` and 'unrated' has been printed to the console. Otherwise, `is_unrated` is `False` and 'maybe' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, inclusive, `ratings` is a list of `n` tuples of integers. If `is_rated` is `True`, then `is_unrated` is `False` and 'rated' has been printed. If `is_rated` is `False`, then `is_unrated` is `True` and 'unrated' has been printed if there exists at least one pair of consecutive tuples in `ratings` where the first element of the first tuple is less than the first element of the second tuple; otherwise, `is_unrated` is `False` and 'maybe' has been printed.
#Overall this is what the function does:The function processes a series of input lines containing participant ratings before and after a round, and outputs a string indicating whether the ratings have changed, and if not, whether the initial ratings were in a valid order. The function reads an integer `n` representing the number of participants, followed by `n` lines of input, each containing two integers `a_i` and `b_i` representing the rating of the `i-th` participant before and after the round. After reading all input, it checks if any participant's rating has changed (`is_rated` is `True`). If ratings have changed, it outputs 'rated'. If no ratings have changed, it checks if the initial ratings are in a valid order (i.e., if there exists at least one pair of consecutive tuples where the first element of the first tuple is less than the first element of the second tuple). If the initial ratings are not in a valid order, it outputs 'unrated'; otherwise, it outputs 'maybe'. The function does not handle cases where the input is invalid (e.g., non-integer input, out-of-range values), and does not perform any error checking or handling.

