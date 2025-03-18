#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4. For each test case, n is an integer such that 1 <= n <= 10^5, and a is a list of n integers where each integer a_i satisfies 1 <= a_i <= 10^9. The sum of all n across all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0, n is the integer input by the user in the last iteration, a is the sorted list of integers input by the user in the last iteration, and res is the count of occurrences of a[mdx] from index mdx to n-1 in the list a if n is not 1. If n is 1, res is 1.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list `a` of `n` integers. For each test case, it outputs the count of occurrences of the median element (or the single element if `n` is 1) in the sorted list `a` from the median index to the end of the list.

