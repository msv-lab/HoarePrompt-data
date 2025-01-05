#State of the program right berfore the function call: sum and limit are integers such that 1 <= sum, limit <= 10^5.**
def func():
    target, n = map(int, raw_input().split())
    A = []
    s = 0
    for i in range(1, n + 1):
        k = (i & -i) - 1
        
        if i != 1 and k == i - 1:
            k = int(math.log(i, 2))
        
        A.append((2 ** k, i))
        
        s += A[-1][0]
        
    #State of the program after the  for loop has been executed: `A` is a list containing tuples where the first element is 2 raised to the power of the value assigned to `k` for each `i` from 1 to `n`, and the second element is the value of `i`, `s` is the sum of the first elements of all tuples in list `A`, `n` is a positive integer
    if (s < target) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *`A` is a list containing tuples where the first element is 2 raised to the power of the value assigned to `k` for each `i` from 1 to `n`, the second element is the value of `i`, `s` is the sum of the first elements of all tuples in list `A`, `n` is a positive integer. If the sum `s` of the first elements of tuples in list `A` is less than `target`, then the state remains unchanged.
    A.sort()
    selected = []
    for tup in A:
        target -= tup[0]
        
        selected.append(tup[1])
        
        if target <= 0:
            break
        
    #State of the program after the  for loop has been executed: After the loop finishes executing, `A` is a list containing tuples sorted in ascending order based on the first element, `s` is the sum of the first elements of all tuples in list `A`, `n` is a positive integer, `selected` contains the second elements of the tuples in list `A` until the sum of the first elements in the selected tuples is greater than or equal to `s`. If the sum of the first elements in `selected` is less than `s`, then `selected` will contain all the second elements of the tuples in `A`.
    print(len(selected))
    print(' '.join(map(str, selected)))
#Overall this is what the function does:The function `func` reads input from the user, processes the input to create a list of tuples, sorts the list based on the first element of the tuples, and selects elements from the list until a certain target value is reached. It then prints the number of selected elements and the selected elements. The function does not accept any parameters.

