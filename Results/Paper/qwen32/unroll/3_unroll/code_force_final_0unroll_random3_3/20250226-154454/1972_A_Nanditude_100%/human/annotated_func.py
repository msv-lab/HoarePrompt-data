#State of the program right berfore the function call: Each test case consists of an integer n (1 ≤ n ≤ 100) representing the number of problems, followed by two lists a and b, each of length n. The elements of a and b are integers such that 1 ≤ a_i ≤ a_{i+1} ≤ 10^9 and 1 ≤ b_i ≤ b_{i+1} ≤ 10^9. The function will be called multiple times with different test cases, the number of which is given by the first input t (1 ≤ t ≤ 100).
def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        a = list(map(int, input().split()))
        
        b = list(map(int, input().split()))
        
        cnt = 0
        
        i = 0
        
        for j in range(n):
            if b[j] < a[i]:
                cnt += 1
            else:
                i += 1
        
        print(cnt)
        
    #State: t is 0, n, a, b, cnt, and i are in the state they were in after the last test case was processed.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of two sorted lists of integers `a` and `b`. For each test case, it counts and prints the number of elements in `b` that are less than the smallest unmatched element in `a`.

