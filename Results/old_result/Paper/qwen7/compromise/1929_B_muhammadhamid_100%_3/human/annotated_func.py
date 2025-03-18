#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * (n + (n - 2)):
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: Output State: The output state will consist of a series of numbers printed based on the conditions within the loop. For each test case, if \( k = 1 \), it will print 1. If \( k \leq 2(n + (n - 2)) \), it will print \( \lceil \frac{k}{2} \rceil \). Otherwise, it will print \( \frac{k}{2} + 1 \).
    #
    #For example, if there are multiple test cases with different values of \( n \) and \( k \), the output will be a sequence of numbers corresponding to the above conditions for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it prints a number based on specific conditions involving \( n \) and \( k \). If \( k = 1 \), it prints 1. If \( k \leq 2(n + (n - 2)) \), it prints \( \lceil \frac{k}{2} \rceil \). Otherwise, it prints \( \frac{k}{2} + 1 \). The function does not return any value but outputs a series of numbers corresponding to these conditions for each test case.

