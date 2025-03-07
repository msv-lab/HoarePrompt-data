#State of the program right berfore the function call: t is an integer where 1 ≤ t ≤ 100, representing the number of test cases. For each test case, n is an integer where 1 ≤ n ≤ 100, representing the number of sticks, and a_1, a_2, ..., a_n are integers where 1 ≤ a_i ≤ 100, representing the lengths of the sticks.
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
        
    #State: `t` is an integer where 1 ≤ t ≤ 100, `n` is an integer where 1 ≤ n ≤ 100, `a_1, a_2, ..., a_n` are integers where 1 ≤ a_i ≤ 100, `w` is equal to the initial value of `w` (an integer), `_` is `w - 1`, `ln` is an input integer, `palka` is a list of integers read from input, `pl` is a list containing all unique elements from `palka`, `d` is a dictionary where each key is an element from `palka` and the value is the count of how many times that element appears in `palka`, `shapes` is the number of unique elements in `pl` that appear at least 3 times in `palka`.
#Overall this is what the function does:The function `func` reads multiple sets of inputs from the standard input. Each set starts with an integer `w` indicating the number of test cases. For each test case, it reads another integer `ln` representing the number of sticks, followed by a list of stick lengths. It then calculates and prints the number of unique stick lengths that appear at least three times in the list for each test case. The function does not return any value; it only prints the results to the standard output. After the function completes, the input variables `w`, `ln`, `palka`, `pl`, `d`, and `shapes` will have been modified according to the processing of the inputs, but their final states are not retained outside the function.

