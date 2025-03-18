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
        
    #State: After all iterations of the loop, `shapes` is the sum of `d[j] // 3` for each unique integer `j` in `palka` that appears at least 3 times for each of the `w` test cases. The loop variable `_` will have iterated `w` times, and the dictionary `d` and list `pl` will have been updated for each test case based on the input `palka`. The values of `t`, `n`, and `a_i` remain unchanged as they are not modified within the loop.
#Overall this is what the function does:The function `func` reads an integer `w` indicating the number of test cases. For each test case, it reads an integer `ln` representing the length of a list, followed by the list of integers `palka`. It then calculates the number of groups of three identical integers that can be formed from `palka` and prints this number for each test case. The function does not return any values and does not modify the initial state of `t`, `n`, or `a_i`. After the function concludes, the program state is such that `w` test cases have been processed, and the number of groups of three identical integers has been printed for each test case.

