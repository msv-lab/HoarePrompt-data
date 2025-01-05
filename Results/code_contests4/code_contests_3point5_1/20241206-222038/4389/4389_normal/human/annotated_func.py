#State of the program right berfore the function call: **
def func_1():
    n, m = list(map(int, le.pop().split()))
    a = list(map(int, le.pop().split()))
    if (m < n or n == 2) :
        af.append(-1)
        return None
        #The program appends -1 to the list 'af'
    #State of the program after the if block has been executed: *`n` and `m` are assigned integer values extracted from the last element of list `le`. The condition (m >= n and n != 2) is satisfied
    af.append(2 * sum(a))
    for k in range(n):
        af.append(str(k + 1) + ' ' + str((k + 1) % n + 1))
        
    #State of the program after the  for loop has been executed: `n` and `m` are assigned integer values extracted from the last element of list `le`, `af` contains the appended value of 2 times the sum of elements in list `a`, `n` is greater than or equal to 0, `m` is greater than or equal to `n`, `n` is not equal to 2
#Overall this is what the function does:The function func_1 extracts integer values for n and m from the last element of list `le`, then appends -1 to the list `af` if either m is less than n or n is equal to 2. If neither condition is met, the function calculates 2 times the sum of elements in list `a` and appends it to `af`. Additionally, the function appends strings representing pairs of numbers from 1 to n in `af`.

