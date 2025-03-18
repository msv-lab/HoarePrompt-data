#State of the program right berfore the function call: n is an integer representing the number of cards in your hand, and a is a list of n integers where each integer is between 1 and n inclusive, representing the integers on the cards in your hand. It is guaranteed that each integer from 1 through n appears in the list a at most 2 times.
def func_1(n, a):
    counter = Counter(a)
    pairs = sum(1 for count in counter.values() if count == 2)
    return min(pairs, n // 2)
    #The program returns the minimum value between the number of pairs (integers with a count of exactly 2) found in the counter and half the number of cards in your hand (`n // 2`).
#Overall this is what the function does:The function accepts two parameters: `n`, an integer representing the number of cards in your hand, and `a`, a list of `n` integers where each integer is between 1 and `n` inclusive. The function returns the minimum value between the number of pairs (integers with a count of exactly 2) found in the list `a` and half the number of cards in your hand (`n // 2`).

#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n and appears at most twice in the list.
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
        
    #State: Output State: `t` must be greater than 0; `idx` is increased by the total length of all lists `a` (which is 3 * n), plus 3 (for the increments and the initial value of `t`); `results` is a list to which the return value of `func_1(n, a)` has been appended three times, with each `n` and corresponding `a` being derived from the slices of `data` as per the loop's logic; `n` is the last integer obtained from `data[idx]`, and `a` is the list of integers obtained from the slice of `data` starting from `idx` and of length `n`.
    #
    #This means that after the loop has executed all its iterations, `t` should still be greater than 0, `idx` will point to the position right after the last processed list `a`, `results` will contain the results of applying `func_1(n, a)` three times, and `n` and `a` will be set based on the final iteration of the loop.
    for result in results:
        print(result)
        
    #State: `results` must contain exactly three elements, `t` must be greater than 0, `idx` must point to the position right after the last processed list `a`, and `n` and `a` must be set based on the final iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, each defined by an integer `t`, followed by `t` groups of data. Each group contains an integer `n` and a list `a` of `n` integers. For each group, it calls `func_1(n, a)` three times, collects the results, and prints them. The function does not return any value but modifies a list `results` to store the output of `func_1` and prints the contents of `results` after processing all groups.

