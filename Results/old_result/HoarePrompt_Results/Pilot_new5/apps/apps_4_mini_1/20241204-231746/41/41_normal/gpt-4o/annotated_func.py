#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and each of the next n lines contains two integers a_i and b_i (1 ≤ a_i, b_i ≤ 4126), representing the rating of the i-th participant before and after the round, respectively.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000, `ratings` contains `n` tuples of the form `(a, b)`, where `a` and `b` are input integers from each iteration, `is_rated` is True if at least one pair of `a` and `b` are not equal, otherwise `is_rated` is False, `is_unrated` remains False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples; `is_rated` is False; `is_unrated` is True if at least one pair of consecutive ratings shows an increase; otherwise, `is_unrated` is False.
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of the form `(a, b)`, where `is_rated` is False. If at least one pair of consecutive ratings shows an increase, then `is_unrated` is True; otherwise, `is_unrated` remains False.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of the form (a, b), where `is_rated` is False. If at least one pair of consecutive ratings shows an increase, then `is_unrated` is True, `is_rated` remains False, and the output is 'unrated'. Otherwise, `is_unrated` is False, `is_rated` is False, and the output is 'maybe'.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000 and `ratings` contains `n` tuples of the form `(a, b)`. If `is_rated` is True, then `is_unrated` remains False and the output is 'rated'. If `is_rated` is False, then if at least one pair of consecutive ratings shows an increase, `is_unrated` becomes True, `is_rated` remains False, and the output is 'unrated'. Otherwise, `is_unrated` is False, `is_rated` is False, and the output is 'maybe'.
#Overall this is what the function does:The function accepts an integer `n` (where 2 ≤ n ≤ 1000) and reads `n` pairs of integers representing the ratings of participants before and after a round. It checks if at least one pair of these ratings is different, indicating that the participant is rated. If any pairs are unequal, it outputs 'rated'. If all pairs are equal, it further checks if there is any increase in consecutive ratings; if such an increase is found, it outputs 'unrated'. If no increases are found, it outputs 'maybe'. Thus, the function assesses the rating status of participants based on the provided ratings.

