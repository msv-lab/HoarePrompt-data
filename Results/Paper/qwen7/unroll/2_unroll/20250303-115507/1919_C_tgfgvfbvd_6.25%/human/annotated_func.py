#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case contains an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: c is the count of elements in the list l that are greater than both their preceding and succeeding elements, or are the smallest or largest element between two such elements in the list.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a list of n integers. For each test case, it counts the number of elements in the list that are either greater than both their preceding and succeeding elements, or are the smallest or largest element between two such elements in the list. The function then prints the count for each test case.

