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
        
    #State: The value of `shapes` is the sum of `d[j] // 3` for each `j` in `pl` where `d[j]` is greater than or equal to 3 after all iterations of the loop have finished.
#Overall this is what the function does:The function processes multiple test cases, each consisting of an integer indicating the number of stick lengths followed by those lengths. It counts the number of equilateral triangles (triangles with all sides of equal length) that can be formed from the given stick lengths and prints the total count for each test case.

