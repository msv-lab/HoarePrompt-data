#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the second line of each test case contains n integers a_1, a_2, \ldots, a_n such that 1 ≤ a_i ≤ 100.
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
        
    #State: Output State: `shapes` is the total count of unique elements in `palka` that appear 3 or more times across all iterations, `palka` remains an empty list, `d` is a dictionary with updated counts of each element in `palka`, and `pl` is a list containing all unique elements from `palka` in the order they were first encountered.
    #
    #Explanation: After the loop has executed all its iterations, `shapes` will hold the cumulative count of unique elements in `palka` that appear 3 or more times. The list `palka` remains empty because the loop does not add any elements to it. The dictionary `d` will have updated counts of each element based on their occurrences across all iterations. The list `pl` will contain all unique elements from `palka` in the order they were first encountered, as no elements are added or removed from `pl` during the loop's execution.
#Overall this is what the function does:The function processes multiple test cases, where each test case consists of an integer n followed by n integers. It counts the number of unique integers that appear 3 or more times across all test cases and prints this count for each test case. The function does not return any value but prints the count of such unique integers for each test case.

