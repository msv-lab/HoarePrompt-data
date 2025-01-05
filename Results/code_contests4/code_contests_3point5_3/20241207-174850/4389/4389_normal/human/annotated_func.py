#State of the program right berfore the function call: **
def func_1():
    n, m = list(map(int, le.pop().split()))
    a = list(map(int, le.pop().split()))
    if (m < n or n == 2) :
        af.append(-1)
        return None
        #The program does not return any value
    #State of the program after the if block has been executed: *`n` and `m` are assigned values based on the last element of the list `le`, `a` is a list containing integers from the last element of `le`. `m` is not less than `n` and `n` is not equal to 2
    af.append(2 * sum(a))
    for k in range(n):
        af.append(str(k + 1) + ' ' + str((k + 1) % n + 1))
        
    #State of the program after the  for loop has been executed: `n` and `m` are assigned values based on the last element of the list `le`, `a` is a list containing integers from the last element of `le`, `m` is not less than `n`, `n` is not equal to 2, `af` is appended with 2 times the sum of elements in list `a`, `af` contains the string representation of each number from 1 to `n` followed by a space and then the result of `(k + 1) % n + 1` for each `k` from 0 to `n-1`
#Overall this is what the function does:The function `func_1` reads input values for `n` and `m`, creates a list `a` based on the input, and appends specific values to the list `af`. If the condition `m < n` or `n == 2` is met, it appends -1 to `af`. Otherwise, it calculates 2 times the sum of elements in list `a` and appends the string representation of numbers from 1 to `n` followed by specific calculations to `af`. The function does not accept any parameters and does not return any value.

