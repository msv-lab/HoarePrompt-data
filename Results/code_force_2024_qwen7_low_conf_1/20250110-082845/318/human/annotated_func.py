#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^3, and for each test case, n is an integer such that 3 ≤ n ≤ 10^5. Additionally, the sum of all n across all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        mid = n // 2
        
        a = []
        
        for i in range(1, n // 2 + 1):
            a.append(i)
            a.append(mid + i)
        
        if n % 2 != 0:
            a.append(n)
        
        for i in range(n):
            print(a[i], end=' ')
        
        print('\n', end='')
        
    #State of the program after the  for loop has been executed: `t` is an integer such that \(1 \leq t \leq 10^3\), each `n` is an integer such that \(3 \leq n \leq 10^5\), `i` is `n + 1`, `mid` is `n // 2`, `a` is a list containing exactly \(n + 1\) elements where the first half consists of integers from 1 to \(n // 2\) and the second half consists of those integers incremented by \(n // 2\), if `n` is odd, the last element is `n`, and the list `a` contains all these values exactly once.
#Overall this is what the function does:The function processes a series of test cases, where each test case involves an integer \( n \) (such that \( 3 \leq n \leq 10^5 \)). For each \( n \), the function generates and prints a sequence of integers. Specifically, it creates a list `a` containing \( n \) elements, where the first half of the list consists of integers from 1 to \( n // 2 \), and the second half consists of those integers incremented by \( n // 2 \). If \( n \) is odd, the last element of the list is set to \( n \). After constructing the list, the function prints its elements, one per line. The function handles up to \( 10^3 \) test cases, and the sum of all \( n \) across all test cases does not exceed \( 10^5 \).

