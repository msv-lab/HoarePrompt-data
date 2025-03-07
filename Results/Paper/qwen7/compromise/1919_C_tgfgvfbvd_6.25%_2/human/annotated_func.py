#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n where 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: After the loop executes all the iterations, variable `c` will hold the total number of elements in the list `l` that are either greater than both `a` and `b`, or are closer to `a` than to `b` when they are neither greater than `a` nor `b`. The variables `a` and `b` will represent the smallest and second smallest unique elements found in the list `l` during the iterations, respectively. If no such unique elements exist, `a` and `b` will retain their initial values. The variable `x` will be equal to `y + c`, where `y` is the last value of `n` minus the last value of `x`. The variable `n` will remain unchanged from its initial value.
    #
    #This means that after the loop completes, `c` will contain the count of significant elements based on the conditions given, `a` and `b` will be set to the smallest and second smallest unique elements found in the list, and `x` will reflect the final state as described.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer \( n \) and a list of \( n \) integers. It identifies the smallest and second smallest unique elements in the list and counts the number of elements that are either greater than both these elements or closer to the smaller element than to the larger one when they are not greater than both. The function prints the count of such elements for each test case and does not return any value.

