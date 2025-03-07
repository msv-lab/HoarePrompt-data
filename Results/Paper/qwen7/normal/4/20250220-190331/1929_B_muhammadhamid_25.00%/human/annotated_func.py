#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, n and k are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2.
def func():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        
        if k == 1:
            print(1)
            continue
        
        if k <= 2 * n:
            print(math.ceil(k / 2))
        else:
            print(k // 2 + 1)
        
    #State: After all iterations of the loop have finished, `t` is a positive integer such that 1 ≤ t ≤ 1000, and for each test case, `n` and `k` are integers such that 2 ≤ n ≤ 10^8 and 1 ≤ k ≤ 4n - 2. The loop processes each test case individually, updating `t` to reflect the number of remaining test cases after each iteration. Once all test cases have been processed, `t` will be reduced to 0, indicating that there are no more test cases left to process.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers \( n \) and \( k \). For each test case, it calculates and prints a value based on the given \( n \) and \( k \). If \( k \) is 1, it prints 1. If \( k \) is less than or equal to \( 2n \), it prints the ceiling of \( k/2 \). Otherwise, it prints \( k/2 + 1 \). After processing all test cases, it ensures that the number of remaining test cases \( t \) is reduced to 0.

