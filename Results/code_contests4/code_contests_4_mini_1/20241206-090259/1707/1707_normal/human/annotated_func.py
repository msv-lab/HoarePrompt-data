#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the array consists of n non-negative integers, each strictly less than 2^30.
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `a` is a list where each `a[i]` (for `1 ≤ i ≤ n`) is the cumulative XOR of the elements from `a[0]` to `a[i]`, and `n` is an integer such that 1 ≤ `n` ≤ 100.
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `ans` is the maximum value obtained from the XOR operations between all `a[i]` and `a[j]` for `0 ≤ j < i` across all iterations of the loop, `a` is a list where each `a[i]` (for `1 ≤ i ≤ n`) is the cumulative XOR of the elements from `a[0]` to `a[i]`, and `n` is an integer such that 1 ≤ `n` ≤ 100.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and an array of `n` non-negative integers (each less than 2^30). It computes the cumulative XOR of the elements in the array, then calculates and prints the maximum XOR value obtained from any two cumulative XOR values in the array. The function does not handle cases where the input is not within the specified constraints, nor does it account for potential input errors, such as non-integer values.

