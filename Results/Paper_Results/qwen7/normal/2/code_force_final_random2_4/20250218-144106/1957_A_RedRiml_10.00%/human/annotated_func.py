#State of the program right berfore the function call: t is an integer such that 1 ≤ t ≤ 100. For each test case, n is an integer such that 1 ≤ n ≤ 100, and the list of stick lengths a_1, a_2, \ldots, a_n consists of integers such that 1 ≤ a_i ≤ 100.
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
        
    #State: Output State: `shapes` is equal to the number of unique elements in `palka` whose count in `d` is greater than or equal to 3, `d` is a dictionary where each key from the list `palka` is mapped to its count in `palka`, and `pl` is a list containing all unique elements from `palka` in the order they appeared.
    #
    #Explanation: After the loop has executed all its iterations, the value of `shapes` will be equal to the number of unique elements in `palka` whose count in the dictionary `d` is greater than or equal to 3. The dictionary `d` will hold the counts of each key from the list `palka`, and the list `pl` will contain all unique elements from `palka` in the order they appeared, as no modifications are made to `pl` within the loop body other than appending new unique elements.
#Overall this is what the function does:The function processes multiple test cases, where for each test case, it reads an integer `w` representing the number of test cases, followed by `w` sets of inputs. Each set includes an integer `n` and a list of `n` integers representing stick lengths. It then calculates and prints the number of unique stick lengths that appear at least three times in the input list for each test case.

