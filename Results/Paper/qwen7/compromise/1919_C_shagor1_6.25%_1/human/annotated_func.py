#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        *inp, = map(int, input().split())
        
        x = y = n + 1
        
        ans = 0
        
        for a in inp:
            if a <= x:
                x = a
            elif a <= y:
                y = a
            else:
                x == y
                y = a
                ans += 1
        
        print(ans)
        
    #State: Output State: After all iterations of the loop, `a` is the last element of the tuple `inp`, `x` is the minimum value among all elements of `inp` that are less than or equal to `x` seen throughout all iterations, `y` is the minimum value among all elements of `inp` that are greater than `x` but less than or equal to `y` seen throughout all iterations, and `ans` is the total count of elements in `inp` that are greater than `y` across all iterations.
    #
    #This means that after the loop completes, `x` will hold the smallest element in the entire input list `inp`, `y` will hold the second smallest unique element if it exists, and `ans` will count how many elements in `inp` are larger than the second smallest unique element.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer \( n \) and a list of \( n \) integers. It then finds the smallest and second smallest unique elements in the list and counts how many elements are larger than the second smallest unique element. The function outputs this count for each test case.

