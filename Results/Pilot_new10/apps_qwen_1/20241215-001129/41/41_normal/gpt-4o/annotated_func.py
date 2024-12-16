#State of the program right berfore the function call: The input consists of a single integer n (2 ≤ n ≤ 1000) followed by n lines, each containing two integers a_{i} and b_{i} (1 ≤ a_{i}, b_{i} ≤ 4126).
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
        
    #State of the program after the  for loop has been executed: `n` is within the range 2 ≤ n ≤ 1000, `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\), `is_unrated` is `False`, and `is_rated` is `True` if at least one of the tuples \((a_i, b_i)\) satisfies \(a_i \neq b_i\), otherwise `is_rated` is `False`.
    if (not is_rated) :
        for i in range(1, n):
            if ratings[i - 1][0] < ratings[i][0]:
                is_unrated = True
                break
            
        #State of the program after the  for loop has been executed: `i` is `n`, `n` must be greater than 1, `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\), `is_unrated` is `True`, `is_rated` is `False`.
    #State of the program after the if block has been executed: *`n` is within the range 2 ≤ n ≤ 1000, `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\), `is_unrated` is `True`, and `is_rated` remains unchanged. If the condition inside the if statement is true, `i` is set to `n`, `n` must be greater than 1, and `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\). If the condition inside the if statement is false, `i` is set to `n`, `n` must be greater than 1, and `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\).
    if is_rated :
        print('rated')
    else :
        if is_unrated :
            print('unrated')
        else :
            print('maybe')
        #State of the program after the if-else block has been executed: *`n` is within the range 2 ≤ n ≤ 1000, `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\), and either 'unrated' or 'maybe' is printed to the console. `is_unrated` is `False` and `is_rated` is `False`.
    #State of the program after the if-else block has been executed: *`n` is within the range 2 ≤ n ≤ 1000, `ratings` is a list containing exactly `n` tuples \((a_i, b_i)\), and either 'rated', 'unrated', or 'maybe' is printed to the console. `is_unrated` and `is_rated` are both set to `False`.
#Overall this is what the function does:The function processes a list of \(n\) tuples \((a_i, b_i)\) where \(2 \leq n \leq 1000\) and \(1 \leq a_i, b_i \leq 4126\). It checks if any \(a_i \neq b_i\) to determine if the ratings are rated. If not, it checks if the first elements of consecutive tuples are strictly increasing to determine if the ratings are unrated. If neither condition is met, it prints 'maybe'.

