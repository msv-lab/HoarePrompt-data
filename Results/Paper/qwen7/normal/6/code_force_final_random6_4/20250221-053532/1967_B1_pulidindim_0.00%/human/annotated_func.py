#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4, and for each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^6. It is also guaranteed that the sum of n and the sum of m over all test cases does not exceed 2⋅10^6.
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
        
    #State: `t` is an integer between 1 and \(10^4\), `i` is 3, `n` is an input integer, `m` is an integer such that the loop condition `count <= m` evaluates to false, `count` is `m + 1`, `ans` is the sum of `n` plus the series \(\sum_{k=2}^{m+1} \left(\frac{n}{k} - (k-2)\right) + 1\), `countmins` is 0, `g` is now `n / (m + 1) - 0
#Overall this is what the function does:The function processes a series of test cases, each containing two positive integers n and m. For each test case, it calculates a value based on n and m using a specific formula and prints the result. The function reads the number of test cases from the input, then for each test case, it reads n and m, performs the calculation, and outputs the result.

