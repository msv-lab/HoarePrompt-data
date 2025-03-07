#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After all iterations of the loop, `y` will be equal to `n`, `b` will hold the maximum value found in the list `l` where `l[y] > l[y - 1]` was true, and `a` will hold the second maximum value among the first, third, and any value greater than both `a` and `b` encountered during the loop. The variable `c` will count how many elements in the list `l` are greater than both `a` and `b`. The variable `x` will be `n - 1` since it increments from `y + 1` until it reaches `n - 1`.
    #
    #In simpler terms, after the loop completes:
    #- `y` will be `n`.
    #- `b` will be the highest value in the list `l` that satisfies `l[y] > l[y - 1]`.
    #- `a` will be the second highest value in the list `l` that is either the initial value of `a`, or a value greater than both `a` and `b`.
    #- `c` will be the count of elements in the list `l` that are greater than both `a` and `b`.
    #- `x` will be `n - 1`.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. For each test case, it finds the highest value \( b \) in the list where the current element is greater than the previous one, and the second highest value \( a \) among the initial value of \( a \), or any value greater than both \( a \) and \( b \). It then counts how many elements in the list are greater than both \( a \) and \( b \). The function outputs this count for each test case.

