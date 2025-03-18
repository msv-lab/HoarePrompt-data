#State of the program right berfore the function call: The function should accept two parameters: an integer t (1 ≤ t ≤ 10^4) representing the number of test cases, and a list of tuples, where each tuple contains an integer n (1 ≤ n ≤ 10^5) and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9). The sum of the values of n over all test cases does not exceed 2 · 10^5.
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: The variable `t` is unchanged. The list of tuples is unchanged. The loop iterates `t` times, and for each tuple, it reads `n` and the list `a`, sorts `a`, calculates the count of the middle element (or the element just before the middle if `n` is even), and prints this count. The variables `n`, `a`, `p`, and `res` are updated in each iteration but their final values after the loop are not retained.
#Overall this is what the function does:The function `func` reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `n` integers. It sorts the list, finds the count of the middle element (or the element just before the middle if `n` is even), and prints this count. The function does not return any value; it only prints the results to the console. The input parameters `t` and the list of tuples are not modified.

