#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the following list contains n integers a_1, a_2, \ldots, a_n such that 1 ≤ a_i ≤ 100.
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
        
    #State: After the loop executes all iterations, `shapes` will be the sum of `d[j] // 3` for all unique elements `j` in `pl` where `d[j]` is greater than or equal to 3.
#Overall this is what the function does:The function processes multiple test cases, each containing an integer n and a list of n integers. For each test case, it counts the number of unique integers that appear at least three times in the list and prints the total count. The function does not return any value but prints the result for each test case.

