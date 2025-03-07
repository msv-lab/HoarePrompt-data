#State of the program right berfore the function call: t is an integer where 1 <= t <= 100, n is an integer where 1 <= n <= 100 for each test case, and a_1, a_2, ..., a_n are integers where 1 <= a_i <= 100 representing the lengths of the sticks.
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
        
    #State: t is an integer where 1 <= t <= 100, n is an integer where 1 <= n <= 100 for each test case, and a_1, a_2, ..., a_n are integers where 1 <= a_i <= 100 representing the lengths of the sticks. w is an integer input by the user, and the loop has printed the number of shapes (sets of three sticks of the same length) for each of the w test cases.
#Overall this is what the function does:The function `func` reads an integer `w` from the user, representing the number of test cases. For each test case, it reads an integer `ln` indicating the number of sticks, followed by a list of integers `palka` representing the lengths of the sticks. The function then calculates and prints the number of shapes (sets of three sticks of the same length) that can be formed from the sticks in each test case. After processing all test cases, the function concludes without returning any value. The state of the program remains unchanged except for the printed output.

