#State of the program right berfore the function call: The input consists of a list of participant ratings before and after the round, where each participant's rating is a positive integer, and the number of participants is between 2 and 1000. The participants are listed in order from the top to the bottom of the standings.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: The number of participants is between 2 and 1000, each participant's rating is a positive integer, `n` is a non-negative integer, `ratings_before` is a list containing `n` input integers `a`, `ratings_after` is a list containing `n` input integers `b`.
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
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 1000, `rated` is False, `maybe` is True, `ratings_before` and `ratings_after` are lists containing `n` input integers, `unrated` is True if no participant has a lower rating before but a higher rating after, otherwise `unrated` is False, `i` is `n-1` if `unrated` is True, otherwise `i` is the index where the inconsistency was found.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is between 2 and 1000, `ratings_before` and `ratings_after` are lists containing `n` input integers, `maybe` is True, `unrated` is True if no participant has a lower rating before but a higher rating after otherwise `unrated` is False, `rated` is True if any `ratings_before[i]` is not equal to `ratings_after[i]`, otherwise `rated` is False, `i` is the index of the first inconsistent rating if found, otherwise `i` is `n-1`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is between 2 and 1000, `ratings_before` and `ratings_after` are lists containing `n` input integers, `maybe` is True, `rated` is False, `i` is `n-1`, and for all indices `j` in range `n`, `ratings_before[j]` is equal to `ratings_after[j]`. If `unrated` is True, 'unrated' has been printed to the console. If `unrated` is False, there exists at least one participant who has a lower rating before but a higher rating after, and 'maybe' has been printed to the console.
    #State of the program after the if-else block has been executed: `n` is between 2 and 1000, `ratings_before` and `ratings_after` are lists containing `n` input integers, `maybe` is True. If `rated` is True, `i` is the index of the first inconsistent rating, the string 'rated' has been printed to the console, and at least one `ratings_before[i]` is not equal to `ratings_after[i]`. If `rated` is False, `i` is `n-1`, and for all indices `j` in range `n`, `ratings_before[j]` is equal to `ratings_after[j]`. In the case of `rated` being False, if `unrated` is True, 'unrated' has been printed to the console; otherwise, 'maybe' has been printed to the console because there exists at least one participant who has a lower rating before but a higher rating after.
#Overall this is what the function does:The function determines the outcome of a round based on the change in participant ratings. It accepts two lists of participant ratings before and after a round, where each rating is a positive integer and the number of participants is between 2 and 1000. The function checks if the ratings have changed and if the changes are consistent with the standings. If any rating has changed, it prints 'rated'. If no ratings have changed, it checks if there are any participants who have a lower rating before but a higher rating after. If such a participant exists, it prints 'maybe'. Otherwise, it prints 'unrated'. The function handles edge cases where the number of participants is between 2 and 1000 and each participant's rating is a positive integer. It also considers the case where no participant has a lower rating before but a higher rating after, and where at least one participant has a changed rating. However, the function does not handle potential errors such as non-integer or non-positive input ratings, or a number of participants outside the specified range. The function's output is one of three strings: 'rated', 'unrated', or 'maybe', indicating the outcome of the round based on the change in ratings.

