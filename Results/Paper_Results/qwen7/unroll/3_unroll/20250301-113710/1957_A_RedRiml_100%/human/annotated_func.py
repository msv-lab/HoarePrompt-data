#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, \ldots, a_n where 1 ≤ a_i ≤ 100 represents the lengths of the sticks.
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
        
    #State: Output State: t is an integer such that 1 ≤ t ≤ 100, w is an integer representing the number of iterations in the loop, each iteration processes a line (ln) and a list of integers (palka), then calculates and prints the total number of shapes based on the occurrences of each integer in palka where the count is 3 or more, divided by 3.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer `n` and a list of `n` integers representing stick lengths. It counts the number of shapes that can be formed, where each shape requires three sticks of the same length. The function prints the total number of such shapes for each test case.

