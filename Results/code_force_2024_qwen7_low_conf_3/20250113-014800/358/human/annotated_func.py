#State of the program right berfore the function call: t is a positive integer, each test case consists of n and m where 1 ≤ n ≤ 2 ⋅ 10^5 and 0 ≤ m ≤ 2 ⋅ 10^6, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        
        a = list(map(str, input().split()))
        
        len_arr = [0] * n
        
        zrr = [0] * n
        
        ans = 0
        
        for i in range(n):
            len_arr[i] = len(a[i])
            zrr[i] = len(a[i]) - len(a[i].rstrip('0'))
            ans += len_arr[i] - zrr[i]
        
        zrr.sort(reverse=True)
        
        for i in range(n):
            if i % 2 != 0:
                ans += zrr[i]
        
        if ans - 1 >= m:
            print('Sasha')
        else:
            print('Anna')
        
    #State of the program after the  for loop has been executed: `t` is the number of test cases, `n` is the number of integers in each test case, `m` is an integer for each test case, `a` is a list of strings containing integers, `len_arr` is a list of the lengths of the strings in `a`, `zrr` is a list of the number of trailing zeros in the strings in `a` sorted in descending order, and `ans` is the sum of `len_arr[i] - zrr[i]` for all even indices `i` in the range `0` to `n-1` plus the sum of `zrr[i]` for all odd indices `i` in the range `0` to `n-1`. After processing all test cases, if `ans - 1` is greater than or equal to the maximum `m` among all test cases, the final output is 'Sasha'. Otherwise, the final output is 'Anna'.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads the number of integers `n`, an integer `m`, and a list of `n` space-separated strings representing integers. It calculates the total number of non-zero digits in these strings (ignoring trailing zeros) and compares this value with `m`. If the calculated value minus one is greater than or equal to `m`, it prints 'Sasha'; otherwise, it prints 'Anna'. The function handles up to 200,000 test cases, with each test case containing between 1 and 200,000 integers and a list of strings representing those integers. Each string in the list can have up to 1 billion characters.

