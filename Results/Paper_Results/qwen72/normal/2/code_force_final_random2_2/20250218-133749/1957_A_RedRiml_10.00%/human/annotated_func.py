#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 100, representing the number of sticks. The list of stick lengths a_1, a_2, ..., a_n consists of integers where 1 ≤ a_i ≤ 100.
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
        
    #State: After all iterations of the loop have executed, `t` remains unchanged, `n` remains unchanged, `a_1, a_2, ..., a_n` remain unchanged, `w` is equal to the initial value of `w`, `_` is equal to `w`, `ln` is the last input integer read during the last iteration, `palka` is the last list of integers read during the last iteration, `d` is a dictionary where each key is an integer from the last `palka` and its value is the count of how many times that integer appears in the last `palka`, `pl` is a list containing all unique integers from the last `palka` in the order they first appeared, and `shapes` is the number of unique integers in the last `palka` that appear 3 or more times.
#Overall this is what the function does:The function reads an integer `w` indicating the number of test cases. For each test case, it reads an integer `ln` representing the number of sticks and a list of integers representing the lengths of the sticks. It then calculates and prints the number of unique stick lengths that appear 3 or more times in the list for each test case. The function does not return any values; it only prints the results. After the function completes, the input variables `w`, `ln`, and the list of stick lengths remain unchanged, while the internal variables used for processing (such as `d`, `pl`, and `shapes`) will reflect the state of the last test case processed.

