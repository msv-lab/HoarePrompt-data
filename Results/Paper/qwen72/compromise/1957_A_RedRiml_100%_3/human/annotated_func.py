#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, n is an integer where 1 <= n <= 100 for each test case, and a_1, a_2, ..., a_n are integers where 1 <= a_i <= 100.
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
        
    #State: The loop has completed all `w` iterations, and for each iteration, `ln` is an input integer, `palka` is a list of integers input by the user that must have `ln` elements, `d` is a dictionary where each key is a unique integer from `palka` and each value is the count of that integer in `palka`, `pl` is a list containing all unique integers from `palka` in the order they first appeared, `shapes` is the sum of the integer divisions of the counts of all unique integers in `palka` that appear 3 or more times by 3. The variables `t`, `n`, `a_1, a_2, ..., a_n`, and `w` remain unchanged.
#Overall this is what the function does:The function `func` reads an integer `w` indicating the number of test cases. For each test case, it reads an integer `ln` representing the number of elements, followed by a list of `ln` integers. It then calculates and prints the number of groups of three identical integers that can be formed from the list for each test case. The function does not return any value; it only prints the results. The variables `t`, `n`, and `a_1, a_2, ..., a_n` are not modified by the function.

