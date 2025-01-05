#State of the program right berfore the function call: N is a positive integer between 1 and 100, a_i are integers between 0 and 1000 for 1 ≤ i ≤ N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `N` and a list of integers `a_i` from user input. It then calculates the absolute difference between the maximum and minimum values in the list `a` using numpy functions. Finally, it prints the calculated absolute difference as the output. The function does not explicitly return any value.

