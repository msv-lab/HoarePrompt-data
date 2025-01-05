#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `N` (1 ≤ N ≤ 100) and a list `a` of `N` integers (0 ≤ a_i ≤ 1000), calculates the absolute difference between the maximum and minimum values in the list, and prints this difference. However, the function does not validate the input, meaning if the user inputs an invalid value for `N` or the integers in the list, it could lead to unexpected behavior. Additionally, the function uses `raw_input()`, which is typically used in Python 2, and may not function as intended in Python 3 without modification.

