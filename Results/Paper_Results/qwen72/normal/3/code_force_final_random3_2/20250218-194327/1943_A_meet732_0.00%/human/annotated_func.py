#State of the program right berfore the function call: The function `func` is expected to be called within a context where it processes multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 2 · 10^5) representing the size of the array `a`, and the array `a` itself, which contains `n` integers (0 ≤ a_i < n). The total number of test cases `t` is an integer (1 ≤ t ≤ 2 · 10^4), and the sum of `n` over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        cntl = [(0) for _ in range(n + 1)]
        
        for i in a:
            cntl[i] += 1
        
        if cntl[0] == 0:
            print(0)
        else:
            c = min(2, cntl[0])
            for j in range(1, n + 1):
                if cntl[j] < 2:
                    c -= 1
                    if not c or j == n:
                        print(j)
                        break
        
    #State: `t` is an integer greater than 0, `_` is `t - 1`, `n` is an input integer, `a` is a list of integers provided by the user, `cntl` is a list of length `n + 1` where each element at index `i` (where `i` is an element in `a`) is the number of times `i` appears in the list `a`. If `cntl[0]` is 0, the program retains all initial conditions. If `cntl[0]` is not 0, `j` is the smallest index in the range 1 to `n` where `cntl[j]` is less than 2, or `n` if no such index exists, and `c` is 0 if `j` is less than `n` and `cntl[j]` is less than 2, otherwise `c` is the minimum of 2 and the first element of `cntl`.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it counts the occurrences of each integer in the array `a`. If the integer `0` does not appear in the array, the function prints `0`. Otherwise, it finds the smallest index `j` in the range 1 to `n` where the integer `j` appears fewer than 2 times in the array, or prints `n` if no such index exists. The function does not return any values; it only prints the results for each test case.

