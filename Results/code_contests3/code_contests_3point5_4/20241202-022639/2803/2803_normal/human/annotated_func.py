#State of the program right berfore the function call: n and k are integers such that 1 ≤ k ≤ n ≤ 10^18.**
def func():
    n, k = map(int, raw_input().split())
    print(2 ** len(bin(n)[2:]) - 1 if k - 1 else n)
#Overall this is what the function does:The function takes two integer inputs n and k, where 1 ≤ k ≤ n ≤ 10^18. It then calculates and prints the value of nCk, where nCk represents the binomial coefficient "n choose k". The function utilizes bitwise operations to calculate the result, specifically returning 2 raised to the length of the binary representation of n minus 1 if k is not equal to 1, otherwise it returns n.

