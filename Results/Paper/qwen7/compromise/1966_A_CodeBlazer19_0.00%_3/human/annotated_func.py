#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500; for each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; the next line of each test case contains n integers c_1, c_2, ..., c_n such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t lines of "k - 1" where each "k" is an integer read from the input during the corresponding iteration.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads an integer t, followed by pairs of integers n and k, and a list of n integers. It then prints the value k - 1 for each test case. After processing all test cases, the function ends with t lines of output, each containing the value k - 1 from the corresponding test case.

