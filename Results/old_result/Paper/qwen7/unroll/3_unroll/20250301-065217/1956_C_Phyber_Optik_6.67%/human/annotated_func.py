#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 500, and for each test case, n is an integer such that 1 ≤ n ≤ 500. Additionally, the sum of n^2 over all test cases does not exceed 5 × 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        sum, r = 0, 0
        
        for i in range(1, n + 1):
            if n * (n + 1) // 2 > i * n:
                r = i
                sum += n * (n + 1) // 2
            else:
                sum += i * n
        
        print(sum, n + r)
        
        for j in range(1, n + r + 1):
            if j <= n:
                print(1, j, end=' ')
                print(*range(1, n + 1))
            else:
                print(2, j % n, end=' ')
                print(*range(1, n + 1))
        
    #State: Output State: The output will consist of `t` pairs of lines, each pair containing a sum and a number `n + r`. For each input `n`, it calculates `sum` based on certain conditions and prints `sum` and `n + r`. Then it prints two blocks of lines. The first block prints `n` lines with the first column being 1 and the second column being numbers from 1 to `n`. The second block prints `r` lines with the first column being 2 and the second column being numbers from 1 to `n` in a cyclic manner.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `t` (1 ≤ t ≤ 500) and an integer `n` (1 ≤ n ≤ 500), where the sum of `n^2` over all test cases does not exceed 5 × 10^5. For each test case, it calculates a sum based on specific conditions and prints the sum along with a number derived from `n` and `r`. It then prints two blocks of lines: the first block contains `n` lines with the first column as 1 and the second column as numbers from 1 to `n`, and the second block contains `r` lines with the first column as 2 and the second column as numbers from 1 to `n` in a cyclic manner.

