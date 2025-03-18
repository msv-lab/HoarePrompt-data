#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, the first line contains two integers n (1 ≤ n ≤ 100) and k (2 ≤ k ≤ 100), where n is the number of cards and k is the number of cards exchanged during each operation. The second line contains n integers c_1, c_2, ..., c_n (1 ≤ c_i ≤ 100), representing the numbers written on the cards. The total number of test cases, t, satisfies 1 ≤ t ≤ 500.
def func():
    t = int(input())
    for i in range(t):
        n, k = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        print(k - 1)
        
    #State: `t` must be greater than or equal to 0, `i` is `t-1`, `n` and `k` are the integers read from the input during the last iteration, `l` is a list of integers read from the input during the last iteration.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `k`, and a list of `n` integers. For each test case, it outputs `k - 1`.

