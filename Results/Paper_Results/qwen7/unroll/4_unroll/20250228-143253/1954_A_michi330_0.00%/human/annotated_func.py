#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are positive integers such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: The output consists of 'YES' or 'NO' for each test case based on the given conditions. The number of 'YES' and 'NO' depends on the input values for each test case within the range specified by t.
#Overall this is what the function does:The function processes multiple test cases, each consisting of three integers \( t \), \( n \), and \( m \). It checks if \( n \) can be divided into \( k \) parts such that each part is less than or equal to \( m \). If possible, it prints 'YES'; otherwise, it prints 'NO'. The function reads \( t \) test cases from the standard input, performs the check for each case, and prints the result for each case.

