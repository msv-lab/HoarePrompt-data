#State of the program right berfore the function call: n is an integer between 2 and 1000, and for each participant, a_i and b_i are integers between 1 and 4126 representing the rating before and after the round, respectively.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000, `ratings_before` contains `n` integers representing the values of `a` inputted during each iteration, `ratings_after` contains `n` integers representing the values of `b` inputted during each iteration.
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
        
    #State of the program after the  for loop has been executed: `unrated` is either True or False depending on whether any inconsistencies were found between the ratings_before and ratings_after, with `n` remaining between 2 and 1000.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `unrated` is True if any ratings_before differ from ratings_after, otherwise it is False; `i` is equal to n - 1 if all ratings are the same, or some value less than n - 1 if a difference was found before the last index; `n` is between 2 and 1000.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`unrated` is a boolean indicating if there are differences between `ratings_before` and `ratings_after`. If `unrated` is True, then `i` is either equal to `n - 1` if all ratings are the same or some value less than `n - 1` if a difference was found, while `n` is between 2 and 1000, and `rated` is False, leading to an output of 'unrated'. If `unrated` is False, then `i` is equal to `n - 1`, `n` remains between 2 and 1000, `rated` is False, and 'maybe' has been printed.
    #State of the program after the if-else block has been executed: *`unrated` is a boolean indicating if there are differences between `ratings_before` and `ratings_after`. If `rated` is True, then `unrated` indicates if any ratings differ, `i` can be `n - 1` if all ratings are the same, or some value less than `n - 1` if a difference was found, and `n` is between 2 and 1000. If `rated` is False, then `unrated` reflects whether there are differences; if `unrated` is True, `i` is less than `n - 1`, while if `unrated` is False, `i` equals `n - 1`, and `n` remains in the range of 2 to 1000, leading to different outputs based on the conditions met.
#Overall this is what the function does:The function accepts an integer `n` (between 2 and 1000) representing the number of participants, and then reads two ratings for each participant: `ratings_before` and `ratings_after`, both of which are integers between 1 and 4126. It determines if the results are 'rated' (if any `ratings_before` differ from the corresponding `ratings_after`), 'unrated' (if there are inconsistencies where a lower `ratings_before` corresponds to a higher `ratings_after`), or 'maybe' (if none of the ratings differ, but inconsistencies were found). The outputs are determined based on the conditions of these comparisons.

