#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n such that 1 ≤ a_i ≤ n. The sum of all n values across all test cases does not exceed 2⋅10^5.
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
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 10^4. Each test case consists of an integer n such that 1 ≤ n ≤ 2⋅10^5, and a list of n integers a_1, a_2, …, a_n such that 1 ≤ a_i ≤ n. After executing the loop, the variable c contains the count of elements in the list l that satisfy the condition of being either greater than both a and b or less than both a and b, where a and b are updated according to the rules within the loop. The sum of all n values across all test cases does not exceed 2⋅10^5.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer n and a list of n integers. It counts the number of elements in the list that are either greater than both the initial values of a and b or less than both a and b, where a and b are updated based on certain conditions within the loop. The function prints the count for each test case and does not return any value.

