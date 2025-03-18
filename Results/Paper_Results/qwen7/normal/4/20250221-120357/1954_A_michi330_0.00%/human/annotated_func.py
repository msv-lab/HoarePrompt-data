#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n, m, and k are positive integers such that 1 ≤ m, k ≤ n ≤ 50.
def func():
    t = int(input())
    for itest in range(0, t, 1):
        n, m, k = map(int, input().split())
        
        if n <= k or n - math.ceil(n / m) < k:
            print('NO')
        else:
            print('Yes')
        
    #State: t is an integer between 1 and 1000 inclusive, itest equals the total number of iterations (which is the value of t), n, m, and k are integers obtained from the last input split by spaces. The condition checked in the loop is n <= k or n - math.ceil(n / m) >= k. If the condition was met for any iteration, 'Yes' was printed; otherwise, 'NO' was printed.
#Overall this is what the function does:The function processes up to 1000 test cases, where for each test case, it takes three integers \(n\), \(m\), and \(k\) as inputs. It checks if \(1 \leq m, k \leq n \leq 50\) and \(1 \leq t \leq 1000\). Based on the values of \(n\), \(m\), and \(k\), it prints either 'Yes' or 'No' for each test case. After processing all test cases, the function does not return anything but prints the results directly.

