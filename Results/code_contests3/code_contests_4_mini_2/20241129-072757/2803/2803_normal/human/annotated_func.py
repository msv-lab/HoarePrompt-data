#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function accepts two integers, `n` and `k`, through user input. It returns `n` if `k` is equal to 1; otherwise, it calculates and returns \(2^{\text{len}(\text{bin}(n)[2:])} - 1\), which represents the maximum value that can be represented with the number of bits required to represent `n`, minus one. The function does not handle cases where `k` is outside the specified constraints, and it does not return any value explicitly; it only prints the result.

