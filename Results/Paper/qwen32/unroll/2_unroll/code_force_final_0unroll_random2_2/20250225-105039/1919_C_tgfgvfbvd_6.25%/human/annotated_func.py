#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2⋅10^5) representing the size of the array a. The following line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array a. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: a series of integers, each representing the count `c` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates and prints a count `c` that represents the number of elements in the array that satisfy specific conditions related to being greater than or less than two reference values `a` and `b`.

