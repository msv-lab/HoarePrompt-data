#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, n is an integer where 1 ≤ n ≤ 2·10^5, and a is a list of n integers where 1 ≤ a_i ≤ n. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is 0, `n` is the last input integer, `lit` is the last list of integers provided by the user, `a` and `b` are lists that have been modified based on the conditions in the loop body, `cp` is 0, `i` is `len(b) - 1`, and `s` is the number of times an element in `a` was greater than its preceding element from index 1 to `len(a) - 1` plus the number of times an element in `b` was greater than its preceding element from index 1 to `len(b) - 1`.
#Overall this is what the function does:The function `func` reads multiple test cases from the standard input. For each test case, it reads an integer `n` and a list of `n` integers `lit`. It then processes `lit` by distributing its elements into two lists `a` and `b` based on specific conditions. After processing, it calculates the total number of strictly increasing adjacent pairs in both `a` and `b` and prints this count for each test case. The function does not return any value; it only prints the results. After the function concludes, `t` is 0, `n` is the last input integer, `lit` is the last list of integers provided by the user, `a` and `b` are lists that have been modified based on the conditions in the loop body, and `s` is the number of times an element in `a` or `b` was greater than its preceding element.

