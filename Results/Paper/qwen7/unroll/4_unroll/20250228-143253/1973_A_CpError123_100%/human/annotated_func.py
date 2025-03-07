#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500, and for each test case, p_1, p_2, and p_3 are non-negative integers satisfying 0 ≤ p_1 ≤ p_2 ≤ p_3 ≤ 30.
def func():
    t = int(input())
    for _ in range(t):
        a, b, c = map(int, input().split())
        
        if (a + b + c) % 2 != 0:
            print(-1)
            continue
        
        x = (a + b + c) // 2
        
        y = a + b
        
        print(min(x, y))
        
    #State: t is the number of test cases, and for each test case, the output is either -1 or the minimum value between half the sum of a, b, and c (rounded down) and the sum of a and b, provided the sum is even.
#Overall this is what the function does:The function processes multiple test cases, each defined by three integers \(a\), \(b\), and \(c\). For each test case, it checks if the sum of \(a\), \(b\), and \(c\) is even. If the sum is odd, it prints \(-1\). Otherwise, it calculates two values: \(x\) as half the sum of \(a\), \(b\), and \(c\) (rounded down), and \(y\) as the sum of \(a\) and \(b\). It then prints the smaller of these two values. The function reads the number of test cases from the input and repeats this process for each test case.

