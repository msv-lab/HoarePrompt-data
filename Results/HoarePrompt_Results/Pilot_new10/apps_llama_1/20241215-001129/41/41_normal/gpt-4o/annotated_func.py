#State of the program right berfore the function call: There is a list of participants of length n (2 ≤ n ≤ 1000), where each participant has a rating before and after the round, and participants are listed in order from the top to the bottom of the standings.
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
        
    #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 1000 (inclusive), there is a list of participants of length `n`, `ratings` is a list of `n` tuples containing the input integers `a` and `b` for each participant, `is_rated` is `True` if any participant's rating has changed and `False` otherwise, `is_unrated` is `False`.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is an input integer between 2 and 1000 (inclusive), there is a list of participants of length `n`, `ratings` is a list of `n` tuples containing the input integers `a` and `b` for each participant, `is_unrated` is `True` if any `ratings[i-1][0]` is less than `ratings[i][0]` for `i` in range(1, n), `is_rated` is `False`, and the list of participants and `ratings` remain unchanged.
    #State of the program after the if block has been executed: `n` is an input integer between 2 and 1000 (inclusive), there is a list of participants of length `n`, `ratings` is a list of `n` tuples containing the input integers `a` and `b` for each participant, if `is_rated` is `False`, then `is_unrated` is `True` if any `ratings[i-1][0]` is less than `ratings[i][0]` for `i` in range(1, n), and the list of participants and `ratings` remain unchanged; otherwise, the state of `is_unrated` and the lists remains as it was before the if statement, since there is no else part to modify the state when `is_rated` is `True`.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: `n` is an input integer between 2 and 1000 (inclusive), there is a list of participants of length `n`, `ratings` is a list of `n` tuples containing the input integers `a` and `b` for each participant, `is_rated` is `False`. If `is_unrated` is `True` because any `ratings[i-1][0]` is less than `ratings[i][0]` for `i` in range(1, `n`), then 'unrated' has been printed. Otherwise, `is_unrated` is `False`, 'maybe' has been printed to the console, and for all `i` in range(1, `n`), `ratings[i-1][0]` is greater than or equal to `ratings[i][0]`. The list of participants and `ratings` remain unchanged in both cases.
    #State of the program after the if-else block has been executed: *`n` is an input integer between 2 and 1000 (inclusive), there is a list of participants of length `n`, `ratings` is a list of `n` tuples containing the input integers `a` and `b` for each participant. If `is_rated` is `True`, then 'rated' has been printed. If `is_rated` is `False`, then if any `ratings[i-1][0]` is less than `ratings[i][0]` for `i` in range(1, `n`), 'unrated' has been printed; otherwise, 'maybe' has been printed and for all `i` in range(1, `n`), `ratings[i-1][0]` is greater than or equal to `ratings[i][0]`. The list of participants and `ratings` remain unchanged in all cases.
#Overall this is what the function does:The function reads the number of participants and their initial and final ratings, then determines whether the ratings have changed, and prints 'rated' if a change is found, 'unrated' if the initial ratings are not in decreasing order and no changes are found, or 'maybe' if the initial ratings are in decreasing order and no changes are found

