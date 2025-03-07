#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. For each test case, n and m are positive integers such that 1 <= n, m <= 2 * 10^6. The sum of n and the sum of m over all test cases do not exceed 2 * 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = count - 1
            g = n / count
            if g < countmins:
                break
            g -= countmins
            ans += g / count + 1
            count += 1
        
        print(int(ans))
        
    #State: t remains the same, i is equal to t, n and m hold the values from the last test case, count is m + 1 if the inner loop completes without breaking, and ans holds the final accumulated value for the last test case.
#Overall this is what the function does:The function processes `t` test cases. For each test case, it takes two positive integers `n` and `m`, and computes a specific value based on these inputs. It then prints the result for each test case. The result is an integer derived from an iterative calculation involving `n` and `m`.

