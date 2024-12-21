#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and each of the next n lines contains two integers a_i and b_i (1 ≤ a_i, b_i ≤ 4126) representing the rating of the i-th participant before and after the round respectively, with participants listed in order from top to bottom of the standings.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings_before` is a list containing `n` integer values of `a`; `ratings_after` is a list containing `n` integer values of `b`; `a` is the last integer input; `b` is the last integer input.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000, `ratings_before` is a list containing `n` integer values, `ratings_after` is a list containing `n` integer values, `a` is the last integer input, `b` is the last integer input, `rated` remains False, and `unrated` is either True or False depending on the comparisons made throughout the iterations.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `rated` is True if there is at least one index `i` where `ratings_before[i]` is not equal to `ratings_after[i]`, otherwise `rated` remains False; `unrated` depends on the values compared, but if all ratings are the same, `unrated` is True.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`rated` is False and `unrated` is True, meaning there are no discrepancies between `ratings_before` and `ratings_after`. If `unrated` is True, the function acknowledges that all ratings are the same. If `unrated` is False, it indicates that 'maybe' has been printed while maintaining that `rated` is still False.
    #State of the program after the if-else block has been executed: *If `rated` is True, the output 'rated' has been printed, and `unrated` can be either True or False depending on the comparison of `ratings_before` and `ratings_after`. If `rated` is False and `unrated` is True, there are no discrepancies between the ratings, meaning all ratings are the same. In this case, if `unrated` is False, 'maybe' has been printed while maintaining that `rated` is still False.
#Overall this is what the function does:The function reads an integer `n`, which represents the number of participants, and then collects each participant's ratings before and after an event through user input. It stores these ratings in two lists: `ratings_before` and `ratings_after`. The function then checks for discrepancies between the before and after ratings. If any participant's after rating does not match their before rating, it outputs 'rated'. If all ratings are the same, it outputs 'unrated'. If there is a condition where one participant's before rating is less than another's but their after rating is greater, it indicates uncertainty in rating and outputs 'maybe'. Therefore, the final output can be 'rated', 'unrated', or 'maybe' based on the comparisons made. The function also does not handle any input errors or invalid cases (e.g., non-integer inputs), which could lead to runtime errors.

