#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: The variables `t`, `n`, `a_1, a_2, ..., a_n`, and `w` remain unchanged. The loop prints the number of integers that appeared at least 3 times for each of the `w` input lists.
#Overall this is what the function does:The function reads an integer `w` representing the number of test cases. For each test case, it reads an integer `ln` and a list of `ln` integers. It then calculates and prints the number of distinct integers in the list that appear at least 3 times.

