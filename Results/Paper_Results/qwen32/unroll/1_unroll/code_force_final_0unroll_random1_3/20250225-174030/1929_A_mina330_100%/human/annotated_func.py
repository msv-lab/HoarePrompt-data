#State of the program right berfore the function call: t is an integer such that 1 <= t <= 500. For each test case, n is an integer such that 2 <= n <= 100, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9.
def func():
    ntest = int(input())
    for itest in range(0, ntest, 1):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        print(a[len(a) - 1] - a[0])
        
    #State: `t` remains an integer such that 1 <= t <= 500; `ntest` remains the integer read from the input. The loop has executed `ntest` times, and for each test case, the difference between the maximum and minimum values in the list `a` has been printed.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers, sorts the list, and prints the difference between the maximum and minimum values in the list.

