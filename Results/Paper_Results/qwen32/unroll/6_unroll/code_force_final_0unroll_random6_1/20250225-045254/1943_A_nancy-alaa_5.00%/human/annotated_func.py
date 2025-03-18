#State of the program right berfore the function call: t is an integer such that 1 <= t <= 2 * 10^4. For each test case, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where each integer a_i satisfies 0 <= a_i < n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: The variables `n`, `arr`, `mpp`, `first`, and `i` will hold the values from the last test case, and `t` will remain unchanged.
#Overall this is what the function does:The function reads multiple test cases. For each test case, it reads an integer `n` and a list `a` of `n` integers where each integer is between 0 and `n-1`. It then determines and prints the smallest integer from 0 to `n-1` that either does not appear in the list or appears exactly once, with the condition that if there are multiple such integers, the smallest one is chosen.

