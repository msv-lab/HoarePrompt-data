#State of the program right berfore the function call: The input consists of multiple lines. The first line contains a single integer n (2 ≤ n ≤ 1000) representing the number of round participants. Each of the next n lines contains two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 4126) representing the rating of the i-th participant before and after the round, respectively. The participants are listed in order from the top to the bottom of the standings.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings` is a list of tuples where each tuple contains two integers `(a, b)`, `is_rated` is `True`, `is_unrated` is `False`. For every tuple in `ratings`, `a` and `b` are distinct integers unless the loop did not execute at all, in which case `ratings` remains an empty list and `is_rated` and `is_unrated` remain their original values.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings` is a list of tuples where each tuple contains two distinct integers (a, b), `is_rated` is `False`, `is_unrated` is `True`. If the loop executes, `i` will be `n`, and the condition `ratings[i - 1][0] < ratings[i][0]` will never be met during the loop iterations. If the loop does not execute, `ratings` remains an empty list, `is_rated` is `False`, and `is_unrated` is `True`.
    #State of the program after the if block has been executed: *`n` is an integer between 2 and 1000, `ratings` is a list of tuples where each tuple contains two distinct integers (a, b), `is_rated` is `False`, and `is_unrated` is `True`. If the loop does not execute, `ratings` remains an empty list. If the loop executes, `i` will be `n`, and the condition `ratings[i - 1][0] < ratings[i][0]` will never be met during the loop iterations.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, `ratings` is a list of tuples where each tuple contains two distinct integers (a, b), `is_rated` is `False`. If `is_unrated` is `True`, `is_unrated` remains `True`. Otherwise, `is_unrated` becomes `False` and `ratings` remains an empty list.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, `ratings` is a list of tuples where each tuple contains two distinct integers (a, b). If `is_rated` is `True`, then `is_rated` is `True`, `is_unrated` is `False`, and the value printed is 'rated'. If `is_rated` is `False`, `is_unrated` remains `False`. The state of `ratings` depends on whether the loop executes: if the loop does not execute, `ratings` remains an empty list; if the loop executes, the condition `ratings[i - 1][0] < ratings[i][0]` will never be met, and `ratings` remains an empty list.
#Overall this is what the function does:The function processes input data consisting of `n` participants' ratings before and after a round. It initializes two flags, `is_rated` and `is_unrated`, to track whether any participant's rating changed and whether the ratings are in non-decreasing order. After processing the ratings, it prints one of three possible outcomes: 'rated', 'unrated', or 'maybe'. The function determines the outcome based on the following criteria:
- If any participant's rating changed (`is_rated` is `True`), it prints 'rated'.
- If no participant's rating changed (`is_rated` is `False`) and the ratings are in non-decreasing order (`is_unrated` is `True`), it prints 'unrated'.
- If no participant's rating changed (`is_rated` is `False`) and the ratings are not in non-decreasing order (`is_unrated` is `False`), it prints 'maybe'.

Potential edge cases:
- If the input `n` is less than 2, the function will still process the input as if `n` were 2, but the loop will not execute, keeping `ratings` an empty list and `is_rated` and `is_unrated` in their initial states.
- The function assumes that the ratings are valid integers within the given range, but no validation is performed on the input data.

