#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, and for each participant i (0 <= i < n), a[i] and b[i] are integers such that 1 <= a[i], b[i] <= 4126, where a[i] is the rating before the round and b[i] is the rating after the round.
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
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 1000, `ratings` contains `n` tuples of integers (a[i], b[i]) where 1 <= a[i], b[i] <= 4126 for each participant `i`, `is_rated` is True if any a[i] is not equal to b[i], otherwise `is_rated` is False, `is_unrated` is False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `is_rated` is False, `is_unrated` is True if there exists at least one pair of consecutive ratings where the first element of the tuple at index `i - 1` is less than the first element of the tuple at index `i`, otherwise `is_unrated` is False. `n` is between 2 and 1000, `ratings` contains `n` tuples of integers.
    #State of the program after the if block has been executed: *`n` is between 2 and 1000, `ratings` contains `n` tuples of integers. If `is_rated` is False, then `is_unrated` is set to True if there exists at least one pair of consecutive ratings where the first element of the tuple at index `i - 1` is less than the first element of the tuple at index `i`; otherwise, `is_unrated` is False. If `is_rated` is True, the state of the variables remains unchanged.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is between 2 and 1000, `ratings` contains `n` tuples of integers, and `is_rated` is False. If `is_unrated` is True, this indicates that there exists at least one pair of consecutive ratings where the first element of the tuple at index `i - 1` is less than the first element of the tuple at index `i`, and the output is 'unrated'. Otherwise, if `is_unrated` is False, there are no such pairs of consecutive ratings.
    #State of the program after the if-else block has been executed: *`n` is between 2 and 1000, `ratings` contains `n` tuples of integers. If `is_rated` is True, the output is 'rated' and the state of the variables remains unchanged. If `is_rated` is False, and `is_unrated` is True, this indicates that there exists at least one pair of consecutive ratings where the first element of the tuple at index `i - 1` is less than the first element of the tuple at index `i`, and the output is 'unrated'. If `is_unrated` is False, there are no such pairs of consecutive ratings.
#Overall this is what the function does:The function accepts an integer `n` representing the number of participants' ratings, followed by `n` pairs of integers where each pair consists of a rating before and after a round. It determines if any participant's rating changed after the round (`is_rated`), and if all ratings remained the same, it checks for at least one case where the ratings before the round are in an increasing order (to set `is_unrated`). The function outputs one of three strings: 'rated' if any participant's rating has changed, 'unrated' if the ratings haven't changed but there is an increasing case, and 'maybe' if the ratings remained the same and there is no increasing case. Overall, the function processes the ratings and provides an appropriate response based on the results.

