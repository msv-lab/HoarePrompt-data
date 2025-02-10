#State of the program right berfore the function call: x is an integer representing the k-th element query index, where 1 ≤ x ≤ size of the array after all operations.
def func_1(x):
    x = int(x)
    if (x in b) :
        return b[x]
        #The program returns the value of the element at index x in the list b, where x is an integer representing the k-th element query index, and x is an element in the list b.
    #State: x is an integer representing the k-th element query index, where 1 ≤ x ≤ size of the array after all operations, and x is not in b
    for i in a:
        x = (x - 1) % i + 1
        
        if x in b:
            return b[x]
        
    #State: `x` is updated to `(x - 1) % i + 1` for each element `i` in `a`, and `a` has been fully iterated over. If at any point during the iteration `x` becomes an element in `b`, the program returns the value of `b` at the index `x`. Otherwise, the loop completes without returning, and `b` remains unchanged.
#Overall this is what the function does:The function `func_1` accepts an integer `x` representing the k-th element query index, where 1 ≤ x ≤ size of the array after all operations. It returns the value of the element at index `x` in the list `b` if `x` is an element in `b`. If `x` is not in `b`, the function iterates over each element `i` in list `a`, updating `x` to `(x - 1) % i + 1` for each `i`. During this iteration, if `x` becomes an element in `b`, the function returns the value of `b` at the updated index `x`. If no such `x` is found in `b` after iterating through all elements in `a`, the function does not return anything (implicitly returns `None`).

