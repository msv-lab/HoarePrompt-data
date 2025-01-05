#State of the program right berfore the function call: a is an integer such that 0 <= a <= 15.
def func():
    print([15, 14, 12, 13, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7][int(raw_input())])
#Overall this is what the function does:The function accepts an integer input from the user, uses it as an index to access an element from a fixed list of integers, and prints the element. If the input is outside the range of 0 to 15, it will raise an IndexError.

