#State of the program right berfore the function call: The input consists of an integer t (1 ≤ t ≤ 100) representing the number of test cases. For each test case, there is an integer n (1 ≤ n ≤ 100) representing the number of sticks, followed by a list of n integers a_1, a_2, ..., a_n (1 ≤ a_i ≤ 100) representing the lengths of the sticks.
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
        
    #State: the printed value of `shapes` for each of the `w` test cases, one per line.
#Overall this is what the function does:The function processes multiple test cases, each consisting of a list of stick lengths. For each test case, it calculates and prints the maximum number of triangles that can be formed using the sticks, where each triangle requires three sticks of the same length.

