#State of the program right berfore the function call: t is a positive integer, and for each test case, n is a positive integer such that 1 ≤ n ≤ 10^5, and a is a list of n integers where each integer is in the range 1 to 10^9 inclusive.
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
        
    #State: Output State: The final output state after the loop executes all its iterations is as follows: `a` is a sorted list of integers obtained from the last input provided by the user; `p` is calculated as `(n + 1) // 2 - 1` using the value of `n` from the last iteration; `res` is the count of elements in `a` that are equal to the element at index `p`; `n` is an integer input from the user during the last iteration; `t` is the total number of iterations the loop executed, which is an integer greater than 0; `res` holds the count of elements in `a` that are equal to the element at index `p` after all iterations.
    #
    #This means that after all iterations, `res` will contain the count of the median element(s) in the final list `a` that was sorted and processed in the last iteration of the loop.
#Overall this is what the function does:The function processes a series of test cases, where for each case, it reads a positive integer \( n \), followed by a list of \( n \) integers. It sorts the list and calculates the count of the middle element (or the average of the two middle elements if \( n \) is even) in the sorted list. The function prints this count for each test case.

