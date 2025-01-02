#State of the program right berfore the function call: t is a positive integer where 1 ≤ t ≤ 10^4, and for each of the t test cases, s is a positive integer where 1 ≤ s ≤ 10^9.
def func():
    t = int(input())
    for i in range(t):
        s = int(input())
        
        total = 0
        
        while s > 0:
            ss = str(s)
            spend = int(ss[0]) * 10 ** (len(ss) - 1)
            back = spend // 10
            total += spend
            s = s - spend + back
        
        print(total)
        
    #State of the program after the  for loop has been executed: `t` is an integer within the range 1 ≤ t ≤ 10^4, `i` is `t-1`, `s` is 0 or a non-positive value for each test case, `total` is the sum of all `spend` values calculated during the iterations for each test case, where each `spend` is `int(ss[0]) * 10
#Overall this is what the function does:The function `func` reads an integer `t` from the input, representing the number of test cases, where `1 ≤ t ≤ 10^4`. For each test case, it reads another integer `s` (where `1 ≤ s ≤ 10^9`). The function then calculates a total value by repeatedly spending and adjusting the value of `s` until `s` becomes 0 or a non-positive value. Specifically, in each iteration, it calculates `spend` as the first digit of `s` multiplied by 10 raised to the power of the length of `s` minus one, adds `spend` to `total`, and updates `s` by subtracting `spend` and adding back `spend // 10`. After processing all test cases, the function prints the `total` value for each test case. The function does not return any value; it only prints the results. After the function concludes, `t` remains unchanged, `i` is `t-1`, `s` is 0 or a non-positive value for each test case, and `total` is the sum of all `spend` values for each test case. Edge cases include when `s` is a single-digit number or when `s` is exactly a power of 10.

