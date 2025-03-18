#State of the program right berfore the function call: t is a positive integer such that 1 ≤ t ≤ 2 ⋅ 10^4. For each test case, n is a positive integer such that 1 ≤ n ≤ 2 ⋅ 10^5, and a is a list of n non-negative integers where each integer a_i satisfies 0 ≤ a_i < n. The sum of all n values across all test cases does not exceed 2 ⋅ 10^5.
def func():
    T = int(input())
    for _ in range(T):
        S = int(input())
        
        N = list(map(int, input().split()))
        
        N.sort()
        
        cur = -1
        
        M = {}
        
        for num in N:
            if num > cur:
                if num > cur + 1:
                    cur += 1
                    break
                cur = num
                M[cur] = 1
            else:
                M[cur] += 1
        
        if sum([M[k] for k in M.keys()]) == S:
            cur += 1
        
        for i in range(cur):
            if M[i] <= i:
                cur = i
                break
        
        print(cur)
        
    #State: cur is greater than 3, i is 0.
#Overall this is what the function does:The function processes multiple test cases. For each test case, it reads a positive integer \( T \) (the number of test cases), followed by a positive integer \( S \) and a list \( N \) of \( n \) non-negative integers. It then sorts the list \( N \) and iterates through it to determine the largest integer \( cur \) such that the count of numbers less than or equal to \( cur \) in \( N \) meets or exceeds \( S \). Finally, it prints the value of \( cur \).

