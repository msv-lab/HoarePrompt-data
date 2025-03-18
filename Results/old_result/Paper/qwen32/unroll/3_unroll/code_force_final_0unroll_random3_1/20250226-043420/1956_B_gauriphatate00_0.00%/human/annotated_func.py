#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times and half the number of cards each player receives (`n // 2`).
#Overall this is what the function does:The function takes a positive integer `n` and a list `a` of `n` integers, where each integer from 1 through `n` appears at most twice. It returns the minimum value between the number of integers in `a` that appear exactly twice and half the number of cards each player receives (`n // 2`).

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
        
    #State: `idx` is the total number of elements processed in `data`, `n` is the value used in the last iteration, `a` is the list of integers used in the last iteration, `t` remains the same, `data` remains the same, and `results` is a list of results from `func_1` for each iteration.
    for result in results:
        print(result)
        
    #State: `idx` is the total number of elements processed in `data`, `n` is the value used in the last iteration, `a` is the list of integers used in the last iteration, `t` remains the same, `data` remains the same, and `results` is a list of results from `func_1` for each iteration.
#Overall this is what the function does:The function reads multiple test cases from standard input. Each test case consists of an integer `n` and a list of `n` integers. For each test case, it computes and prints the number of unique integers that appear exactly once in the list.

