#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and for each participant, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126, representing the ratings before and after the round respectively.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ n ≤ 1000; `ratings` contains n tuples of the form (a, b); `is_rated` is True if at least one pair (a, b) has a ≠ b, otherwise it is False; `is_unrated` is False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `is_unrated` is True if there exists at least one index `i` such that `ratings[i - 1][0] < ratings[i][0]`, else `is_unrated` is False, `is_rated` remains False, and `n` is an integer such that 2 ≤ n ≤ 1000.
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000, `ratings` contains `n` tuples of the form (a, b), `is_unrated` is True if there exists at least one index `i` such that `ratings[i - 1][0] < ratings[i][0]`, otherwise `is_unrated` is False, and `is_rated` remains False.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000 and `ratings` contains `n` tuples of the form (a, b). If `is_unrated` is True, then 'unrated' has been printed and `is_rated` is False. Otherwise, if `is_unrated` is False, then 'maybe' has been printed and `is_rated` remains False.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of the form (a, b). If `is_rated` is True, then a message 'rated' is printed and `is_rated` is set to True. If `is_rated` is False and `is_unrated` is True, then 'unrated' is printed and `is_rated` remains False. Otherwise, if both `is_rated` and `is_unrated` are False, then 'maybe' is printed and `is_rated` remains False.
#Overall this is what the function does:The function processes ratings for `n` participants, where each participant has a rating before and after a round. It determines if the ratings are "rated" (if any participant's before and after ratings differ), "unrated" (if the before ratings are not strictly increasing when all after ratings are equal), or "maybe" (if the ratings are all equal and not strictly increasing). The function does not return any values directly, as it takes no parameters.

