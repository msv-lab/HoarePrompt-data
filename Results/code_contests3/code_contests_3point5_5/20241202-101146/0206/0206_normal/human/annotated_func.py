#State of the program right berfore the function call: N is a positive integer. Each a_i is an integer such that 0 <= a_i <= 1000.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads an input N followed by N integers, calculates the absolute difference between the maximum and minimum integers in the list, and prints the result. The function does not accept any parameters explicitly, but it relies on user input.

