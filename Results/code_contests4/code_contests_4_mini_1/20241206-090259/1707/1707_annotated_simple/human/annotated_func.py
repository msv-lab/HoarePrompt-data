#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the second line contains n non-negative integers each strictly less than 2^30.
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `a[i]` is the cumulative XOR of `a[0]` through `a[i]` for all `1 ≤ i ≤ n`
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `ans` is the maximum XOR of all pairs `a[i]` and `a[j]` for `1 ≤ i ≤ n` and `0 ≤ j < i`, `n` is an integer such that 1 ≤ `n` ≤ 100.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and reads `n` non-negative integers (each strictly less than 2^30) from input. It computes the cumulative XOR of these integers and finds the maximum XOR value that can be obtained from any two distinct elements in this list, including the cumulative values and the initial zero. The result is printed as output.

