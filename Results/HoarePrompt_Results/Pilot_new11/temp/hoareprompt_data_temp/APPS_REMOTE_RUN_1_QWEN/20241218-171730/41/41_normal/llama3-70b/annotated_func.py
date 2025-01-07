#State of the program right berfore the function call: The input is a list of tuples, where each tuple contains two integers representing the rating of a participant before and after the round, respectively. The list contains exactly n tuples, and n is an integer such that 2 ≤ n ≤ 1000. Each integer in the tuples is between 1 and 4126 inclusive.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `ratings_before` is a list containing `n` input integers, `ratings_after` is a list containing `n` input integers, `n` is a non-negative integer.
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
        
    #State of the program after the  for loop has been executed: `unrated` is `False`, `rated` is `False`, `maybe` is `False`, `ratings_before` is a list containing `n` input integers, `ratings_after` is a list containing `n` input integers, `n` is a non-negative integer, `i` is `n`, and `j` is `n + 1`.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `unrated` is `False`, `rated` is `True` if there exists at least one index `i` such that `ratings_before[i]` is not equal to `ratings_after[i]`, `maybe` is `False`, `ratings_before` is a list of `n` integers, `ratings_after` is a list of `n` integers, `n` is a non-negative integer, `i` is `n`, and `j` is `n + 1`.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`unrated` is `False`, `rated` is `False`, `maybe` is `False`, `ratings_before` is a list of `n` integers, `ratings_after` is a list of `n` integers, `n` is a non-negative integer, `i` is `n`, `j` is `n + 1`. If `unrated` is `True`, no changes are made. Otherwise, we print 'maybe'.
    #State of the program after the if-else block has been executed: *`unrated` is `False`, `rated` is a boolean value (either `True` or `False`), `maybe` is `False`, `ratings_before` is a list of `n` integers, `ratings_after` is a list of `n` integers, where `n` is a non-negative integer, `i` is `n`, and `j` is `n + 1`. If the condition `rated` is `True`, the string 'rated' is printed to the console. Otherwise, if `unrated` is `True`, no changes are made; otherwise, the string 'maybe' is printed to the console.
#Overall this is what the function does:The function accepts a list of tuples, where each tuple contains two integers representing the rating of a participant before and after a round, respectively. The list contains exactly `n` tuples, and `n` is an integer such that 2 ≤ `n` ≤ 1000. Each integer in the tuples is between 1 and 4126 inclusive. The function then determines whether the ratings have changed for all participants, for none of the participants, or for some but not all participants. Specifically, it checks if the ratings of all participants have increased (meaning they are "rated"), if none of the ratings have changed (meaning they are "unrated"), or if the ratings have mixed behavior (meaning the result is "maybe"). The function prints one of three possible outcomes: 'rated', 'unrated', or 'maybe'. The function does not return any value; instead, it prints the outcome directly to the console. Potential edge cases include lists with exactly 2 or 1000 tuples, and integer values at the boundaries of the specified ranges (1 and 4126). The function also handles the case where the ratings do not strictly increase for all participants but do not remain unchanged either, which would otherwise lead to an incorrect "unrated" classification.

