#State of the program right berfore the function call: s is a positive integer such that 2 ≤ s ≤ 10^12, and x is a non-negative integer such that 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is a positive integer such that 2 ≤ `s` ≤ 10^12, `x` is a non-negative integer such that 0 ≤ `x` ≤ 10^12, `count` is the number of pairs `(a, b)` such that `a + b = s` and `a XOR b = x`, where `a` ranges from 1 to `s - 1`, and `b` is equal to `s - a`.
    print(count)
#Overall this is what the function does:The function accepts no parameters, reads two integers from input, and counts the number of pairs `(a, b)` such that `a + b = s` and `a XOR b = x`, then prints this count.

