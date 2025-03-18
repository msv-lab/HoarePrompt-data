#State of the program right berfore the function call: The function `func` is expected to be called within a loop that processes multiple test cases. Each test case consists of an integer n (1 ≤ n ≤ 2 · 10^5) representing the size of the array, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n) representing the array elements. The function should be designed to handle these inputs and compute the minimum number of burles required to make all elements of the array equal. The total number of test cases t satisfies 1 ≤ t ≤ 10^4, and the sum of n over all test cases does not exceed 2 · 10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        le = len(a)
        
        l, r = 0, n - 1
        
        st, end = 1, 1
        
        while l < r and a[l] == a[l + 1]:
            l += 1
            st += 1
        
        while r > l and a[r] == a[r - 1]:
            r -= 1
            end += 1
        
        ans = le - max(st, end)
        
        if a[0] == a[-1]:
            ans = max(0, le - (st + end))
        
        print(ans)
        
    #State: The loop has processed all test cases, and for each test case, the minimum number of burles required to make all elements of the array equal has been printed. The variables `l`, `r`, `st`, `end`, and `ans` are reset and recalculated for each test case, and their final values after the last test case are not relevant to the output state. The loop variable `_` has completed its range, and the input has been fully consumed.
#Overall this is what the function does:The function `func` processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the minimum number of operations (burles) required to make all elements of the array equal. The function does not return any value; instead, it prints the result for each test case directly. After processing all test cases, the function has consumed all input and printed the results, leaving no relevant state in the variables used for computation.

