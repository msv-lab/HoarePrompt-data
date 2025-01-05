#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and a_i are integers such that 0 ≤ a_i ≤ 1000 for i = 1 to N.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts an integer `N` and a list of integers `a_i`, calculates the absolute difference between the maximum and minimum values of the list, and prints this difference. It does not handle input validation or potential errors for user input.

