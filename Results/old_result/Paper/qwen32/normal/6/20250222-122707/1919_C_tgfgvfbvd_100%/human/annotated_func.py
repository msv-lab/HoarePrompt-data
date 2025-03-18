#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2⋅10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2⋅10^5.
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
        
    #State: A series of integers, each representing the count of elements greater than both the smallest and second smallest elements in the corresponding list `l` for each test case.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list `l` of `n` integers. For each test case, it calculates and prints the count of elements in the list that are greater than both the smallest and second smallest unique elements in the list.

