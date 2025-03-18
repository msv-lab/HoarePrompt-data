#State of the program right berfore the function call: t is a positive integer, and for each test case, n and q are positive integers such that 1 ≤ n, q ≤ 3 × 10^5. c is a list of n positive integers where each integer is between 1 and 10^9 inclusive. l_i and r_i are integers such that 1 ≤ l_i ≤ r_i ≤ n for each query.
def func():
    for _ in range(int(input())):
        n, m = map(int, input().split())
        
        l = list(map(int, input().split()))
        
        p = [0]
        
        c = [0]
        
        i, j = 0, 0
        
        for x in l:
            if x == 1:
                j += 1
            i += x
            p.append(i)
            c.append(j)
        
        for _ in range(m):
            a, b = map(int, input().split())
            i = c[b] - c[a - 1]
            s = p[b] - p[a - 1]
            if b - a + 1 > 1 and s - (b - a + 1) >= i:
                print('YES')
            else:
                print('NO')
        
    #State: Output State: The output state consists of "YES" or "NO" printed for each query in the range specified by `m` queries. For each query `(a, b)`, it checks if the number of 1s in the subarray `l[a-1...b]` is more than half the length of the subarray. If true, it prints "YES"; otherwise, it prints "NO".
#Overall this is what the function does:The function processes a series of queries on a given list `c`. It reads the list `c` and a number of queries from standard input. For each query defined by a pair of indices `(a, b)`, it calculates the count of the integer `1` within the subarray `c[a-1...b]` and compares it to half the length of the subarray. If the count of `1`s is greater than half the length of the subarray, it prints "YES"; otherwise, it prints "NO". The function does not return any value but prints the result for each query.

