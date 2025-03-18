#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000, n is an integer such that 1 ≤ n ≤ 50, and a is a list of 2n integers such that 1 ≤ a_i ≤ 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, `n` is a new input integer such that 1 ≤ n ≤ 50, `a` is a list of 2n integers such that 1 ≤ a_i ≤ 10^7, `A` is now a sorted list of integers provided by the user.
#Overall this is what the function does:The function `func` reads an integer `t` from the user, which represents the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers from the user, sorts the list, and prints the sum of the elements at even indices. After processing all test cases, the function terminates with `t` being 0. The function does not return any value.

