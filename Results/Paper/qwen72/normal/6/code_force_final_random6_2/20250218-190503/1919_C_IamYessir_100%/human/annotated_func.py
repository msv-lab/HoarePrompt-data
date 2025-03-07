#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 10^4, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 2·10^5, representing the size of the array a. a is a list of n integers where 1 ≤ a_i ≤ n, representing the elements of the array a. The sum of n over all test cases does not exceed 2·10^5.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 10^4, `_` is `t - 1`, `n` is the last input integer where 1 ≤ n ≤ 2·10^5, `lit` is the last list of integers provided by the user, `a` and `b` are lists where each element in `a` is greater than or equal to the element before it, and each element in `b` is greater than or equal to the element before it, `x` is the last element of `a` if `a` is not empty, otherwise `x` is positive infinity, `y` is the last element of `b` if `b` is not empty, otherwise `y` is positive infinity, and `s` is the total count of elements in `a` that are strictly greater than the element immediately before them plus the total count of elements in `b` that are strictly greater than the element immediately before them.
#Overall this is what the function does:The function `func` processes multiple test cases. For each test case, it reads an integer `n` and a list `lit` of `n` integers. It then distributes the elements of `lit` into two lists `a` and `b` based on certain conditions. After processing, it calculates the total number of strictly increasing adjacent pairs in both `a` and `b` and prints this count. The function does not return any value. After the function concludes, the state of the program includes the integer `t` (number of test cases), the loop counter `_` (which is `t - 1`), the last input integer `n`, the last list `lit` of integers, and the lists `a` and `b` which are sorted in non-decreasing order. The variable `s` holds the total count of strictly increasing adjacent pairs in `a` and `b`.

