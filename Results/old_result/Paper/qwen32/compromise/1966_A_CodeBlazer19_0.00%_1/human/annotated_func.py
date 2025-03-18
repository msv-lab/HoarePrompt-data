#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500. For each test case, n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100. c_1, c_2, ..., c_n are integers such that 1 ≤ c_i ≤ 100 for each i from 1 to n.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: t is an integer provided by the user such that 1 ≤ t ≤ 500; n and k are integers such that 1 ≤ n ≤ 100 and 2 ≤ k ≤ 100; c_1, c_2, ..., c_n are integers such that 1 ≤ c_i ≤ 100 for each i from 1 to n. The loop has printed "k - 1" t times, where k is the second integer in each of the t input pairs.
#Overall this is what the function does:The function reads an integer `t` representing the number of test cases. For each test case, it reads two integers `n` and `k`, and a list of `n` integers. It then prints `k - 1` for each test case.

