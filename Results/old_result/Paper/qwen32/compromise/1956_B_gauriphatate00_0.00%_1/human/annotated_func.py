#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of integers of length n where each integer from 1 to n appears at most twice.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers that appear exactly twice in the list `a` and half the number of cards each player receives (`n // 2`).
#Overall this is what the function does:The function takes a positive integer `n` and a list `a` of length `n` containing integers from 1 to `n` (each appearing at most twice) and returns the minimum of the number of integers that appear exactly twice in `a` and half of `n`.

#State of the program right berfore the function call: n is a positive integer representing the number of cards you and Nene each receive, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
def func_2():
    input = sys.stdin.read
    data = input().split()
    idx = 0
    t = int(data[idx])
    idx += 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        
        idx += 1
        
        a = list(map(int, data[idx:idx + n]))
        
        idx += n
        
        results.append(func_1(n, a))
        
    #State: `n` is the number of cards from the last iteration, `a` is the list of integers from the last iteration, `data` is the same list of substrings, `idx` is incremented by `1 + sum(n for each iteration) + t`, `t` is unchanged, `results` is a list of results from `func_1(n, a)` for each iteration.
    for result in results:
        print(result)
        
    #State: n is the number of cards from the last iteration, a is the list of integers from the last iteration, data is the same list of substrings, idx is incremented by 1 + sum(n for each iteration) + t, t is unchanged, results is a list of results from func_1(n, a) for each iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input, where each test case consists of a positive integer `n` and a list `a` of `n` integers. Each integer from 1 through `n` appears at most twice in the list. For each test case, it computes and prints the maximum number of cards that can be matched between you and Nene.

