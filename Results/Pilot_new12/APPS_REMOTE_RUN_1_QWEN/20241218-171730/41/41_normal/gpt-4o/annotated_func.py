#State of the program right berfore the function call: The input consists of n lines where n is an integer such that 2 ≤ n ≤ 1000. Each line contains two space-separated integers a_{i} and b_{i} such that 1 ≤ a_{i}, b_{i} ≤ 4126. The lines are ordered such that the first line represents the top participant and the last line represents the bottom participant of the standings.
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
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `ratings` is a list of tuples where each tuple contains two integers `(a_i, b_i)` with `1 ≤ a_i, b_i ≤ 4126`, `is_rated` is True, `is_unrated` is False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is a non-negative integer greater than 1, `ratings` is a list of tuples where each tuple contains two integers `(a_i, b_i)` with `1 ≤ a_i, b_i ≤ 4126`, `is_rated` remains `False`, `is_unrated` remains `True`. If for any `i` (1 ≤ i < n), `ratings[i-1][0] < ratings[i][0]` holds true, `is_unrated` becomes `False`. Otherwise, `is_unrated` remains `True`.
    #State of the program after the if block has been executed: `n` is a non-negative integer. If for any `i` (1 ≤ i < n), `ratings[i-1][0] < ratings[i][0]` holds true, `is_unrated` becomes `False`. Otherwise, `is_unrated` remains `True`. `is_rated` remains `False`.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer, `is_rated` remains `False`, `is_unrated` remains `True`, and for any `i` (1 ≤ i < n), `ratings[i-1][0] < ratings[i][0]` does not hold true.
    #State of the program after the if-else block has been executed: *`n` is a non-negative integer. `is_rated` remains `False`. If for any `i` (1 ≤ i < n), `ratings[i-1][0] < ratings[i][0]` holds true, `is_unrated` becomes `False`. Otherwise, `is_unrated` remains `True`.
#Overall this is what the function does:The function processes input consisting of \(n\) lines, each containing two space-separated integers \(a_i\) and \(b_i\). It determines whether the participants' ratings are consistent (i.e., no participant has a strictly lower rating than the next one), fully rated (at least one participant has a strictly higher rating than the previous one), or mixed (neither condition is met). Specifically, it:

1. Reads \(n\) and initializes lists to store ratings and boolean flags.
2. Collects \(n\) pairs of ratings into a list.
3. Sets a flag `is_rated` to True if any participant has a different rating than the previous one.
4. If no participant has a different rating (`is_rated` remains False), it checks if the ratings are strictly increasing. If so, it sets `is_unrated` to False; otherwise, it keeps `is_unrated` as True.
5. Prints "rated" if `is_rated` is True, indicating the ratings are fully rated.
6. Prints "unrated" if `is_unrated` is True, indicating the ratings are not strictly increasing.
7. Prints "maybe" if neither of the above conditions is met, indicating the ratings are mixed.

Potential edge cases:
- If \(n = 1\), the function will always print "maybe" because there are no subsequent ratings to compare.
- If all participants have the same rating, the function will print "unrated" since no participant has a strictly higher rating than the previous one.

