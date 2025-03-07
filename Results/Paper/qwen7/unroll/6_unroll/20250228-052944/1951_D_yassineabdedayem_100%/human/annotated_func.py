#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
def func():
    t = int(input())
    for _ in range(t):
        n, k = map(int, stdin.readline().split())
        
        if n == k:
            print('YES')
            print(1)
            print(1)
        elif n + 2 > k * 2:
            print('YES')
            print(2)
            print(n - k + 1, end=' ')
            print(1)
        else:
            print('NO')
        
    #State: Output State: The output state depends on the input values provided during each iteration of the loop. For each input pair (n, k), the program checks conditions and prints 'YES' or 'NO'. If 'YES', it also prints additional details. Since the input values are not specified, the exact output cannot be determined without knowing the specific inputs. However, the output will consist of lines printed during each iteration, with each line either stating 'YES' followed by integers, or 'NO'.
#Overall this is what the function does:The function processes a series of test cases, each consisting of two integers \( n \) and \( k \). It checks specific conditions involving these integers and prints 'YES' or 'NO' along with additional details if applicable. Specifically, it prints 'YES' when \( n \geq k \) or when \( n + 2 > 2k \), and prints 'NO' otherwise. For each 'YES' case, it also outputs two more integers. The final state of the program is that it has processed all test cases and printed the corresponding results.

