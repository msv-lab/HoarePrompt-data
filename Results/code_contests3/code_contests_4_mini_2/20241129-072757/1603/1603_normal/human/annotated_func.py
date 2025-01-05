#State of the program right berfore the function call: n is a positive integer representing the number of flowers (1 ≤ n ≤ 1000), m is a positive integer representing the number of visitors (1 ≤ m ≤ 1000), and each visitor's range (l_i, r_i) are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers, `n` (the number of flowers) and `m` (the number of visitors). It generates and prints a string of '10's repeated for every pair of flowers, alongside a single '1' if `n` is odd. However, the function does not utilize the `m` parameter, nor does it process the visitor ranges, which means it lacks functionality related to visitor interactions with the flowers.

