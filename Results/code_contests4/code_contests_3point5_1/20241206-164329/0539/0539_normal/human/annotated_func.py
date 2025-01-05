#State of the program right berfore the function call: sum and limit are integers such that 1 ≤ sum, limit ≤ 105.**
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
        
    #State of the program after the  for loop has been executed: A is a list containing tuples of the form (2
    if (s < target) :
        print(-1)
        exit()
    #State of the program after the if block has been executed: *A is a list containing tuples of the form (2, s), where s is less than target.
    A.sort()
    selected = []
    for tup in A:
        target -= tup[0]
        
        selected.append(tup[1])
        
        if target <= 0:
            break
        
    #State of the program after the  for loop has been executed: A is a list containing sorted tuples of the form (2, s) in ascending order of s values, selected is a list containing the values of s from the tuples in list A until the sum of the first elements of the tuples in A is greater than or equal to the initial value of target, target is less than or equal to 0 after all iterations of the loop have finished.
    print(len(selected))
    print(' '.join(map(str, selected)))
#Overall this is what the function does:The function reads input values for target and n, then iterates through a loop to calculate values based on conditions involving bitwise operations and logarithmic calculations. After sorting the calculated values, it selects elements from the list A until the sum of the first elements reaches the target value or exceeds it. Finally, it prints the number of selected elements and their corresponding values.

