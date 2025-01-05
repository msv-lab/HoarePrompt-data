#State of the program right berfore the function call: N is a positive integer, a_i is an integer, and 0 <= a_i <= 1000 for 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function does not accept any parameters. It reads an integer N from the user, followed by N integers as input. It then calculates the absolute difference between the maximum and minimum values in the list of integers and prints the result. The function does not return any value. The code does not use `raw_input()` as it is not a valid function in Python, and it also lacks the import statement for numpy, so the code will result in errors.

