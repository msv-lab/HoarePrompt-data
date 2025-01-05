#State of the program right berfore the function call: **
def func_1():
    n, m = list(map(int, le.pop().split()))
    a = list(map(int, le.pop().split()))
    if (m < n or n == 2) :
        af.append(-1)
        return None
        #The program returns None
    #State of the program after the if block has been executed: *`n` and `m` are assigned integer values from the list `le`, `a` is a list of integers from the popped element. The condition (m < n or n == 2) is false, meaning m is greater than or equal to n and n is not equal to 2
    af.append(2 * sum(a))
    for k in range(n):
        af.append(str(k + 1) + ' ' + str((k + 1) % n + 1))
        
    #State of the program after the  for loop has been executed: `n` and `m` are assigned integer values from the list `le`, `a` is a list of integers from the popped element, `af` contains a sequence of strings in the format 'k k+1' where k ranges from 1 to n (inclusive), where the second element in each string wraps around to 1 when it reaches n.
#Overall this is what the function does:The function `func_1` processes input values `n`, `m`, and list `a` obtained from the input list `le`. If the condition (m < n or n == 2) is met, the function appends -1 to the list `af` and returns None. If the condition is not met, it calculates 2 times the sum of elements in list `a`, appends this value to `af`, and generates a sequence of strings indicating pairs of numbers in the format 'k k+1' for k ranging from 1 to n. The function does not accept any parameters and always returns None.

