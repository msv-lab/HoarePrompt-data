#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, w is an integer representing the number of iterations of the loop, each iteration processes a line (ln) and a list of integers (palka), then calculates and prints the number of unique integers in palka that appear at least 3 times across all iterations.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `ln` and a list of integers representing stick lengths. It then counts and prints the number of unique stick lengths that appear at least three times across all test cases.

