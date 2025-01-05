#State of the program right berfore the function call: N is a positive integer and a_i are integers such that 1 ≤ N ≤ 100, 0 ≤ a_i ≤ 1000 for 1 ≤ i ≤ N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `N` from the user and then reads `N` integers as input. It calculates the absolute difference between the maximum and minimum values of the input integers and prints the result. The function does not return any value. However, the code is missing the import of the numpy library which would cause an error when running the function. Additionally, it lacks error handling for cases where the input is not in the expected format or range.

