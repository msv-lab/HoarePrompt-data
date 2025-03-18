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
        
    #State: Output State: The output state will consist of multiple lines, each containing an integer result from the loop's execution. For each test case, if `n` (the length of the list `a`) is 1, the output will be `1`. Otherwise, the output will be the count of elements in the sorted list `a` that are equal to the middle element (or one of the two middle elements if `n` is even).
    #
    #This means that for each test case, the program will read an integer `n` and a list of `n` integers, sort the list, and then check how many times the middle element(s) appear in the list, printing this count.
#Overall this is what the function does:The function processes a series of test cases, each consisting of an integer `n` and a list `a` of `n` integers. For each test case, it sorts the list `a`, determines the middle element(s) of the sorted list, and counts how many times this element(s) appears in the list. If the list has only one element, it prints `1`. Otherwise, it prints the count of occurrences of the middle element(s). The function reads these inputs from standard input and outputs the results for each test case to standard output.

