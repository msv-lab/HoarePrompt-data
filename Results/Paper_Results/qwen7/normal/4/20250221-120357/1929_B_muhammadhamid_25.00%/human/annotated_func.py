#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 1000, and for each test case, n and k are integers such that 2 <= n <= 10^8 and 1 <= k <= 4n - 2.
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
        
    #State: All test cases defined by the initial state have been processed.
#Overall this is what the function does:The function processes multiple test cases, each defined by integers n and k, where n is between 2 and \(10^8\) and k is between 1 and \(4n - 2\). For each test case, it prints a calculated value based on the conditions: if k is 1, it prints 1; if k is less than or equal to 2n, it prints the ceiling of k/2; otherwise, it prints k/2 rounded down plus 1. After processing all test cases, the function concludes with no return value.

