#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, a, b, and c are integers such that 0 ≤ a, b, c ≤ 9.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if a < b < c:
            print('STAIR')
        elif a < b and b > c:
            print('PEAK')
        else:
            print('NONE')
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(0 \leq t \leq 997\), `a` is the last input integer \(a_{input}\), `b` is the last input integer \(b_{input}\), `c` is the last input integer \(c_{input}\). After executing the loop, the program will have processed all inputs up to the \(t\)th input, and if none of the conditions `a < b < c`, `a < b` and `b > c` were met for any input, the program will print 'NONE' for all remaining iterations without changing the values of `a`, `b`, and `c`.
#Overall this is what the function does:The function processes up to 1000 test cases, each consisting of three integers \(a\), \(b\), and \(c\) within the range [0, 9]. For each test case, it checks if the integers satisfy one of two conditions: either \(a < b < c\) (in which case it prints "STAIR") or \(a < b\) and \(b > c\) (in which case it prints "PEAK"). If neither condition is met for a given test case, it prints "NONE" for that test case. After processing all test cases, the function will have printed "STAIR", "PEAK", or "NONE" for each test case based on the conditions specified. If \(t\) is 1000, the function will handle exactly 1000 test cases; otherwise, it will process up to \(t\) test cases. The function does not return any value but prints the results directly.

