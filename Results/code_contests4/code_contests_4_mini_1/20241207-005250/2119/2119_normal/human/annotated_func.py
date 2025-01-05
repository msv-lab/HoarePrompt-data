#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 25.
def func():
    print[0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 15, 4, 0, 0, 0, 0, 0][input() - 10]
#Overall this is what the function does:The function does not accept any parameters and takes an integer input from the user, which should be between 1 and 25 inclusive. It then uses this input to access an index in a predefined list, where it prints the value at that index. The list has specific values, and for input values of 10 or less, it will print values from that list. If the input is outside the range of valid indices (1 to 25), it may raise an `IndexError` since it attempts to access an index that does not exist in the list.

