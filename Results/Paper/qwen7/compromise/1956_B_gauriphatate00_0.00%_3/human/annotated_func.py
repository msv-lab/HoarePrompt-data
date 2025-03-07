#State of the program right berfore the function call: n is an integer representing half the number of cards, and a is a list of integers where each integer is between 1 and n, inclusive, and appears at most twice in the list.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of counts in `counter.values()` that are equal to 2 and `n // 2`
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing half the number of cards, and `a`, a list of integers where each integer is between 1 and n, inclusive, and appears at most twice in the list. It calculates the number of elements in the list `a` that appear exactly twice and returns the minimum value between this count and `n // 2`.

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, representing the number of cards you and Nene receive initially. The list a contains n integers, where each integer a_i satisfies 1 ≤ a_i ≤ n, representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the list a at most 2 times, and the sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: `t` is the integer value of `data[0]`, `n` is an integer such that 1 ≤ n ≤ 2⋅10^5, `data` is a list of strings obtained by splitting the input on whitespace, `idx` is `2 + 2*t`, `results` is a list of length `t` where each element is the result of calling `func_1(n, a)` with appropriate parameters.
    for result in results:
        print(result)
        
    #State: t is the integer value of data[0], n is an integer such that 1 ≤ n ≤ 2⋅10^5, data is a list of strings obtained by splitting the input on whitespace, idx is 2 + 2*t, results is a list of length t where each element is the result of calling func_1(n, a), and the loop has printed each element in the results list once.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of integers. For each test case, it calls `func_1(n, a)` to compute a result and stores these results in a list. After processing all test cases, it prints each result from the list. The function does not return any value directly but modifies a list (`results`) and prints the computed results.

