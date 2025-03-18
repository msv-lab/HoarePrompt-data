#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000. Each of the next n lines contains two integers a_{i} and b_{i} such that 1 ≤ a_{i}, b_{i} ≤ 4126.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer between 2 and 1000, `ratings_before` is a list of `n` integers, `ratings_after` is a list of `n` integers, where each pair of integers `(a, b)` in `ratings_before` and `ratings_after` corresponds to the inputs received in the loop.
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
        
    #State of the program after the  for loop has been executed: `unrated` is `False`, `i` is the smallest index where the condition `ratings_before[i] < ratings_before[j] and ratings_after[i] > ratings_after[j]` is satisfied for some `j > i`, or `i` is `n - 1` if the condition is never satisfied.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `unrated` is `False`, `rated` is `True` if the loop executes at least once, otherwise `rated` is `False` and `i` is `n-1`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`unrated` is either `True` or `False`, `rated` is `False`, and `i` remains as `n-1`.
    #State of the program after the if-else block has been executed: *`unrated` is a boolean, `rated` is `True` if the loop executes at least once, otherwise `rated` is `False`. If `rated` is `True`, the console prints 'rated'. If `rated` is `False`, `unrated` remains unchanged and `i` remains as `n-1`.
#Overall this is what the function does:The function processes a series of ratings before and after an event. It checks if there is any inconsistency where a participant's rating decreases relative to another participant who had a higher initial rating but ended up with a lower final rating. If such an inconsistency exists, the function prints 'maybe'. If no such inconsistency exists, it further checks if any participant's rating changed. If at least one participant's rating changed, it prints 'rated'. If no participant's rating changed, it prints 'unrated'.

