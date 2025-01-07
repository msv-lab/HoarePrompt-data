#State of the program right berfore the function call: lst is a list, and n is a positive integer such that 0 < n <= len(lst).
def func_1(lst, n):
    result = [[] for _ in range(n)]
    for (i, element) in enumerate(lst):
        result[i % n].append(element)
        
    #State of the program after the  for loop has been executed: `lst` is a list with at least `n` elements, `result` is a list of `n` lists where each list contains every `n`-th element from `lst`.
    return result
    #`The program returns a list 'result' where each element is a list containing every nth element from the original list 'lst'`
#Overall this is what the function does:The function `func_1` accepts a list `lst` and a positive integer `n`, and returns a list `result` where each element is a list containing every \(n\)-th element from the original list `lst`. Specifically, the function creates a list of \(n\) sublists, and for each element in `lst`, it appends the element to the sublist indexed by its position modulo \(n\). This ensures that each sublist contains elements from `lst` at intervals of \(n\).

