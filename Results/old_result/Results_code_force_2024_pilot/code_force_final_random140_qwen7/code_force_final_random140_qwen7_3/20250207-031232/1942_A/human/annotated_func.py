#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^3. Each test case consists of two integers n and k such that 1 ≤ k ≤ n ≤ 10^3, and the sum of n over all test cases does not exceed 10^3.
def func():
    for _ in range(int(input())):
        n, k = list(map(int, input().split(' ')))
        
        if n == k:
            print(('1 ' * n)[:-1])
        elif k == 1:
            print(' '.join([str(x + 1) for x in range(n)]))
        else:
            print(-1)
        
    #State: Output State: The values of `n` and `k` will be the integers entered by the user for each test case, and these values will remain unchanged after all iterations of the loop. The loop processes each test case independently, so the final values of `n` and `k` for each test case will be the same as the initial values provided for that test case.
    #
    #In Natural Language: After all iterations of the loop, the values of `n` and `k` will be the same as the values entered by the user for each test case, and these values will not be altered by the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers \( n \) and \( k \). For each test case, it checks the relationship between \( n \) and \( k \) and prints one of three possible outputs: a sequence of \( n \) ones separated by spaces, a sequence of integers starting from 2 up to \( n+1 \), or -1 if no valid output can be determined. After processing all test cases, the function does not alter the values of \( n \) and \( k \) from their initial inputs.

