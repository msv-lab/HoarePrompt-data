#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 10^3) representing the number of test cases. Each of the following t lines contains two integers n (1 ≤ n ≤ 100) and k (0 ≤ k ≤ n * (n - 1) / 2) representing the number of islands and the maximum number of bridges Dominater can destroy, respectively.
def func():
    t = int(input())
    for i in range(0, t, 1):
        n, k = map(int, input().split())
        
        if k >= n - 1:
            print(1)
        else:
            print(n)
        
    #State: `t` is unchanged, `n` and `k` are undefined after the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of the number of islands (`n`) and the maximum number of bridges (`k`) that can be destroyed. For each test case, it outputs `1` if the number of bridges that can be destroyed is at least `n - 1`; otherwise, it outputs `n`.

