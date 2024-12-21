#State of the program right berfore the function call: n is an integer between 2 and 1000, and for each participant, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126, where a_i is the rating before the round and b_i is the rating after the round.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings` contains `n` tuples of integers `(a_i, b_i)` given as input, `is_rated` is True if at least one pair `(a_i, b_i)` exists where `a_i` is not equal to `b_i`, and `is_unrated` remains False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `is_unrated` is True if there exists at least one `i` such that `ratings[i - 1][0] < ratings[i][0]` within the range of the ratings; otherwise, `is_unrated` is False. `n` is an integer between 2 and 1000, and `i` will be `n-1` after the loop completes.
    #State of the program after the if block has been executed: *`n` is an integer between 2 and 1000. If `is_rated` is False, `is_unrated` is set to True if there exists at least one index `i` such that `ratings[i - 1][0] < ratings[i][0]`; otherwise, `is_unrated` is set to False.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000, `is_rated` is False, and `is_unrated` is True. If `is_unrated` is true, the output 'unrated' has been printed. Otherwise, the output 'maybe' has been printed.
    #State of the program after the if-else block has been executed: *`n` is an integer between 2 and 1000. If `is_rated` is True, `is_unrated` remains unchanged, and the output is 'rated'. If `is_rated` is False, then if there exists at least one index `i` such that `ratings[i - 1][0] < ratings[i][0]`, `is_unrated` is set to True and the output is 'unrated'; otherwise, `is_unrated` is set to False and the output is 'maybe'.
#Overall this is what the function does:The function reads an integer `n` representing the number of participants and their ratings before and after a round, stored as tuples in a list. It determines if at least one participant's rating has changed (is rated) or if the ratings are in a potential unrated state. If any participant has a different rating before and after the round, it prints 'rated'. If not, it checks if the ratings are strictly increasing; if they are, it prints 'unrated'. If the ratings are not rated and do not follow a strictly increasing order, it prints 'maybe'. The function effectively analyzes the state of the ratings and outputs one of three possible results: 'rated', 'unrated', or 'maybe'. Additionally, the function does not handle any invalid input scenarios, such as if the input integers exceed the specified ranges or if non-integer values are provided, indicating a potential edge case.

