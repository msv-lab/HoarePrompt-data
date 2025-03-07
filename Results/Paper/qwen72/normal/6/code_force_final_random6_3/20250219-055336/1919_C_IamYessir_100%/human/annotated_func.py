#State of the program right berfore the function call: t is an integer such that 1 <= t <= 10^4, n is an integer such that 1 <= n <= 2 * 10^5, and a is a list of n integers where 1 <= a_i <= n. The sum of n over all test cases does not exceed 2 * 10^5.
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
        
    #State: `a` and `b` are lists that have been populated with elements from `lit` according to the conditions specified in the loop. `s` is the total count of elements in `a` and `b` that are greater than their preceding elements. The values of `n`, `lit`, `cp`, and `_` remain unchanged.
#Overall this is what the function does:The function `func` processes a series of test cases. For each test case, it reads an integer `n` and a list `lit` of `n` integers. It then populates two lists, `a` and `b`, with elements from `lit` based on specific conditions. After processing, it calculates the total count of elements in `a` and `b` that are greater than their preceding elements and prints this count. The function does not return any value. The state after the function concludes is that `a` and `b` are lists populated according to the conditions, and `s` is the count of increasing elements in these lists. The values of `n`, `lit`, and the loop counter `_` remain unchanged.

