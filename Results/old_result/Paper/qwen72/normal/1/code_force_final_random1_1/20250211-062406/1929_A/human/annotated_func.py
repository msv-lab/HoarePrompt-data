#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 500, representing the number of test cases. For each test case, n is an integer where 2 ≤ n ≤ 100, representing the length of the array a. Each element a_i of the array a is an integer where 1 ≤ a_i ≤ 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` is an integer where 1 ≤ t ≤ 500, `ntest` is equal to `t`, `itest` is `ntest - 1`, `n` is an input integer, `a` is a sorted list of integers read from the input, `ntest` must be greater than or equal to 1.
#Overall this is what the function does:The function reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers, sorts the list, and prints the difference between the maximum and minimum values in the list. The function does not return any value; it only prints the results to the standard output. After processing all test cases, the function terminates.

