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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `w` is an integer representing the number of iterations of the loop, `shapes` is the sum of the number of groups of three or more occurrences of each unique integer in the input lists across all iterations of the loop.
#Overall this is what the function does:The function processes multiple lists of integers, each list containing between 1 and 100 integers (inclusive), where each integer is between 1 and 100 (inclusive). For each list, it counts the number of groups of three or more occurrences of each unique integer and sums these counts. Finally, it prints the total count of such groups across all processed lists.

