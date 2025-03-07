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
        
    #State: t is an integer such that 0 ≤ t ≤ 10^4 - (number of iterations executed); n is the integer obtained from the input; l is the list of integers obtained from the input; a is the smallest element in l; b is the second smallest element in l; c is the count of elements in l that are greater than both a and b.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads an integer `n` and a list of `n` integers. It then calculates and prints the count of elements in the list that are greater than both the smallest and the second smallest elements in the list.

