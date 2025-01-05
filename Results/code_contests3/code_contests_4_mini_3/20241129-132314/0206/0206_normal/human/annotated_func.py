#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts no parameters and reads an integer N from input, followed by a list of N integers. It calculates and prints the absolute difference between the maximum and minimum values in the list. However, the function does not handle cases where the input is invalid (e.g., if N does not match the number of integers provided) or where the input contains non-integer values.

