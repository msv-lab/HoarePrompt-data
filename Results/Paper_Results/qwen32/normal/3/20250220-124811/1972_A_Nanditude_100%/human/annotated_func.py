#State of the program right berfore the function call: The input consists of multiple test cases. For each test case, n is a positive integer (1 ≤ n ≤ 100) representing the number of problems. a is a list of length n (1 ≤ a_1 ≤ a_2 ≤ ... ≤ a_n ≤ 10^9) representing the difficulties of the proposed problems, and b is a list of length n (1 ≤ b_1 ≤ b_2 ≤ ... ≤ b_n ≤ 10^9) representing the expected difficulties of the problems. The number of test cases t satisfies 1 ≤ t ≤ 100.
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
        
    #State: The loop has finished executing `t` times, and for each of the `t` test cases, the value of `cnt` (which represents the number of elements in `b` that are less than the corresponding elements in `a`) has been printed. The variables `n`, `a`, `b`, `cnt`, and `i` will reflect the state of the last iteration of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of a number of problems `n`, a list `a` of proposed difficulties, and a list `b` of expected difficulties. For each test case, it calculates and prints the number of elements in `b` that are less than the corresponding elements in `a` as `a` is iterated through sequentially.

