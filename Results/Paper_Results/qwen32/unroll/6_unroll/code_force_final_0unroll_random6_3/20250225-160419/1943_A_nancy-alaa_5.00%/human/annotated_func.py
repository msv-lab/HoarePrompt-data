#State of the program right berfore the function call: The input consists of multiple test cases. The first line contains a single integer t (1 ≤ t ≤ 2 · 10^4), the number of test cases. For each test case, the first line contains a single integer n (1 ≤ n ≤ 2 · 10^5), the size of the array a. The second line contains n integers a_1, a_2, ..., a_n (0 ≤ a_i < n), the elements of the array a. The sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: A series of integers printed to the console, one per test case, representing the smallest non-negative integer that either does not appear in the array or appears exactly once for that test case.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it identifies and prints the smallest non-negative integer that either does not appear in the given array or appears exactly once.

