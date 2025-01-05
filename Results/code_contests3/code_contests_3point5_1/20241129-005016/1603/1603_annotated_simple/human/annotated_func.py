#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 10^3. Each segment [l_i, r_i] is valid with 1 ≤ l_i ≤ r_i ≤ n.**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from input. It then prints a string pattern based on the value of `n`. The pattern consists of the string '10' repeated n//2 times, and if n is odd, it appends '1' to the end. The function does not return any value.

