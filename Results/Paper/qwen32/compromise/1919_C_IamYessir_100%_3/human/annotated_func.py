#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 10^4. For each test case, n is an integer such that 1 ≤ n ≤ 2·10^5, and a is a list of n integers where each integer a_i satisfies 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
def func():
    for _ in range(int(input())):
        n = int(input())
        
        lit = list(map(int, input().split()))
        
        a, b = [], []
        
        cp = 0
        
        for i in range(0, n):
            if len(a) == 0:
                x = float('inf')
            else:
                x = a[-1]
            if len(b) == 0:
                y = float('inf')
            else:
                y = b[-1]
            if x > y:
                if y >= lit[i]:
                    b.append(lit[i])
                elif lit[i] > x:
                    b.append(lit[i])
                elif x >= lit[i] and lit[i] > y:
                    a.append(lit[i])
            elif x == y:
                a.append(lit[i])
            elif x < y:
                if x >= lit[i]:
                    a.append(lit[i])
                elif lit[i] > y:
                    a.append(lit[i])
                elif y >= lit[i] and lit[i] > x:
                    b.append(lit[i])
        
        s = 0
        
        for i in range(1, len(a)):
            if a[i] > a[i - 1]:
                s += 1
        
        for i in range(1, len(b)):
            if b[i] > b[i - 1]:
                s += 1
        
        print(s)
        
    #State: `s` is the count of times an element in `a` or `b` is greater than the previous element for the last test case processed, `a` and `b` are lists populated based on the last test case's input, `lit` is the list of integers from the last test case, `n` is the integer from the last test case, and `cp` is 0.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers. For each test case, it computes and prints the count of times an element in two derived lists `a` and `b` is greater than the previous element. The derived lists are populated based on specific conditions related to the input list.

