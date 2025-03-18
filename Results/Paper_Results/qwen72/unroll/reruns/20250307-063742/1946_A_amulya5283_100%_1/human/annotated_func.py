#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. Each test case includes an integer `n` (1 ≤ n ≤ 10^5) representing the length of the array, and an array `a` of `n` integers (1 ≤ a_i ≤ 10^9). The total number of test cases `t` is given, where 1 ≤ t ≤ 10^4, and the sum of the values of `n` over all test cases does not exceed 2 · 10^5.
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
        
    #State: The value of `t` is 0, and the loop has processed all the test cases. The variable `n` and array `a` are set to the values of the last test case, and `a` is sorted. The variable `res` is set to the number of elements in the last test case's array `a` that are equal to the median element.
#Overall this is what the function does:The function `func` reads an integer `t` representing the total number of test cases. For each test case, it reads an integer `n` and an array `a` of `n` integers. It sorts the array `a` and then calculates the number of elements in `a` that are equal to the median element. The function prints this count for each test case. After processing all test cases, the function terminates with `t` set to 0, and the last test case's `n` and `a` values are retained, with `a` being sorted.

