#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 1000. Each test case consists of two integers n and k such that 2 ≤ n ≤ 10^6 and 1 ≤ k ≤ n. The sum of n over all test cases does not exceed 10^7.
def func():
    t = int(input())
    for tc in range(t):
        n, k = map(int, input().split())
        
        i = 0
        
        while 1 << i + 1 <= k:
            i = i + 1
        
        ans = [k - (1 << i), k + 1, k + 1 + (1 << i)]
        
        for j in range(20):
            if j != i:
                ans.append(1 << j)
        
        print(len(ans))
        
        print(*ans)
        
    #State: A series of concatenated lists, each containing 21 numbers: [k - (1 << i), k + 1, k + 1 + (1 << i), 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072] excluding \(2^i\) for each test case.
#Overall this is what the function does:The function processes multiple test cases, each defined by two integers `n` and `k`. For each test case, it calculates and prints a list of 21 integers based on the value of `k`. The list includes specific powers of 2 and values derived from `k`, ensuring that one particular power of 2 (determined by the highest power less than or equal to `k`) is excluded.

