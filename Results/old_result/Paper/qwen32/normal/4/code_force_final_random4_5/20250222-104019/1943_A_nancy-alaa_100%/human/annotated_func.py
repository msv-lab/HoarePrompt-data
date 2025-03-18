#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each element a_i satisfies 0 <= a_i < n. The sum of n across all test cases does not exceed 2 * 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        arr = list(map(int, input().split()))
        
        mpp = Counter(arr)
        
        first = False
        
        for i in range(n + 1):
            if i not in mpp.keys():
                print(i)
                break
            if mpp[i] == 1 and first:
                print(i)
                break
            if mpp[i] == 1:
                first = True
        
    #State: The smallest non-negative integer that is either not present in `arr` or appears exactly once in `arr` is printed for each test case.
#Overall this is what the function does:For each test case, the function prints the smallest non-negative integer that is either not present in the list `a` or appears exactly once in `a`.

