#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 10^5) representing the length of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 10^9) representing the array a. The total number of elements across all test cases does not exceed 2 * 10^5.
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
        
    #State: t is 0. The values of n and a are from the last test case but are not significant to the final output state.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` representing the length of an array `a`, followed by `n` integers representing the elements of the array `a`. For each test case, it sorts the array and then determines the number of elements in the second half of the array (including the middle element if `n` is odd) that are equal to the middle element of the array. It prints this count for each test case.

