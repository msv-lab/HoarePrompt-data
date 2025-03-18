#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers in `a` that appear exactly 2 times and half the number of cards each player receives (`n // 2`).
#Overall this is what the function does:The function takes a positive integer `n` and a list `a` of `n` integers, where each integer from 1 through `n` appears at most twice. It returns the minimum value between the number of integers in `a` that appear exactly twice and half the number of cards each player receives (`n // 2`).

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
        
    #State: `n` is the integer value of `data[idx - 1]` from the last iteration, `a` is a list of integers from `data[idx - n - 1:idx - 1]` from the last iteration, `data` is a list of strings, `idx` is the position right after the last processed segment of data, `t` is 0, `results` is a list containing the output of `func_1(n, a)` for each of the initial `t` iterations.
    for result in results:
        print(result)
        
    #State: `n` is the integer value of `data[idx - 1]` from the last iteration, `a` is a list of integers from `data[idx - n - 1:idx - 1]` from the last iteration, `data` is a list of strings, `idx` is the position right after the last processed segment of data, `t` is 0, `results` is a list containing all the elements processed by the loop, and `result` is the last element of `results`.
#Overall this is what the function does:The function reads input from standard input, processes multiple test cases where each test case consists of a number `n` and a list `a` of `n` integers, and prints the result of processing each test case. The processing involves determining if the list `a` contains pairs of each integer from 1 through `n`. If it does, the function prints `True`; otherwise, it prints `False`.

