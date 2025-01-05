#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts a positive integer N (1 ≤ N ≤ 100) and a list of N integers a, where each integer satisfies 0 ≤ a_i ≤ 1000. It calculates the absolute difference between the maximum and minimum values of the list and prints this difference. However, the function does not handle any input errors or validate that the input list contains exactly N integers, which could lead to unexpected behavior if the input does not match the expected format.

