#State of the program right berfore the function call: N is a positive integer. a_i is an integer and 0 <= a_i <= 1000 for 1 <= i <= N.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads a positive integer N and a list of N integers a_i. It then calculates the absolute difference between the maximum and minimum values in the list and prints the result. The function does not return any value. The functionality is to find the absolute difference between the maximum and minimum values in the list of integers a_i.

