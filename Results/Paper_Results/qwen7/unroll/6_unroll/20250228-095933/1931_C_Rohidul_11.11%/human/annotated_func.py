#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        l, r = 0, n - 1
        
        st, end = 0, 0
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        if a[0] == a[-1]:
            ans = r - l - 1
        elif st == 0 and end == 0 and a[0] != a[-1]:
            ans = len(a) - 1
        else:
            ans = r - l
        
        print(max(0, ans))
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2⋅10^5, and the array a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. After executing the loop, ans is an integer representing the maximum length of the subarray starting from either the first or last element (whichever has more consecutive elements), excluding the first and last elements if they are equal, or the entire array minus one if the first and last elements are different and there are no consecutive duplicates at the start or end. The sum of all n across all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t`, an integer `n`, and a list `a` of `n` integers. It then determines the maximum length of a subarray starting from either the first or last element, excluding the first and last elements if they are equal, or the entire array minus one if the first and last elements are different and there are no consecutive duplicates at the start or end. Finally, it prints the maximum length found for each test case.

