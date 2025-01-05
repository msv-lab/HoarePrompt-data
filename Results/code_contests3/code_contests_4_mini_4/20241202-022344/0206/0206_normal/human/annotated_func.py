#State of the program right berfore the function call: N is an integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts an integer N and a list of N integers, calculates the absolute difference between the maximum and minimum values in the list, and prints this difference. The function does not return any value.

