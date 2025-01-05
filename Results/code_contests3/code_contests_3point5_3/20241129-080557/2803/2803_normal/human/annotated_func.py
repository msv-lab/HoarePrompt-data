#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function `func` takes two integer inputs `n` and `k` and calculates the result based on the conditions stated in the code. It uses bitwise operations to calculate the result and prints the output. If `k` is equal to 1, it returns `n`; otherwise, it performs a bitwise operation on `n` and prints the result. The function does not explicitly return any value.

