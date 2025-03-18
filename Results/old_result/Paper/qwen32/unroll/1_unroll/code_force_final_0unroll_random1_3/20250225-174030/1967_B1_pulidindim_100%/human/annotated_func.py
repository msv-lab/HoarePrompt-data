#State of the program right berfore the function call: Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 10^4). For each test case, the first line contains two integers n, m (1 ≤ n, m ≤ 2 · 10^6). It is guaranteed that neither the sum of n nor the sum of m over all test cases exceeds 2 · 10^6.
def func():
    t = int(input())
    for i in range(t):
        n, m = map(int, input().split())
        
        count = 2
        
        ans = n
        
        while count <= m:
            countmins = int(count - 1)
            g = int(n / count)
            if g < countmins:
                break
            g -= countmins
            ans += int(g / count) + 1
            count += 1
        
        print(int(ans))
        
    #State: A series of printed integers, each representing the result `ans` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of two integers `n` and `m`. For each test case, it calculates and prints an integer `ans` based on a specific algorithm involving division and summation operations. The final state of the program is a series of printed integers, each corresponding to the result of the calculation for a respective test case.

