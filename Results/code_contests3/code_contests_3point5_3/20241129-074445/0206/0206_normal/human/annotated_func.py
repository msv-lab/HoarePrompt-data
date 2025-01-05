#State of the program right berfore the function call: N is a positive integer, a_i is an integer, and 0 <= a_i <= 1000 for each i where 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `N` from the input, followed by `N` integers `a_i` within the range [0, 1000]. It then calculates the absolute difference between the maximum and minimum values in the list `a`, and prints the result. The function does not explicitly return any value.

