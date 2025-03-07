#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100, n is an integer such that 1 <= n <= 100 for each test case, and a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 100.
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
                shapes += 1
        
        print(shapes)
        
    #State: The values of `t`, `n`, and `a_1, a_2, ..., a_n` remain unchanged. The value of `w` is decremented by the number of iterations the loop has executed. The loop prints the number of unique integers in each list `palka` that appear at least 3 times, for each of the `w` iterations.
#Overall this is what the function does:The function `func` reads an integer `w` from the input, which represents the number of test cases. For each test case, it reads an integer `ln` and a list of integers `palka`. It then calculates and prints the number of unique integers in `palka` that appear at least 3 times. The function does not return any value. After the function concludes, the values of `t`, `n`, and `a_1, a_2, ..., a_n` (if they exist) remain unchanged, but the value of `w` is decremented by the number of iterations the loop has executed.

