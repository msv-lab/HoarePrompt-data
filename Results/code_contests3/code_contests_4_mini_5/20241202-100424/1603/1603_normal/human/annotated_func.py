#State of the program right berfore the function call: n and m are integers such that 1 ≤ n, m ≤ 1000, and each of the m subsequent lines contains two integers l_i and r_i such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two integers, `n` and `m`, where `n` determines the length of the output string and `m` is not utilized in the function. It constructs and prints a string consisting of '10' repeated `n // 2` times, followed by '1' if `n` is odd. The function does not process the `m` pairs of integers as mentioned in the annotations, making the handling of `m` irrelevant to the output.

