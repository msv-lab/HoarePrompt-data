#State of the program right berfore the function call: **
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user, calculates the absolute difference between the maximum and minimum values of the input array, and prints the result. The function does not accept any parameters and does not return any output. However, the code snippet is missing the necessary import statement for numpy (np) and will result in a NameError when executed.

