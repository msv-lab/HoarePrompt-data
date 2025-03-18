#State of the program right berfore the function call: The input consists of an integer n (2 ≤ n ≤ 1000) followed by n pairs of integers (a_i, b_i) where 1 ≤ a_i, b_i ≤ 4126, representing the ratings of the i-th participant before and after the round, respectively. The pairs are ordered according to the standings from top to bottom.
def func():
    n = int(input())
    ratings_before = []
    ratings_after = []
    for _ in range(n):
        a, b = map(int, input().split())
        
        ratings_before.append(a)
        
        ratings_after.append(b)
        
    #State of the program after the  for loop has been executed: `n` is an integer between 2 and 1000; `ratings_before` contains `n` instances of input integers `a`; `ratings_after` contains `n` instances of input integers `b`.
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
        
    #State of the program after the  for loop has been executed: `unrated` is False if there exists at least one pair of indices (i, j) such that `ratings_before[i] < ratings_before[j]` and `ratings_after[i] > ratings_after[j]`; `n` is an integer between 2 and 1000; `i` is less than or equal to `n-1`, `j` is less than or equal to `n-1`, and `ratings_before` and `ratings_after` are lists containing `n` instances of input integers. If no such pairs are found, then `unrated` remains True.
    for i in range(n):
        if ratings_before[i] != ratings_after[i]:
            rated = True
            break
        
    #State of the program after the  for loop has been executed: `unrated` is False, `rated` may be True or remain unchanged, `n` is an integer between 2 and 1000, `i` is `n`, `ratings_before` and `ratings_after` are unchanged. If no changes are found between any indices after checking all `n` elements, `rated` remains False, indicating that the ratings were the same before and after; otherwise, `rated` is set to True if any difference was found.
    if rated :
        print('rated')
    else :
        if unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *If `unrated` is True, then `rated` may be True or remain unchanged, `n` is an integer between 2 and 1000, `i` is `n`, and `ratings_before` and `ratings_after` are unchanged. If `unrated` is False, then `rated` may be True or remain unchanged, `n` is an integer between 2 and 1000, `i` is `n`, `ratings_before` and `ratings_after` are unchanged, and 'maybe' has been printed.
    #State of the program after the if-else block has been executed: *`unrated` is False, if `rated` is True, the output 'rated' is printed. If `unrated` is True, then `rated` may be True or remain unchanged, `n` is an integer between 2 and 1000, `i` is `n`, `ratings_before` and `ratings_after` are unchanged, and the output 'maybe' is printed. If `unrated` is False, then `rated` may be True or remain unchanged, `n` is an integer between 2 and 1000, `i` is `n`, and `ratings_before` and `ratings_after` are unchanged.
#Overall this is what the function does:The function accepts an integer `n` (2 ≤ n ≤ 1000) followed by `n` pairs of integers representing participant ratings before and after a round. It checks if the ratings have changed for any participant; if any rating has changed, it prints "rated." If the ratings haven't changed for any participant, it checks if there is a ranking inconsistency (i.e., if a participant with a lower initial rating has a higher final rating) and prints "maybe" if such inconsistency exists; otherwise, it prints "unrated." If both the rating changes and ranking inconsistencies are missing, it will still print either "unrated" or "maybe" based on comparisons between the ratings, but will not account for cases where ratings are unchanged due to being equal initially and finally across the board. Therefore, the logic concerning ranking is solely evaluated when no rated status is found.

