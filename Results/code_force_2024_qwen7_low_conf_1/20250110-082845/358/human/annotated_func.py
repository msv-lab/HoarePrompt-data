#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of integers n and m such that 1 ≤ n ≤ 2 ⋅ 10^5 and 0 ≤ m ≤ 2 ⋅ 10^6. Additionally, there is a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ 10^9 for each element in the list. The sum of n across all test cases does not exceed 2 ⋅ 10^5.
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
        
    #State of the program after the  for loop has been executed: `t` is 0, `a` is an empty list, `n` is 0, `m` is 0, `len_arr` is a list of 0 integers, `zrr` is a list of 0 integers, `ans` is 0, and `i` is 0.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer \(n\), an integer \(m\), and a list of \(n\) integers \(a_1, a_2, \ldots, a_n\). For each test case, it calculates a value `ans` based on the lengths of the strings in the list \(a\), specifically considering the number of trailing zeros. It then checks if `ans - 1` is greater than or equal to \(m\). If true, it prints 'Sasha', otherwise it prints 'Anna'. The function handles up to \(10^4\) test cases, with each \(n\) not exceeding \(2 \cdot 10^5\), and the sum of all \(n\) values not exceeding \(2 \cdot 10^5\). The function does not modify the input list `a` but instead works with derived lists `len_arr` and `zrr`. The function does not handle edge cases where the input might be invalid (e.g., non-integer values for \(t\), \(n\), or \(m\), or non-positive integers for \(m\)).

