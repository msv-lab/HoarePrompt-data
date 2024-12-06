#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, and for each participant i (where 1 <= i <= n), a_i and b_i are integers such that 1 <= a_i, b_i <= 4126, representing their ratings before and after the round respectively.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 1000; `ratings_before` is a list containing `n` integers from inputs; `ratings_after` is a list containing `n` integers from inputs; `a` is the last input integer for ratings_before; `b` is the last input integer for ratings_after.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 1000; `ratings_before` is a list containing `n` integers; `ratings_after` is a list containing `n` integers; `a` is the last integer for `ratings_before`; `b` is the last integer for `ratings_after`; `rated` is False; `unrated` is False; `maybe` is True. The loop will check the conditions for all pairs of ratings, and if any pair meets the condition leading to a change in `unrated`, the state of `unrated` will be False. If no such pair is found, `unrated` will remain True.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 1000, `ratings_before` and `ratings_after` are lists containing `n` integers. `rated` is True if there is at least one pair of different ratings between `ratings_before` and `ratings_after`; otherwise, `rated` is False. `unrated` remains True if all pairs of ratings are equal, otherwise, it is False. `maybe` is True.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= `n` <= 1000, `ratings_before` and `ratings_after` are lists containing `n` integers, `rated` is False, and `maybe` is True. If `unrated` is True, 'unrated' is printed. Otherwise, `unrated` is False and 'maybe' is printed.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= `n` <= 1000, `ratings_before` and `ratings_after` are lists containing `n` integers. If `rated` is True, the output includes 'rated'. If `rated` is False, `maybe` is True. If `unrated` is True, the output includes 'unrated'; otherwise, 'maybe' is printed while `unrated` is False.
#Overall this is what the function does:The function accepts no parameters and processes the ratings of `n` participants (where `n` is an integer between 2 and 1000). It reads ratings before and after a round for each participant. The function determines whether the ratings are 'rated' (if any participant's rating has changed), 'unrated' (if the ratings before and after are the same for all participants), or 'maybe' (if there is an inconsistency in the ratings where some participants have increased ratings before and decreased afterwards). It outputs one of the three results based on these checks.

