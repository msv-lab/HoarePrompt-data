#State of the program right berfore the function call: N is a positive integer. a_i is an integer such that 0 <= a_i <= 1000 for 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user, where the first input `N` is a positive integer representing the number of elements in a list. The second input is a list of integers `a_i` where each integer is between 0 and 1000. The function then calculates the absolute difference between the maximum and minimum values in the list `a`, but it does not return any value, only prints the result. However, the code is missing the necessary import statements for `numpy` and error handling for invalid inputs.

