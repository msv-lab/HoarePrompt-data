#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n values across all test cases does not exceed 2 * 10^5.
def func():
    t = int(input())
    while t > 0:
        t -= 1
        
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        if n == 1:
            print(1)
        else:
            res = 0
            mdx = n // 2 + n % 2 - 1
            for i in range(mdx, n):
                if a[mdx] == a[i]:
                    res += 1
            print(res)
        
    #State: t is 0; n is the length of the last list a provided by the user input; a is the sorted list of integers from the last test case provided by the user input. If n is 1, no additional changes are made. Otherwise, mdx is n // 2 + n % 2 - 1 and res is the count of elements from a[mdx] to a[n-1] that are equal to a[mdx].
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it outputs the count of elements in the sorted list `a` that are equal to the median element (or the middle element if `n` is odd, or the larger of the two middle elements if `n` is even). If `n` is 1, it simply outputs 1.

