#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and for each of the next n lines, a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126 representing the ratings before and after the round for each participant in ordered standings.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \( 2 \leq n \leq 1000 \); `ratings_before` contains `n` values which are the input integers corresponding to `a`; `ratings_after` contains `n` values which are the input integers corresponding to `b`; `a` is the last input integer received; `b` is the last input integer received.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000, `unrated` is False if there exists at least one pair `(i, j)` such that `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`; otherwise, `unrated` is True. `i` is the index of the last evaluated element in `ratings_before`, `j` is the index of the last evaluated element in `ratings_before`, and both are within the range of `n`. `rated` is still False, and `maybe` remains True.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000, `rated` is True if there is at least one index `i` such that `ratings_before[i]` is not equal to `ratings_after[i]`, otherwise `rated` is False; `i` is 0 to `n-1` depending on the number of iterations; `unrated` remains unchanged based on the relationship of `ratings_before` and `ratings_after`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000. If `unrated` is true, 'unrated' is printed. Otherwise, if `unrated` is false, the function outputs 'maybe', maintaining that `rated` is False and that all elements `ratings_before[i]` are equal to `ratings_after[i]` for all indices `i` from 0 to `n-1`.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000. If `rated` is True, there is at least one index `i` (where `i` is in the range 0 to `n-1`) such that `ratings_before[i]` is not equal to `ratings_after[i]`, and the string 'rated' has been printed, with `unrated` remaining unchanged. If `rated` is False, and `unrated` is true, the string 'unrated' is printed. Otherwise, if `unrated` is false, the function outputs 'maybe', indicating that all elements `ratings_before[i]` are equal to `ratings_after[i]` for all indices `i` from 0 to `n-1`.
#Overall this is what the function does:The function processes ratings for a specified number of participants and classifies the outcome based on the relationship between their ratings before and after a round. It accepts an integer `n` indicating the number of participants and `n` pairs of integers representing their ratings before (`a_i`) and after (`b_i`) the round. After evaluating these ratings, the function prints one of three possible outcomes: 'rated' if at least one participant's before and after ratings differ, 'unrated' if there are no pairs where a participant with a lower before rating has a higher after rating than another participant, and 'maybe' if all participants have the same ratings before and after. The function ensures that all comparisons and evaluations stay within the specified limits for input sizes.

