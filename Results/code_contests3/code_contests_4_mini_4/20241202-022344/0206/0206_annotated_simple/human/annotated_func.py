#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts a positive integer N and a list of N integers, computes the absolute difference between the maximum and minimum values in the list, and prints the result. However, it does not handle cases where the input is not properly formatted or where N does not match the number of integers provided. Additionally, it uses `raw_input()` which is not defined in Python 3, and the input integers are not converted to an integer type, which could lead to errors in computation.

