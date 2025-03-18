#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, ..., a_n where 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        l = list(map(int, input().split()))
        
        a = l[0]
        
        b = 0
        
        c = 0
        
        y = 0
        
        for y in range(1, n):
            if l[y] > l[y - 1]:
                b = l[y]
                break
        
        for x in range(y + 1, n):
            if l[x] > a and l[x] > b:
                if l[x] - a >= l[x] - b:
                    a = l[x]
                else:
                    b = l[x]
                c += 1
            elif l[x] < a and l[x] < b:
                if a - l[x] <= b - l[x]:
                    a = l[x]
                else:
                    b = l[x]
            elif a >= l[x]:
                a = l[x]
            else:
                b = l[x]
        
        print(c)
        
    #State: Output State: After the loop executes all its iterations, `y` will be `n - 1`, `x` will be `n + 1`, `b` will be the smallest element in `l` that is greater than both `a` and `b`, or it will remain 0 if no such element exists. The variable `c` will be the count of elements in `l` that are greater than both `a` and `b`. `a` will be the minimum value among `l[0]` to `l[n-2]`, and `l` will retain its final values from the loop iterations. The final state of `n` will be the same as the last input value provided to the loop.
    #
    #In simpler terms, after the loop completes:
    #- `y` will be `n - 1`.
    #- `x` will be `n + 1`.
    #- `b` will be the smallest element in `l` that is greater than both `a` and `b`, or it will remain 0 if no such element exists.
    #- `c` will be the count of elements in `l` that are greater than both `a` and `b`.
    #- `a` will be the minimum value among `l[0]` to `l[n-2]`.
    #- `l` will contain the final list of integers processed by the loop.
    #- `n` will be the last `n` value provided as input to the loop.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it finds the count of elements in the list that are greater than both the minimum value among the first `n-1` elements (`a`) and the smallest element in the list that is greater than both `a` and another element `b`. The function prints this count for each test case and retains the final values of `a`, `b`, `c`, `n`, and the list `l` after processing all test cases.

