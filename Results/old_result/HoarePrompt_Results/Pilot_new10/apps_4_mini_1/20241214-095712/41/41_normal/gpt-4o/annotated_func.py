#State of the program right berfore the function call: n is an integer such that 2 <= n <= 1000, and for each participant i (0 <= i < n), a[i] and b[i] are integers representing their ratings before and after the round, satisfying 1 <= a[i], b[i] <= 4126.
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
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 1000; `ratings` contains `n` tuples of `(a[i], b[i])` for each participant; `is_rated` is True if at least one `a[i]` is not equal to `b[i]`, otherwise it is False; `is_unrated` remains False.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `n` is an integer such that 2 <= `n` <= 1000; `ratings` contains `n` tuples of `(a[i], b[i])` for each participant; `is_rated` is False; `is_unrated` is True if at least one of the tuples has an `a[i]` that is less than the subsequent tuple's `a[i]`; otherwise, `is_unrated` remains False.
    #State of the program after the if block has been executed: *`n` is an integer such that 2 <= `n` <= 1000; `ratings` contains `n` tuples of `(a[i], b[i])` for each participant; `is_rated` is False and `is_unrated` is True if at least one of the tuples has an `a[i]` that is less than the subsequent tuple's `a[i]`; otherwise, `is_unrated` remains False.
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= `n` <= 1000; `ratings` contains `n` tuples of `(a[i], b[i])` for each participant; `is_rated` is False. If `is_unrated` is True, 'unrated' has been printed. Otherwise, if `is_unrated` is False, the output is 'maybe'.
    #State of the program after the if-else block has been executed: *`n` is an integer such that 2 <= `n` <= 1000; `ratings` contains `n` tuples of `(a[i], b[i])` for each participant. If `is_rated` is True, the output is 'rated'. If `is_rated` is False, and `is_unrated` is True, the output is 'unrated'; otherwise, if `is_unrated` is False, the output is 'maybe'.
#Overall this is what the function does:The function accepts an integer `n`, where `n` is the number of participants (2 <= n <= 1000). It reads the ratings before (array `a`) and after (array `b`) a round for each participant. It determines if the round is 'rated' (if any participant's before rating `a[i]` is different from their after rating `b[i]`), 'unrated' (if all before and after ratings are equal but at least one participant has an increasing before rating compared to the previous participant), or 'maybe' (if all before and after ratings are equal and there is no increase).

