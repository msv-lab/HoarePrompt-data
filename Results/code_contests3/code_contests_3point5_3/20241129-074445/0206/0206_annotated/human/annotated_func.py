#State of the program right berfore the function call: N is a positive integer such that 1 <= N <= 100, and a_i is an integer where 0 <= a_i <= 1000 for each i.**
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function `func` reads input from the user, specifically an integer N followed by N space-separated integers. It then calculates the absolute difference between the maximum and minimum values among the input integers and prints the result. The function does not take any parameters and does not explicitly return any value. However, it should be noted that the code is missing the necessary imports for `raw_input()` and `np`, which would cause errors when running the function.

