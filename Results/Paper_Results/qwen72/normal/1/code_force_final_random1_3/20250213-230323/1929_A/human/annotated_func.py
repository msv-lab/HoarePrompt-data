#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the length of the array a. a is a list of n integers where 1 ≤ a_i ≤ 10^9, representing the elements of the array a.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` is an integer where 1 ≤ t ≤ 500, `n` is an input integer where 2 ≤ n ≤ 100, `a` is a sorted list of integers derived from the input, `ntest` must be equal to the initial value of `ntest`, `itest` is `ntest - 1`.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers `a`. For each test case, it sorts the list `a` and prints the difference between the maximum and minimum values in the sorted list. After processing all test cases, the function completes without returning any value. The state of the program remains unchanged except for the printed output.

