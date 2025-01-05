#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100, and the array consists of n non-negative integers, each strictly less than 2^30.
def func():
    n = int(raw_input())
    s = raw_input().split()
    a = [0] + [int(s[i]) for i in range(0, n)]
    for i in range(1, n + 1):
        a[i] ^= a[i - 1]
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100; `s` is a list of strings with at least `n` elements; `a[0]` is 0; `a[1]` is unchanged; `a[i]` for `i` from 2 to `n` is the result of the XOR operations applied iteratively, with `i` being `n`.
    ans = 0
    for i in range(1, n + 1):
        for j in range(0, i):
            ans = max(ans, a[i] ^ a[j])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that 1 ≤ `n` ≤ 100, `s` is a list of strings with at least `n` elements, `ans` is the maximum value obtained from the XOR operation between `a[i]` and all previous `a[j]` for all `i` from 1 to `n`, where `0 ≤ j < i`.
    print(ans)
#Overall this is what the function does:The function accepts an integer `n` (1 ≤ n ≤ 100) and an array of `n` non-negative integers (each strictly less than 2^30) from the user input. It computes the maximum XOR value obtainable from any two elements of an internal array, which is derived from the cumulative XOR of the input integers. The function then prints this maximum XOR value. It does not handle cases where the input might not conform to the specified constraints (e.g., non-integer inputs or integers out of the specified range).

