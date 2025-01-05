#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ a + b, a is an integer representing the number of pieces of the first cake (1 ≤ a ≤ 100), and b is an integer representing the number of pieces of the second cake (1 ≤ b ≤ 100).
def func():
    n, b, c = [int(x) for x in raw_input().split()]
    x = max(b, c) / float(min(b, c))
    print(int(ceil(min(b, c) / float(n) * x)))
#Overall this is what the function does:The function accepts three integer inputs (n, b, c) read from user input. It calculates the ratio of the maximum of b and c to the minimum of b and c, then computes the minimum of b and c divided by n multiplied by this ratio. Finally, it prints the ceiling of this value as an integer. The function does not directly accept parameters as argued in the annotations; it takes input directly from user input instead.

