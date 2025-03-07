#State of the program right berfore the function call: t is a positive integer such that 1 <= t <= 10^4. Each of the following t lines contains two positive integers n and m such that 1 <= n, m <= 2 * 10^6. The sum of all n and the sum of all m across all test cases do not exceed 2 * 10^6.
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
        
    #State: The sequence of integers printed for each test case, where each integer is the final value of `ans` after processing the corresponding pair of `n` and `m`.
#Overall this is what the function does:The function processes `t` test cases, each consisting of two positive integers `n` and `m`. For each test case, it calculates and prints an integer value based on a specific algorithm involving `n` and `m`.

