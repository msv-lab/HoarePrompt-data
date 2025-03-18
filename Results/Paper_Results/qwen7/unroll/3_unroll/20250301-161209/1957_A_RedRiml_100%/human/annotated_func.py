#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks, a_1, a_2, ..., a_n, are integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `w` is an integer representing the number of iterations of the loop, and after executing all iterations, `shapes` is an integer representing the total number of shapes calculated from the input data.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `t`, an integer `n`, and a list of `n` integers representing stick lengths. It then calculates the total number of shapes that can be formed using these sticks, where each shape requires three sticks of the same length. The function outputs the total number of such shapes for each test case.

