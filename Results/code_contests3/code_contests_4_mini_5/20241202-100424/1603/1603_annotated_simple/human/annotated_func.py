#State of the program right berfore the function call: n is a positive integer representing the number of flowers (1 ≤ n ≤ 1000), m is a positive integer representing the number of visitors (1 ≤ m ≤ 1000), and each visitor's segment defined by l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n.
def func():
    n, m = map(int, raw_input().split())
    print('10' * (n // 2) + ('1' if n & 1 else ''))
#Overall this is what the function does:The function accepts two positive integers, `n` (number of flowers) and `m` (number of visitors), and generates a string representing a sequence of flower identifiers. Each flower identifier is '10' repeated for each complete pair of flowers, and if `n` is odd, it appends '1' at the end. The function does not utilize the visitor segments defined by `l_i` and `r_i`, meaning it does not consider how many visitors there are or how they might interact with the flowers. Therefore, it primarily focuses on generating a string based on the count of flowers, disregarding the visitor information.

