#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each integer a_i satisfies 1 <= a_i <= 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: t is 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then outputs the sum of the smallest `n` integers from the list.

