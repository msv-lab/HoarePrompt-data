#State of the program right berfore the function call: **Precondition**: 
- N is a positive integer such that 1 ≤ N ≤ 100.
- a_i is an integer for each house i, and 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads the total number of houses in a neighborhood and a list of house numbers. It then calculates the absolute difference between the maximum and minimum house numbers and prints the result. The function does not accept any parameters explicitly, but it assumes the user will input the values for N (total number of houses) and a list of house numbers within the specified constraints. However, the current implementation lacks error handling for invalid inputs, such as non-integer inputs or values outside the specified ranges.

