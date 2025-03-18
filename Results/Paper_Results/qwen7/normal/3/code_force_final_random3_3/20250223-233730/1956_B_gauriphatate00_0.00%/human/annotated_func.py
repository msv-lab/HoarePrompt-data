#State of the program right berfore the function call: n is an integer representing half the number of cards, and a is a list of integers where each integer is between 1 and n, inclusive, and appears at most twice.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of key-value pairs in `counter` where the value is 2 and `n // 2`
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing half the number of cards, and `a`, a list of integers where each integer is between 1 and n, inclusive, and appears at most twice. It counts how many numbers in the list `a` appear exactly twice, then returns the smaller value between this count and `n // 2`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, representing the number of cards you and Nene receive initially. The list a contains n integers such that 1 ≤ a_i ≤ n, representing the integers on the cards in your hand, and each integer from 1 through n appears in the list at most 2 times.
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
        
    #State: Output State: `data` remains unchanged, `idx` is `idx + 3 * n`, `a` is a list of integers from `data[idx-3*n:idx-2*n]` converted using `map(int, ...)`, `results` is a list with elements from each iteration of `func_1(n, a)` appended, totaling `t` elements.
    #
    #In this final state, after all iterations of the loop have completed:
    #- The `data` list remains unchanged throughout the process.
    #- The `idx` variable will have increased by `3 * n` (since it increments by `n` each iteration and the loop runs `t` times).
    #- The `a` list contains integers from the portion of `data` that corresponds to the last iteration's input.
    #- The `results` list contains the outputs of `func_1(n, a)` for each iteration, resulting in a total of `t` elements in the `results` list.
    for result in results:
        print(result)
        
    #State: Output State: `data` remains unchanged, `idx` is `idx + 3 * n`, `a` is a list of integers from `data[idx - 3 * n:idx - 2 * n]` converted using `map(int, ...)`, `results` is a list with `t` elements.
    #
    #In this final state, after all iterations of the loop have completed:
    #- The `data` list remains unchanged throughout the process.
    #- The `idx` variable will have increased by `3 * n` (since it increments by `n` each iteration and the loop runs `t` times).
    #- The `a` list contains integers from the portion of `data` that corresponds to the last iteration's input.
    #- The `results` list contains the outputs of `func_1(n, a)` for each iteration, resulting in a total of `t` elements in the `results` list.
#Overall this is what the function does:The function processes a series of test cases, where each test case includes an integer t (number of test cases), followed by an integer n (number of cards) and a list a of integers. For each test case, it calls `func_1(n, a)` to determine if it's possible to pair up all cards such that each pair consists of two cards with the same integer. It then prints the results of these calls for all test cases. The function does not modify the input data and only uses the input data to compute and print the results.

