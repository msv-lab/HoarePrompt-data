#State of the program right berfore the function call: n is an integer representing half the number of cards, and a is a list of integers where each integer is between 1 and n (inclusive), representing the integers on the cards in your hand. Each integer from 1 to n appears at most twice in the list a.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of pairs of integers in list 'a' that occur exactly twice (`pairs`) and half the number of cards (`n // 2`).
#Overall this is what the function does:The function accepts an integer `n` representing half the number of cards and a list `a` of integers where each integer is between 1 and `n` (inclusive). It calculates the minimum value between the number of pairs of integers in list `a` that occur exactly twice and half the number of cards (`n // 2`). The function returns this minimum value.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, representing the number of cards in your and Nene's hands. The list a is a list of n integers, where each integer a_i satisfies 1 ≤ a_i ≤ n, representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the list a at most 2 times, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: The loop has executed all its iterations, so `t` is now 0. `idx` is `idx + n` from the last iteration, where `n` is `int(data[idx])`. `a` is a list of integers created by mapping `int` over the slice of `data` from `idx` to `idx + n`. `results` is a list containing the return values of `func_1(n, a)` for each iteration, with a total of `t` elements. `data` remains unchanged throughout the process.
    #
    #In simpler terms, after the loop finishes, `t` is 0 because all iterations are done. `idx` points to the position right after the last list `a` was processed. `a` contains integers from the current position of `idx` to `idx + n`. `results` is a list of function outputs from each iteration of the loop, and `data` stays as it was initially.
    for result in results:
        print(result)
        
    #State: The loop has executed all its iterations, so `t` is now 0. `idx` is pointing to the position right after the last list `a` was processed. `a` contains integers from the current position of `idx` to `idx + n`. `results` is a list of function outputs from each iteration of the loop, with a total of `t` elements (which is 3 in this case). `data` remains unchanged throughout the process.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( t \) representing the number of test cases, followed by \( t \) sets of data. Each set includes an integer \( n \) representing the number of cards, and a list \( a \) of \( n \) integers where each integer appears at most twice. For each test case, the function calls another function `func_1(n, a)` to determine if it is possible to pair the cards such that each pair consists of two cards with the same integer. The function then prints the result for each test case.

