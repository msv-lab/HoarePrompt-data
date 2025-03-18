#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are integers such that 1 ≤ n, m ≤ 2 · 10^6. The sum of n and the sum of m over all test cases do not exceed 2 · 10^6.
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
        
    #State: t is an integer such that 1 ≤ t ≤ 10^4.
#Overall this is what the function does:The function processes `t` test cases, where each test case consists of two integers `n` and `m`. For each test case, it calculates a specific value based on these integers and prints the result as an integer.

