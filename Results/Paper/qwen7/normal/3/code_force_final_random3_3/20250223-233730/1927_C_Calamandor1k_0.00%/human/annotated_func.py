#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). Each test case consists of two arrays a and b, where a has n integers and b has m integers, and each integer in both arrays is in the range 1 to 10^6. The sum of values n and m over all test cases in a test does not exceed 4⋅10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        len_a, len_b = len(a), len(b)
        
        count_a, count_b = 0, 0
        
        d = k // 2
        
        for i in range(max(len_a, len_b)):
            if len_a > i + 1:
                if a[i] <= k:
                    count_a += 1
            if len_b > i + 1:
                if b[i] <= k:
                    count_b += 1
        
        print('YES' if count_a >= d and count_b >= d else 'NO')
        
    #State: Output State: The final output state after the loop executes all its iterations is determined by the values of `count_a` and `count_b` after processing all elements in lists `a` and `b` that are less than or equal to `k`. Specifically, `count_a` will be the total number of elements in list `a` that are less than or equal to `k`, and `count_b` will be the total number of elements in list `b` that are less than or equal to `k`. If both `count_a` and `count_b` are greater than or equal to `k // 2`, the output will be 'YES'; otherwise, it will be 'NO'.
    #
    #This final output state is derived from the cumulative counts of elements in `a` and `b` that meet the condition `x <= k`, ensuring that these counts reflect the entire dataset processed over all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case includes positive integers \(n\) and \(m\), an even integer \(k\), and two arrays \(a\) and \(b\). It counts the number of elements in arrays \(a\) and \(b\) that are less than or equal to \(k\). If the count of such elements in both arrays is at least \(\frac{k}{2}\), the function outputs 'YES'; otherwise, it outputs 'NO'.

