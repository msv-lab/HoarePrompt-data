#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 100, and each test case consists of two positive integers n and m such that 1 ≤ n, m ≤ 100.
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
        
    #State: Output State: The output state will consist of a series of 'Yes' and 'No' responses based on the conditions evaluated in the loop for each pair of integers (n, m) entered. Specifically, 'Yes' is printed if n equals m, if m is greater than n, if m is one less than n, or if both n and m are even or both are odd. Otherwise, 'No' is printed. The exact sequence of 'Yes' and 'No' depends on the input pairs provided during the loop's execution.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two positive integers \( n \) and \( m \). For each pair, it checks specific conditions and prints 'Yes' or 'No' based on those conditions. If \( n \) equals \( m \), if \( m \) is greater than \( n \), if \( m \) is one less than \( n \), or if both \( n \) and \( m \) are either even or odd, it prints 'Yes'. Otherwise, it prints 'No'. After processing all test cases, no value is returned.

