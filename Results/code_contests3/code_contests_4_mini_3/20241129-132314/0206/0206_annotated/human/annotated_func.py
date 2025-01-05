#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and a_i is a list of N integers where each a_i (0 ≤ a_i ≤ 1000) represents the coordinates of the houses.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts an integer `N` (where 1 ≤ N ≤ 100) and a list of `N` integers representing the coordinates of houses. It calculates and prints the absolute difference between the maximum and minimum coordinates in the list. However, it does not return any value, and it relies on `raw_input` which is not compatible with Python 3, making the function potentially non-functional in that environment. Additionally, there is no validation of the input values to ensure they meet the specified constraints.

