#State of the program right berfore the function call: n is a positive integer such that 2 ≤ n ≤ 10^18.
def func():
    n = int(input())
    print(n.bit_length() - 1)
#Overall this is what the function does:The function reads a positive integer n from user input, where n is constrained to be between 2 and \(10^{18}\). It then calculates and prints the binary length of n minus one, effectively outputting the highest power of 2 less than or equal to n. However, the function does not explicitly handle any edge cases related to the input, such as ensuring that n is indeed within the specified range or providing any indication of invalid input. The function neither takes parameters nor returns a value; it directly interacts with the user via input and output.

