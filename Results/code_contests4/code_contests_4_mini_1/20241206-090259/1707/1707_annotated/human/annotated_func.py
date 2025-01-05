#State of the program right berfore the function call: n is an integer between 1 and 100 (inclusive), and the array consists of n non-negative integers, each less than 2^30.
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100, `a[i]` is the XOR of all previous elements in `a` from `a[0]` to `a[i]` for `i` in range 1 to `n`.
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `n` is between 1 and 100; `i` is `n + 1`; `ans` is the maximum XOR value from the pairs of `a[i]` and `a[j]` for all `j` in the range from 0 to `n - 1`; `a[i]` is the XOR of all previous elements in `a` from `a[0]` to `a[i]` for `i` in range 1 to `n`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (between 1 and 100, inclusive) and an array of `n` non-negative integers (each less than \(2^{30}\)). It computes the cumulative XOR of the elements in the array, then finds and prints the maximum XOR value obtained from any pair of these cumulative values.

