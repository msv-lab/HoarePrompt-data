#State of the program right berfore the function call: s and x are integers such that 2 <= s <= 10^12 and 0 <= x <= 10^12.
def func():
    s, x = map(int, input().split())
    count = 0
    for a in range(1, s):
        b = s - a
        
        if a ^ b == x:
            count += 1
        
    #State of the program after the  for loop has been executed: `s` is an input integer, `x` is an input integer, `a` is `s - 1`, `b` is `1`, and `count` is the number of times `a ^ b` equals `x` for `a` ranging from 1 to `s - 1`
    print(count)
#Overall this is what the function does:The function accepts two integers `s` and `x` as input, where `2 <= s <= 10^12` and `0 <= x <= 10^12`, and returns the count of pairs of integers `(a, b)` such that `a ^ b == x` and `a + b == s`, where `a` ranges from `1` to `s - 1`. The function effectively calculates the number of ways to express `x` as the bitwise XOR of two numbers whose sum is `s`, and prints this count as its output. The state of the program after execution is that it has consumed the input integers `s` and `x`, and has printed the count of such pairs to the console, with no modifications made to the input values. The function handles all edge cases within the specified input ranges and does not perform any error checking or handling for inputs outside these ranges.

