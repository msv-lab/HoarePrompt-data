#State of the program right berfore the function call: s and x are positive integers such that 2 ≤ s ≤ 10^12 and 0 ≤ x ≤ 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is a positive integer between 2 and 10^12, `x` is a positive integer between 0 and 10^12, `count` is the number of pairs (a, b) such that 1 <= a < s and `a` ^ `b` == `x`, where `b` is always positive and `b` equals `s - a`.
    print(count)
#Overall this is what the function does:The function accepts two positive integers, `s` (ranging from 2 to 10^12) and `x` (ranging from 0 to 10^12), and calculates the number of unique pairs of integers `(a, b)` such that `1 <= a < s`, `b = s - a`, and the bitwise XOR of `a` and `b` equals `x`. It then prints the count of such pairs. The function does not explicitly handle cases where the input might be out of bounds according to the specified ranges, nor does it return or handle the situation when no pairs are found, simply printing `0` in such cases.

