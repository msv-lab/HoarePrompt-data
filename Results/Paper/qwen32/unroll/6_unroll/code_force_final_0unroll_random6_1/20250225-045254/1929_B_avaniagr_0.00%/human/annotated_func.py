#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each of the next t lines contains two integers n and k where 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for s in [*open(0)][1:]:
        n, k = map(int, s.split())
        
        print((k // 2 + k % 2) * (k < 4 * n - 3) + 2 * n * (k >= 4 * n - 3) + (k ==
            4 * n - 2))
        
    #State: a series of integers, each representing the computed value for each pair (n, k) from the input.
#Overall this is what the function does:The function reads a series of test cases from standard input, where each test case consists of two integers `n` and `k`. For each test case, it computes and prints a specific integer value based on the relationship between `n` and `k`.

