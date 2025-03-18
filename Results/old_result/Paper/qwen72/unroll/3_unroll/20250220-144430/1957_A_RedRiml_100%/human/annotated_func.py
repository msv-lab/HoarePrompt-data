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
                shapes += d[j] // 3
        
        print(shapes)
        
    #State: The value of `w` is decremented by the number of iterations the loop has executed. The variables `ln`, `palka`, `pl`, `d`, and `shapes` are updated for each iteration based on the input provided. The initial values of `t`, `n`, and `a_1, a_2, ..., a_n` remain unchanged.
#Overall this is what the function does:The function reads an integer `w` from the input, which represents the number of test cases. For each test case, it reads an integer `ln` representing the length of a list, followed by the list `palka` of integers. It then calculates the number of shapes that can be formed, where a shape is defined as a group of three identical integers in the list. The function prints the number of shapes for each test case. The initial values of `t`, `n`, and `a_1, a_2, ..., a_n` remain unchanged. The function does not return any value.

