#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5) representing the size of the array a. The second line of each test case contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array a. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The series of ans values printed for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and an array `a` of `n` integers. For each test case, it calculates and prints a value `ans` that represents the number of times a specific condition is met while iterating through the array.

