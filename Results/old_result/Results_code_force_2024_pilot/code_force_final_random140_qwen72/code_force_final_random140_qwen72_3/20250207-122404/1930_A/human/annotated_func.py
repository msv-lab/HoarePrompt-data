#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 5000, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where 1 ≤ a_i ≤ 10^7, representing the numbers written on the whiteboard.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, `n` is an input integer where 1 ≤ n ≤ 50, `A` is a list of 2n integers where 1 ≤ a_i ≤ 10^7.
#Overall this is what the function does:The function reads an integer `t` indicating the number of test cases. For each test case, it reads an integer `n` and a list of 2n integers. It then prints the sum of the elements at even indices (0-based) of the list for each test case. After processing all test cases, the function terminates with `t` set to 0.

