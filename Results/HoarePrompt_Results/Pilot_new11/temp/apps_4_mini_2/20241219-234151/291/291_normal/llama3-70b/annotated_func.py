#State of the program right berfore the function call: n is a single integer representing the number of squares that Sofia wants to draw, where 1 <= n <= 10^9.
def func():
    n = int(input())
    print(2 * (n.bit_length() - 1) + 2)
#Overall this is what the function does:The function reads an integer input `n` from the user, which represents the number of squares Sofia wants to draw (where 1 <= n <= 10^9). It then calculates and prints the perimeter length of a square arrangement based on the bit length of `n` by using the formula `2 * (n.bit_length() - 1) + 2`. However, the function does not return this value nor does it provide any handling for cases where the input might be out of the specified range or invalid. The final state of the program will be that it outputs an integer representing a calculated value based on the input `n`, but it does not store or return this result for further use.

