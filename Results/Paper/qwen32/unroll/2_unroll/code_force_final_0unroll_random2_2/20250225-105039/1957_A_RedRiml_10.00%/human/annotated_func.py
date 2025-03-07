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
                shapes += 1
        
        print(shapes)
        
    #State: a series of w integers, each representing the number of unique elements in the respective input lists that appear 3 or more times.
#Overall this is what the function does:The function reads an integer `w` representing the number of test cases. For each test case, it reads an integer `n` followed by a list of `n` integers. It then calculates and prints the number of unique integers in the list that appear at least 3 times. This process is repeated for each test case, resulting in `w` printed outputs.

