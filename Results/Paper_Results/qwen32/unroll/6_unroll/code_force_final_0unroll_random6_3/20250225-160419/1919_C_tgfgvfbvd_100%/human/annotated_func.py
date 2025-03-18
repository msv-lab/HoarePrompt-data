#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 2·10^5) representing the size of the array a, and a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the elements of the array a. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: c = 1.
#Overall this is what the function does:The function reads multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the number of times the smallest element in the list needs to be updated to maintain the second smallest element, effectively counting how many times the list cannot be extended with a new smallest element without breaking the order of the two smallest distinct elements encountered so far.

