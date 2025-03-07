#State of the program right berfore the function call: The function `func` is expected to handle multiple test cases. For each test case, `n` is a positive integer (1 ≤ n ≤ 2·10^5), and `a` is a list of integers of length `n` where each element `a_i` satisfies 1 ≤ a_i ≤ n. The total number of test cases `t` is a positive integer (1 ≤ t ≤ 10^4), and the sum of `n` over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a, b = float('inf'), float('inf')
        
        c = 0
        
        for x in range(n):
            if a > b:
                a, b = b, a
            if l[x] <= a:
                a = l[x]
            elif l[x] <= b:
                b = l[x]
            else:
                a = l[x]
                c += 1
        
        print(c)
        
    #State: For each test case, the variable `c` will hold the number of elements in the list `l` that are greater than both the smallest and the second smallest elements found in `l`. The variables `a` and `b` will hold the smallest and the second smallest elements in `l`, respectively, but their final values are not part of the output. The loop will print the value of `c` for each test case.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers `l`. It then counts the number of elements in `l` that are greater than both the smallest and the second smallest elements in `l`. The function prints this count for each test case. The variables `a` and `b` are used to track the smallest and second smallest elements, but their final values are not part of the output.

