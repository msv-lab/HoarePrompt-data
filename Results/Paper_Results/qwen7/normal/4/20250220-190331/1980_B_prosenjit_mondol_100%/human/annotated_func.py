#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000. Each test case consists of three integers n, f, and k such that 1 <= f, k <= n <= 100, and a list of n integers a_i such that 1 <= a_i <= 100.
def func():
    for _ in range(int(input())):
        n, f, k = map(int, input().split())
        
        f -= 1
        
        k -= 1
        
        a = list(map(int, input().split()))
        
        x = a[f]
        
        a.sort(reverse=True)
        
        if a[k] > x:
            print('NO')
        elif a[k] < x:
            print('YES')
        else:
            print('YES' if k == n - 1 or a[k + 1] < x else 'MAYBE')
        
    #State: t is a positive integer such that 1 <= t <= 1000, n is the first input integer minus the total number of iterations, f is the first input integer minus the total number of iterations, k is the first input integer minus the total number of iterations, a is a list of integers sorted in descending order, x is the value of a[f], and a[k] remains unchanged.
#Overall this is what the function does:The function processes a series of test cases, each consisting of three integers \( n \), \( f \), and \( k \), along with a list of \( n \) integers \( a_i \). It sorts the list \( a \) in descending order and compares the elements at indices \( f \) and \( k \). Depending on the comparison results, it prints either 'YES', 'NO', or 'MAYBE'. The function does not return any value but modifies and processes the input lists and integers as described.

