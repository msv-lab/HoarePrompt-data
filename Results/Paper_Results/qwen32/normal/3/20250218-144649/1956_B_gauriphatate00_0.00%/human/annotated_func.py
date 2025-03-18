#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 through n appears at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of integers that appear exactly twice in the list `a` and half the number of cards each player receives (`n // 2`).
#Overall this is what the function does:The function calculates and returns the minimum value between the number of integers that appear exactly twice in the list `a` and half the number of cards each player receives (`n // 2`).

#State of the program right berfore the function call: n is a positive integer representing the number of cards each player receives, and a is a list of n integers where each integer from 1 to n appears at most 2 times, representing the integers on the cards in your hand.
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
        
    #State: `n` is the value of `n` from the last iteration, `a` is a list of `n` integers derived from `data[idx - n:idx]`, `data` is a list of strings obtained by splitting the input, `idx` is `1 + sum(n_i + 1 for i in range(t))`, `t` is 0, `results` is a list containing the results of `func_1(n, a)` for each iteration.
    for result in results:
        print(result)
        
    #State: `n` is the value of `n` from the last iteration, `a` is a list of `n` integers derived from `data[idx - n:idx]`, `data` is a list of strings obtained by splitting the input, `idx` is `1 + sum(n_i + 1 for i in range(t))`, `t` is 0, `results` is a list containing all the results of `func_1(n, a)` for each iteration, and the loop has printed all elements in `results`.
#Overall this is what the function does:The function reads multiple test cases from the standard input, where each test case consists of a positive integer `n` and a list `a` of `n` integers. It processes each test case using the function `func_1(n, a)` and prints the result for each test case.

