#State of the program right berfore the function call: s and x are positive integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `count` is the number of pairs (a, b) such that `1 ≤ a < s`, `b = s - a`, and `a ^ b = x`; `s` is a positive integer between 2 and 10^12; `x` is a positive integer between 0 and 10^12.
    print(count)
#Overall this is what the function does:The function accepts two positive integers `s` and `x` (input via standard input), where `2 ≤ s ≤ 10^12` and `0 ≤ x ≤ 10^12`. It calculates the number of pairs `(a, b)` such that `1 ≤ a < s`, `b = s - a`, and `a ^ b = x`. Finally, it prints the count of such pairs. Note that the function does not return any value; it only prints the result.

