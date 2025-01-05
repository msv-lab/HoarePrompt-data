#State of the program right berfore the function call: N is a positive integer between 1 and 100, and a_i values are integers between 0 and 1000 for 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer `N` from the input and then reads a list of integers `a` of length `N`. It calculates the absolute difference between the maximum and minimum values in the list `a` using numpy functions, and prints the result. The function does not return any specific output. The code processing is dependent on the input N and the values in list `a`.

