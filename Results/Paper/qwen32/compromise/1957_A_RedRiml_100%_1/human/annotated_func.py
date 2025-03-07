#State of the program right berfore the function call: t is an integer such that 1 <= t <= 100. For each test case, n is an integer such that 1 <= n <= 100, and a_1, a_2, ..., a_n are integers such that 1 <= a_i <= 100.
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
        
    #State: The final value of `shapes` is the cumulative sum of `d[j] // 3` for all `j` in `pl` where `d[j] >= 3` across all `w` iterations. `w`, `ln`, `palka`, `pl`, and `d` will reflect the state of the last iteration.
#Overall this is what the function does:The function reads multiple test cases, each consisting of a list of integers. For each test case, it calculates how many sets of three identical integers can be formed from the list and prints this count for each test case.

