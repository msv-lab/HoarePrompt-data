#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 500. For each test case, n is an integer such that 2 ≤ n ≤ 10^5, and the array a consists of n positive integers where 1 ≤ a_i ≤ 10^9. The sum of all n across all test cases does not exceed 10^5.
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        max = 0
        
        for i in range(1, n):
            if min(a[i], a[i - 1]) > max:
                max = min(a[i], a[i - 1])
        
        print(max)
        
    #State: Output State: t is a positive integer such that 1 ≤ t ≤ 500. For each i from 1 to t, n is the number of elements in the list a[i], and a[i] is a list of integers. After executing the loop, max[i] is the maximum value of min(a[i][j], a[i][j-1]) for all j from 1 to n-1.
#Overall this is what the function does:The function processes a series of test cases, each containing an integer t (number of test cases, 1 ≤ t ≤ 500), an integer n (size of the array, 2 ≤ n ≤ 10^5), and an array a of n positive integers (1 ≤ a_i ≤ 10^9). For each test case, it finds and prints the maximum value of the minimum adjacent elements in the array a.

