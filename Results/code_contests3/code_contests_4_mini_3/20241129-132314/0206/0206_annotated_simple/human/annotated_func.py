#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts a positive integer `N` (1 ≤ N ≤ 100) and a list of `N` integers `a` (where each integer `a_i` satisfies 0 ≤ a_i ≤ 1000). It calculates and prints the absolute difference between the maximum and minimum values in the list `a`. However, it does not return any value, and the input is read directly from standard input. Additionally, the function does not handle cases where the input does not meet the specified constraints (e.g., if `N` is outside the range or if the list `a` does not contain exactly `N` integers).

