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
        
    #State: The output state will consist of multiple lines, each containing an integer representing the result of the operations inside the loop for each test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `t` (number of test cases), an integer `n` (length of the array `a`), and a list `a` of `n` integers. It sorts the array `a` and then checks if the middle element (or the second middle element in case of even length) appears more than once in the latter half of the array. If it does, it counts the occurrences and prints the count. If the array has only one element, it directly prints 1. The function outputs the result for each test case on a new line.

