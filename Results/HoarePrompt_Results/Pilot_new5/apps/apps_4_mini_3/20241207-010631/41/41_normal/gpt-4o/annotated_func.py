#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and for each participant, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126, where a_i is the rating before the round and b_i is the rating after the round.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of input integers (a, b); `is_rated` is True if at least one tuple (a, b) has a ≠ b, otherwise it is False; `is_unrated` is False; all values of `a` and `b` are the integers input during the iterations.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `is_unrated` is True if there exists at least one pair of consecutive ratings where the first element of the tuple increases; otherwise, `is_unrated` is False. `ratings` contains `n` tuples of input integers (a, b), and `n` is an integer such that 2 ≤ `n` ≤ 1000.
    #State of the program after the if block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of input integers (a, b); `is_rated` is False, then `is_unrated` is True if there exists at least one pair of consecutive ratings where the first element of the tuple increases; otherwise, `is_unrated` is False.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of input integers (a, b); `is_rated` is False; if there exists at least one pair of consecutive ratings where the first element of the tuple increases (`is_unrated` is True), the output is 'unrated'; otherwise, the output is 'maybe'.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings` contains `n` tuples of input integers (a, b); if `is_rated` is True, then `is_unrated` is False and 'rated' has been printed. If `is_rated` is False, and there exists at least one pair of consecutive ratings where the first element of the tuple increases, then `is_unrated` is True and the output is 'unrated'; otherwise, the output is 'maybe'.
#Overall this is what the function does:The function accepts an integer `n` representing the number of participants, and for each participant, it processes their ratings before (`a_i`) and after (`b_i`) a round. The function checks if any participant's rating has changed (`is_rated`). If at least one rating has changed, it outputs 'rated'. If no ratings have changed and at least one rating before the round is less than a subsequent rating, it outputs 'unrated'. If there are no changes and ratings are non-increasing, it outputs 'maybe'. The function handles cases where `n` can range from 2 to 1000 and ratings are integers between 1 and 4126.

