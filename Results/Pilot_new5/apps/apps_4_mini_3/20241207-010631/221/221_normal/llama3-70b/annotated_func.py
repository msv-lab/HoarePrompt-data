#State of the program right berfore the function call: s is a positive integer between 2 and 10^12, and x is a non-negative integer between 0 and 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is a positive integer between 2 and \(10^{12}\), `x` is a non-negative integer between 0 and \(10^{12}\), `count` is equal to the number of pairs (a, b) such that \(a < s\), \(b = s - a\), and \(a \oplus b = x\). If the loop does not execute (when `s` is less than or equal to 1), then `count` remains 0.
    print(count)
#Overall this is what the function does:The function accepts two integers, `s` (a positive integer between 2 and 10^12) and `x` (a non-negative integer between 0 and 10^12), and counts the number of pairs `(a, b)` such that `1 <= a < s`, `b = s - a`, and `a XOR b = x`. It then prints the count of such pairs. If `s` is less than or equal to 1, the count remains 0 since the loop does not execute.

