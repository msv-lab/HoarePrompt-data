#State of the program right berfore the function call: s is a positive integer such that 2 ≤ s ≤ 10^12, and x is a non-negative integer such that 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is a positive integer such that 2 ≤ `s` ≤ 10^12, `x` is a non-negative integer such that 0 ≤ `x` ≤ 10^12, `count` is the number of pairs `(a, b)` such that `1 ≤ a < s`, `b = s - a`, and `a ^ b = x`
    print(count)
#Overall this is what the function does:The function accepts two integers `s` (2 ≤ s ≤ 10^12) and `x` (0 ≤ x ≤ 10^12) from user input, and counts the number of pairs `(a, b)` such that `1 ≤ a < s`, `b = s - a`, and `a XOR b = x`. It then prints the count of such pairs. The function does not return a value.

