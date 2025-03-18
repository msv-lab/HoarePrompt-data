#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, representing the number of test cases. For each test case, n is an integer such that 1 <= n <= 100, representing the number of sticks, and a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 100, representing the lengths of the sticks.
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
        
    #State: The loop executes `w` times, and for each iteration, it reads an integer `ln` and a list of integers `palka`. It then calculates the number of shapes that can be formed using the sticks, where a shape is defined as a set of three sticks of the same length. The result for each test case is printed. The variables `t`, `n`, `a_1, a_2, ..., a_n`, and `w` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `w` from the input, which represents the number of test cases. For each test case, it reads an integer `ln` representing the number of sticks, followed by a list of integers `palka` representing the lengths of the sticks. The function then calculates the number of shapes that can be formed, where a shape is defined as a set of three sticks of the same length, and prints this number for each test case. The function does not return any value, and the input variables `w`, `ln`, and `palka` are consumed during the process but remain unchanged in the context of the function's execution.

