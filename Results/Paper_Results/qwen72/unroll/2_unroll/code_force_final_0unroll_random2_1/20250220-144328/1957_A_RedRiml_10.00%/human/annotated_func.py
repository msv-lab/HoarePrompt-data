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
                shapes += 1
        
        print(shapes)
        
    #State: The values of `t`, `n`, `a_1, a_2, ..., a_n`, and `w` remain unchanged. The loop iterates `w` times, and for each iteration, it reads `ln` integers from input, processes them to count the number of unique integers that appear at least 3 times, and prints this count. After `w` iterations, the loop finishes, and the values of `ln`, `palka`, `pl`, `d`, and `shapes` are not retained between iterations.
#Overall this is what the function does:The function `func` does not accept any parameters and does not return any value. It reads an integer `w` from the input, which represents the number of test cases. For each test case, it reads an integer `ln` and a list of `ln` integers from the input. The function processes each list to count the number of unique integers that appear at least 3 times and prints this count. The values of `t`, `n`, and `a_1, a_2, ..., a_n` (mentioned in the initial state) are not used or modified by the function. After processing all `w` test cases, the function completes and the values of `ln`, `palka`, `pl`, `d`, and `shapes` are not retained.

