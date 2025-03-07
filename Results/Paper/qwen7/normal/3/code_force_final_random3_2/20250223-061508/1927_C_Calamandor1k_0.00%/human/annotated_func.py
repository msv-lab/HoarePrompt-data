#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n and m are positive integers such that 1 ≤ n, m ≤ 2⋅10^5, and k is an even integer such that 2 ≤ k ≤ 2⋅min(n, m). Each test case consists of two arrays a and b, where a has n integers and b has m integers, and each integer in both arrays is between 1 and 10^6 inclusive.
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
        
    #State: Output State: After the loop executes all the iterations, `i` will be equal to `max(len_a, len_b)`, `count_a` will be a value between 0 and `min(len_a, max(len_a, len_b))` inclusive, and `count_b` will be a value between 0 and `min(len_b, max(len_a, len_b))` inclusive. The values of `n`, `m`, `k`, `a`, `b`, `len_a`, `len_b`, and `d` will remain unchanged.
    #
    #This means that after all iterations of the loop have completed, the variable `i` will have reached the maximum length between the two lists `a` and `b`. The variable `count_a` will hold the total number of elements in list `a` that are less than or equal to `k`, up to the length of the longer list. Similarly, `count_b` will hold the total number of elements in list `b` that are less than or equal to `k`, also up to the length of the longer list. The original values of `n`, `m`, `k`, `a`, `b`, `len_a`, `len_b`, and `d` will not change.
#Overall this is what the function does:The function processes multiple test cases, each consisting of integers t, n, m, k, and two arrays a and b. For each test case, it counts the number of elements in arrays a and b that are less than or equal to k (up to the length of the longer array). If the count of such elements in both arrays is greater than or equal to k/2, it prints 'YES'; otherwise, it prints 'NO'. The function does not modify the input arrays or any other global state.

