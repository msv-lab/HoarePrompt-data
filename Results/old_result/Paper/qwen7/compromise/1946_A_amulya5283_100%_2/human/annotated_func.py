#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is between 1 and 10^9 inclusive.
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
        
    #State: `t` is 0, `n` is an integer, `a` is a sorted list of integers entered by the user split from a single input string, and `res` is the total count of elements from index `mdx` to `n-1` that are equal to `a[mdx]` after all iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the array `a`), and an array `a` of `n` integers. It sorts the array `a` and then counts how many elements from the middle index to the end of the array are equal to the element at the middle index. The function prints the count for each test case and returns nothing.

