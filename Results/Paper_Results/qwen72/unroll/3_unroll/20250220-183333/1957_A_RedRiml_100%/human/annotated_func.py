#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 1 <= n <= 100, and a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 100.
def func():
    w = int(input())
    for _ in range(w):
        ln = int(input())
        
        palka = list(map(int, input().split()))
        
        pl = []
        
        d = {}
        
        for i in palka:
            if d.get(i) == None:
                d[i] = 1
            else:
                d[i] += 1
            if i not in pl:
                pl.append(i)
        
        shapes = 0
        
        for j in pl:
            if d[j] >= 3:
                shapes += d[j] // 3
        
        print(shapes)
        
    #State: t, n, a_1, a_2, ..., a_n remain unchanged. w is reduced by the number of iterations the loop has executed.
#Overall this is what the function does:The function `func` reads an integer `w` from the user input, and for each of the `w` test cases, it reads an integer `ln` and a list of integers `palka` from the user input. It then calculates the number of shapes that can be formed, where a shape is defined as a group of three identical integers from the list `palka`. The function prints the number of such shapes for each test case. The function does not modify the original parameters `t`, `n`, and `a_1, a_2, ..., a_n` mentioned in the state before the function call. After the function concludes, `w` is reduced by the number of test cases processed.

