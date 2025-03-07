#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, a and b are positive integers such that 1 ≤ a, b ≤ 10^9.
def func():
    n = int(input())
    for i in range(n):
        a, b = [int(i) for i in input().split()]
        
        if a % 2 != 0 and b % 2 != 0:
            print('NO')
        elif a / 2 == b or b / 2 == a:
            print('NO')
        else:
            print('YES')
        
    #State: Output State: The output state will consist of 'YES' or 'NO' printed for each iteration of the loop based on the conditions provided. Specifically, for each pair (a, b) entered, if either a or b is odd and both are odd, or if a/2 equals b or b/2 equals a, then 'NO' is printed; otherwise, 'YES' is printed. The final state will be a sequence of 'YES' and 'NO' outputs corresponding to the given pairs (a, b).
#Overall this is what the function does:The function processes multiple test cases, each consisting of two positive integers \(a\) and \(b\). For each pair, it checks if both \(a\) and \(b\) are odd and not equal, and if \(a/2\) does not equal \(b\) and \(b/2\) does not equal \(a\). If these conditions are met, it prints 'YES'; otherwise, it prints 'NO'. After processing all test cases, the function outputs a sequence of 'YES' and 'NO' based on the given pairs.

