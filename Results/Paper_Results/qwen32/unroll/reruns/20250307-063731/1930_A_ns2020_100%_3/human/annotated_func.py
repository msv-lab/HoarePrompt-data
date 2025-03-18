#State of the program right berfore the function call: t is an integer such that 1 <= t <= 5000. For each test case, n is an integer such that 1 <= n <= 50, and a list of 2n integers a_1, a_2, ..., a_{2n} where each a_i is an integer such that 1 <= a_i <= 10^7.
def func():
    t = int(input())
    while t:
        n = int(input())
        
        A = list(map(int, input().split()))
        
        A.sort()
        
        print(sum(A[::2]))
        
        t = t - 1
        
    #State: The program will print the sum of the smallest elements in each pair for each test case, and `t` will be 0.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads an integer `n` and a list of `2n` integers. It then calculates and prints the sum of the smallest elements in each pair of the sorted list for that test case. After processing all test cases, the function concludes with `t` equal to 0.

