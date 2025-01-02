#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 3·10^5, and the following list, x, is a list of n integers where each integer xi (1 ≤ xi ≤ 10^9) is distinct.
def func():
    n = int(raw_input())
    s = sorted(map(int, raw_input().split()))
    r = 0
    for i in xrange(n):
        r += s[i] * (2 ** (n - 1 - i) - 1 - (2 ** i - 1)) % (1000000000 + 7)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `x` is undefined, `s` is a sorted list of integers from the input, `r` is the sum of `s[i] * (2
    print - r
#Overall this is what the function does:The function reads an integer `n` and a list of `n` distinct integers from the standard input. It then sorts the list of integers and calculates a value `r` based on a specific formula involving powers of 2 and the sorted list. Finally, it prints `-r`. The function ensures that the input list contains distinct integers within the specified range and handles the calculation modulo \(10^9 + 7\). Potential edge cases include the minimum and maximum values of `n` and the constraints on the input integers.

