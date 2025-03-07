#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 5000. Each of the following t test cases consists of two lines: the first line contains an integer n such that 1 ≤ n ≤ 50, and the second line contains 2n integers a_1, a_2, ..., a_{2n} such that 1 ≤ a_i ≤ 10^7 for each i.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: `t` is 0, and the loop has finished executing all test cases.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of an integer `n` and a list of `2n` integers. For each test case, it sorts the list and computes the sum of the elements at even indices (0-based), then prints this sum.

