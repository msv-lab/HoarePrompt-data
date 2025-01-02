#State of the program right berfore the function call: n is a positive integer such that 1 ≤ n ≤ 2·10^5, and a1, a2, ..., an are integers such that -10^9 ≤ ai ≤ 10^9, representing the numbers on the cubes after Dima's reordering.
def func():
    n = int(raw_input())
    values = raw_input().split()
    for i in range(0, n // 2, 2):
        j = n - 1 - i
        
        values[i], values[j] = values[j], values[i]
        
    #State of the program after the  for loop has been executed: `n` is a positive integer such that \(1 \leq n \leq 2 \times 10^5\), `a1, a2, ..., an` are integers such that \(-10^9 \leq ai \leq 10^9\), `values` is a list of strings where elements at indices \(0\) and \(n-1\), \(2\) and \(n-3\), \(4\) and \(n-5\), and so on, have been swapped up to the midpoint of the list.
    print(' '.join(values))
#Overall this is what the function does:The function reads an integer `n` and a space-separated list of `n` integers from the user. It then swaps elements at even indices (0, 2, 4, ...) with their corresponding elements from the end of the list (n-1, n-3, n-5, ...), up to the midpoint of the list. The function prints the modified list as a space-separated string. If `n` is odd, the middle element remains unchanged. If `n` is less than 2, no swaps occur. The function does not handle invalid input (e.g., non-integer values or out-of-range integers) and assumes the input is always valid.

