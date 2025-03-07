#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 100.
def func():
    t = int(input())
    for i in range(t):
        n, m = [int(i) for i in input().split()]
        
        if n == m:
            print('Yes')
        elif m > n:
            print('No')
        elif m == n - 1:
            print('Yes')
        elif m % 2 == 0 and n % 2 == 0:
            print('Yes')
        elif m % 2 != 0 and n % 2 != 0:
            print('Yes')
        else:
            print('No')
        
    #State: Output State: The output state will consist of a series of "Yes" and "No" responses based on the conditions evaluated within the loop for each iteration. Specifically, for each pair of integers (n, m) entered, if n equals m, or if m is one less than n, or if both n and m are even, or if both n and m are odd, the output will be "Yes". Otherwise, the output will be "No". The exact sequence of "Yes" and "No" will depend on the input pairs provided during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases. For each test case, it reads two integers \( n \) and \( m \). Based on the values of \( n \) and \( m \), it determines whether to output "Yes" or "No". Specifically, it outputs "Yes" if \( n \) equals \( m \), if \( m \) is one less than \( n \), if both \( n \) and \( m \) are even, or if both \( n \) and \( m \) are odd. Otherwise, it outputs "No". The function does not return any value but prints the results for each test case.

