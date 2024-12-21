#State of the program right berfore the function call: n is a positive integer such that 1 <= n <= 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function prompts the user for a positive integer input \( n \) within the range \( 1 \leq n \leq 10^9 \). It then computes and prints the result of the expression \( 2 \times (\text{bit length of } n - 1) + 2 \). This calculation effectively determines the number of bits required to represent \( n \) in binary, adjusted by a constant. The function does not return any values, but it produces an output based on the input \( n \). There is no error handling for invalid inputs or numbers outside the specified range, which can lead to runtime errors.

