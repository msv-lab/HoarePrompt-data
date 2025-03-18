#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2·10^5) representing the size of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array a. The total number of test cases t is between 1 and 10^4, and the sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: The count of elements in the list `l` that are greater than both the smallest and the second smallest unique elements in the list.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the count of elements in the list that are greater than both the smallest and the second smallest unique elements in the list.

