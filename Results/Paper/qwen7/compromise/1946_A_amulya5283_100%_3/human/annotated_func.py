#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is in the range [1, 10^9].
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
        
    #State: Output State: `t` is 0, `n` is an integer representing the number of elements in the last test case, `mdx` is `n // 2 + n % 2 - 1`, `i` is either `-1` or `n - 1` depending on the condition `n == 1`, `res` contains the total count of elements in the list `a` starting from index `mdx` (which is `n // 2 + n % 2 - 1`) that are equal to `a[mdx]` and incremented by 1 each time `a[mdx]` equals `a[i]` for every `i` in the range from `mdx` to `n-1`, and `a` is a sorted list of integers entered by the user.
    #
    #In simpler terms, after all iterations of the loop have finished, `t` will be 0 because all test cases have been processed. The value of `n` will be the number of elements in the last test case, `mdx` will be calculated based on `n`, `i` will be either `-1` or `n - 1` depending on whether `n` is 1 or not, `res` will contain the count of elements in the last test case's sorted list that are equal to the middle element (or the element just after the middle if `n` is even), and `a` will be the sorted list of integers for the last test case as provided by the user.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it sorts the list `a` and then counts the occurrences of the middle element (or the element just after the middle if `n` is even) in the sorted list. It prints the count for each test case. After processing all test cases, the function outputs nothing further and ends.

