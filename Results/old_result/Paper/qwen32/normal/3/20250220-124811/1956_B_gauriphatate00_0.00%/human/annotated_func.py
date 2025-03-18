#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times and half of `n`.
#Overall this is what the function does:The function accepts a positive integer `n` representing the number of cards each player receives and a list `a` of `n` integers where each integer from 1 through `n` appears at most 2 times. It returns the minimum value between the number of integers in `a` that appear exactly 2 times and half of `n`.

#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
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
        
    #State: `n` is the integer value of `data[idx]` from the last iteration, `a` is a list of `n` integers derived from `data[idx:idx + n]` from the last iteration, `data` is a list of strings obtained from the input split by whitespace, `idx` is `1 + Σ(n_i) for i in range(t)`, `t` is the total number of iterations, and `results` is a list containing the result of `func_1(n, a)` for each of the `t` iterations.
    for result in results:
        print(result)
        
    #State: results is a list containing all elements corresponding to the number of iterations, and `result` is each element in the list sequentially.
#Overall this is what the function does:The function reads input data representing multiple test cases, where each test case consists of a number of cards `n` and a list of `n` integers `a`. For each test case, it computes and prints a result indicating the distribution of cards to two players such that each player receives `n` cards and the sum of the cards each player receives is as close as possible.

