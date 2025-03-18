#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the lengths of the sticks a_1, a_2, ..., a_n are integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: The final value of `shapes` is the sum of `d[j] // 3` for all unique elements `j` in `pl` where `d[j]` is greater than or equal to 3 after all iterations of the loop.
#Overall this is what the function does:The function processes multiple test cases, where each test case involves an integer `t` indicating the number of sticks, followed by `t` integers representing the lengths of the sticks. It calculates and prints the total number of shapes that can be formed, where each shape requires at least three sticks of the same length. The final state of the program is the output of the total number of such shapes for each test case.

