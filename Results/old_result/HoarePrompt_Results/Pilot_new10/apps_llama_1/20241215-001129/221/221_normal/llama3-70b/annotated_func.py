#State of the program right berfore the function call: s and x are integers such that 2 <= s <= 10^12 and 0 <= x <= 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is the original input integer, `x` is the original input integer, `a` is `s-1`, `b` is `1`, and `count` is the number of pairs `(a, b)` where `a ^ b == x` for `a` ranging from 1 to `s-1` and `b = s - a`.
    print(count)
#Overall this is what the function does:The function accepts two integers `s` and `x`, where `2 <= s <= 10^12` and `0 <= x <= 10^12`, and prints the number of pairs `(a, b)` where `a` ranges from 1 to `s-1`, `b = s - a`, and `a ^ b == x`.

