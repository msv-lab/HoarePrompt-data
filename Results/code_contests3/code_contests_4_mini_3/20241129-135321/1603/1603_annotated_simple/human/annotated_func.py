#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000, and for each visitor i, l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function reads two integers, `n` and `m`, from input. It then constructs a string consisting of the digit '10' repeated `n // 2` times, followed by '1' if `n` is odd, or an empty string if `n` is even. This string is printed to the output. The function does not return any value, and the specific role of the integer `m` and visitor ranges is not utilized in the code.

