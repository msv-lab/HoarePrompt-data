#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, ..., a_n where each a_i is an integer such that 1 ≤ a_i ≤ 100.
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
        
    #State: After all iterations, `w` will be 0, indicating that the loop has completed all its specified iterations. The final `shapes` value represents the total number of unique integers in the most recent `palka` list that have a count of 3 or more. The variables `ln`, `palka`, `pl`, and `d` will reflect the state of the last iteration of the loop.
#Overall this is what the function does:The function reads multiple test cases, where each test case consists of a list of integers. For each test case, it calculates and prints the number of unique integers that appear at least three times in the list.

