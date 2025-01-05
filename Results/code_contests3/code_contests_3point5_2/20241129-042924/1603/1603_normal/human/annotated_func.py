#State of the program right berfore the function call: **Precondition**: **n and m are integers such that 1 ≤ n, m ≤ 10^3. Each segment specified by l_i and r_i contains valid indices within the range of flowers (1 ≤ l_i ≤ r_i ≤ n).**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function reads two integers n and m from input, then outputs a string of length n representing the number of segments containing each index i. The string consists of '10' repeated n//2 times, and '1' if n is odd.

