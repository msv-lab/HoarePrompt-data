#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the second line contains n space-separated non-negative integers, each strictly less than 2^30.
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ n ≤ 100, `a[i]` is the result of the XOR operation of all preceding elements from `a[0]` to `a[i]` for `1 ≤ i ≤ n.`
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `ans` is the maximum XOR value computed from all pairs `a[i]` and `a[j]` for `0 ≤ j < i` and `1 ≤ i ≤ n`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (where 1 ≤ n ≤ 100) and reads `n` space-separated non-negative integers (each less than 2^30). It calculates the maximum XOR value of all pairs formed by the prefix XORs of the integers, and prints this maximum value.

