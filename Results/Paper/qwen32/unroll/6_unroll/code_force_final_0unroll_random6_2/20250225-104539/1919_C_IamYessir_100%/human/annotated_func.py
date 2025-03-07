#State of the program right berfore the function call: The input consists of multiple test cases. Each test case starts with an integer n (1 ≤ n ≤ 2·10^5), representing the size of the array a. The next line contains n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ n), representing the elements of the array a. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: a series of integers, each representing the count of increasing subsequences in the lists `a` and `b` for each test case.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer `n` and a list of `n` integers. For each test case, it calculates and prints the count of increasing subsequences in two derived lists `a` and `b`, constructed based on specific rules from the input list.

