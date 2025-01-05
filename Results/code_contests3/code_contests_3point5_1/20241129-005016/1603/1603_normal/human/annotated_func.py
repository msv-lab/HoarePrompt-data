#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 ≤ n, m ≤ 10^3. Each segment defined by l_i and r_i contains at least one flower.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from input, where 1 ≤ n, m ≤ 10^3. It then categorizes flower segments based on these inputs and prints the total number of flowers in each segment. If n is odd, an additional flower is added at the end of the last segment.

