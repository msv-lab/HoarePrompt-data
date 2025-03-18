#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and a list of n integers a_1, a_2, \ldots, a_n where 1 ≤ a_i ≤ 100 represents the lengths of the sticks.
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
        
    #State: Output State: `t` is an integer such that 1 ≤ t ≤ 100, `w` is an integer representing the number of iterations of the loop, `shapes` is an integer representing the total number of unique integers in the input lists that appear at least three times across all iterations.
    #
    #The loop processes `w` inputs. For each input, it reads an integer `ln` and a list of integers `palka`. It then counts the occurrences of each integer in `palka`, keeping track of unique integers that appear at least three times. The final count of such integers is printed for each input, and `shapes` accumulates these counts across all iterations.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer indicating the number of sticks and a list of stick lengths. It counts the number of unique stick lengths that appear at least three times across all test cases and prints this count for each test case. The function does not return any value but prints the count of such unique stick lengths for each test case.

