#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are positive integers such that 1 ≤ n, k ≤ 10^{18}.
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
        
    #State: Output State: The output will consist of multiple lines, each corresponding to one iteration of the loop. For each iteration:
    #
    #- If `n` equals `k`, it will print "YES\n1\n1".
    #- If `n + 2` is greater than `k * 2`, it will print "YES\n2" followed by two space-separated integers: `n - k + 1` and `1`.
    #- Otherwise, it will print "NO".
    #
    #The exact content of each line depends on the values of `n` and `k` for each iteration, and there will be `t` such lines in total.
#Overall this is what the function does:The function processes a series of test cases, each containing three integers \( t \), \( n \), and \( k \). For each test case, it checks the relationship between \( n \) and \( k \) and prints one of three possible outputs: "YES" followed by specific numbers or "NO". The function does not return any value but prints the results directly to the console.

