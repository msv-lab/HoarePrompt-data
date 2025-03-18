#State of the program right berfore the function call: s and x are integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is the original input integer, `x` is the original input integer, `count` is the number of pairs of integers `(a, b)` where `1 <= a < s`, `b = s - a`, and `a ^ b == x`. If `s` is less than or equal to 1, the loop does not execute, and `count` remains 0.
    print(count)
#Overall this is what the function does:The function accepts two integer parameters `s` and `x` from the user input, where `s` and `x` are integers such that 2 ≤ `s` ≤ 10^12 and 0 ≤ `x` ≤ 10^12. It calculates and prints the number of pairs of integers `(a, b)` where `1 <= a < s`, `b = s - a`, and `a` bitwise XOR `b` equals `x`. The function does not modify the original input integers `s` and `x`, and the output is the total count of such pairs. If the input validation is not enforced by the function itself, it implicitly relies on the problem statement for valid inputs, and the function does not handle cases where `s` or `x` are outside the specified ranges.

