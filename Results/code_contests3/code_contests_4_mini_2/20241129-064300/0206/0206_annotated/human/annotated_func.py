#State of the program right berfore the function call: N is a positive integer such that 1 ≤ N ≤ 100, and a is a list of N integers where each integer a_i satisfies 0 ≤ a_i ≤ 1000.
def func():
    N = raw_input()
    a = raw_input().split()
    ans = np.abs(np.max(a) - np.min(a))
    print(ans)
#Overall this is what the function does:The function accepts a positive integer N (1 ≤ N ≤ 100) and a list of N integers (0 ≤ a_i ≤ 1000). It calculates the absolute difference between the maximum and minimum values in the list and prints this difference. However, the function does not return any value; it only prints the result. Additionally, it does not handle cases where the input may not conform to the expected format (e.g., if N does not match the number of integers provided in the list).

