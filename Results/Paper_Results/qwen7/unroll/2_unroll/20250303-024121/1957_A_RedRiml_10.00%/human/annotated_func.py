#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the list of stick lengths a_1, a_2, ..., a_n consists of integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `w` is an integer representing the number of iterations of the loop. After executing the loop `w` times, `shapes` is an integer representing the total count of unique elements in the lists `palka` that appear at least three times across all inputs.
#Overall this is what the function does:The function processes up to 100 test cases, where each test case includes an integer `n` and a list of `n` integers representing stick lengths. For each test case, it counts the number of unique stick lengths that appear at least three times and prints this count. The function ultimately outputs the total count of such unique stick lengths across all test cases.

