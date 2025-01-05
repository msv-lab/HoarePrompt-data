#State of the program right berfore the function call: n and m are integers such that 1 <= n, m <= 10^3. Each segment defined by l_i and r_i contains flowers within the range [1, n].**
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function `func` reads two integers `n` and `m` from the input, then prints a string based on the calculation `(10 * (n // 2)) + ('1' if n is odd else '')`. The function does not accept any parameters directly but relies on user input for `n` and `m`. It operates within the constraints of 1 <= n, m <= 10^3, and works with segments containing flowers within the range [1, n]. The function output is a string representing the calculated pattern based on the input `n`.

