#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. The list of integers c_1, c_2, ..., c_n represents the numbers written on the cards and each c_i is an integer such that 1 ≤ c_i ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: For each of the `t` test cases, the output will be `k - 1`. The values of `n`, `k`, and the list `l` will be different for each test case based on the input, but the output for each test case will specifically be the value of `k - 1`.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list of `n` integers. It then prints `k - 1` for each test case.

