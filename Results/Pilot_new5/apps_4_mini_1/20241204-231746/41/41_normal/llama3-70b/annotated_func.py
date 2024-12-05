#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 1000, and for each participant i (0 ≤ i < n), a_i and b_i are integers such that 1 ≤ a_i, b_i ≤ 4126, where a_i is the rating before the round and b_i is the rating after the round.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ n ≤ 1000; `ratings_before` contains `n` integers obtained from user input; `ratings_after` contains `n` integers obtained from user input.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `ratings_before` contains `n` integers; `ratings_after` contains `n` integers; `rated` remains False or True depending on the conditions met during the loop; `unrated` is either False (at least one valid condition was found) or True (no valid conditions were found); `maybe` remains True; `i` is `n-1` after the outer loop completes; `j` is beyond the last index, indicating all relevant comparisons have been made.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 ≤ `n` ≤ 1000; `rated` is True if at least one pair of ratings differs between `ratings_before` and `ratings_after`, otherwise `rated` remains False; `unrated` is True if all pairs of ratings are equal, otherwise `unrated` is False; `i` is `n` after all iterations of the loop are complete; `j` remains beyond the last index.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000; if `unrated` is True, the output is 'unrated'. If `unrated` is False and `rated` is False, the output is 'maybe'.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 ≤ `n` ≤ 1000. If `rated` is True, then `unrated` is False, `i` is `n`, `j` remains beyond the last index, and 'rated' has been printed. Otherwise, if `unrated` is True, the output is 'unrated'; if `unrated` is False and `rated` is False, the output is 'maybe'.
#Overall this is what the function does:The function accepts an integer `n` representing the number of participants and their respective ratings before and after a round of competition. It reads `n` pairs of ratings and determines whether the results are classified as 'rated', 'unrated', or 'maybe' based on the following conditions: if any participant's before rating differs from their after rating, it outputs 'rated'; if all participants have the same ratings before and after, it outputs 'unrated'; otherwise, it outputs 'maybe' if there is at least one pair of ratings where the before rating is less than the after rating while the overall ratings are not all equal.

