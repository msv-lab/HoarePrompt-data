#State of the program right berfore the function call: t is a positive integer representing the number of test cases. For each test case, n is a positive integer representing the length of the array a, and a is a list of n integers where each integer is in the range [1, 10^9].
def func():
    """Median of Array"""
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        a.sort()
        
        p = (n + 1) // 2 - 1
        
        res = a.count(a[p])
        
        print(res)
        
    #State: t test cases have been processed, each case prints the count of the middle element in the sorted list of integers.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `n` representing the length of an array `a`, followed by the array `a` itself. It sorts the array and calculates the count of the middle element (median) in the sorted array. For each test case, it prints the count of the middle element. After processing all test cases, the function does not return any value but prints the count of the middle element for each test case.

