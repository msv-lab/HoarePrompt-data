#State of the program right berfore the function call: n and c are integers where 2 ≤ n ≤ 100 and 0 ≤ c ≤ 100. x is a list of n integers where 0 ≤ xi ≤ 100, representing the price of a honey barrel on day i.
def func_1():
    string = raw_input()
    N, C = string.split(' ')
    N = int(N)
    C = int(C)
    x = raw_input().split(' ')
    tem = 0
    for i in range(N):
        x[i] = int(x[i])
        
    #State of the program after the  for loop has been executed: `n` and `c` are integers where 2 ≤ `n` ≤ 100 and 0 ≤ `c` ≤ 100, `x` is a list where the first `N` elements are now integers, `N` is a non-negative integer, `C` is an integer, `tem` is 0, `i` is `N-1` if `N` > 0, otherwise `i` is undefined.
    for i in range(len(x) - 1):
        if tem <= x[i] - x[i + 1] and x[i] - x[i + 1] - C > 0:
            tem = x[i] - x[i + 1]
        
    #State of the program after the  for loop has been executed: `n` and `c` are integers where 2 ≤ `n` ≤ 100 and 0 ≤ `c` ≤ 100, `x` is a list with at least 2 elements, `N` is a non-negative integer, `C` is an integer, `i` is `len(x) - 2`, and `tem` is the maximum value of `x[j] - x[j + 1]` for all `j` in the range `[0, len(x) - 2]` such that `x[j] - x[j + 1] - C > 0`. If no such `x[j] - x[j + 1]` exists, `tem` remains 0.
    if (tem > 0) :
        tem = tem - C
    #State of the program after the if block has been executed: *`n` and `c` are integers where 2 ≤ `n` ≤ 100 and 0 ≤ `c` ≤ 100, `x` is a list with at least 2 elements, `N` is a non-negative integer, `C` is an integer, `i` is `len(x) - 2`. If `tem` > 0, `tem` is updated to `tem - C`. Otherwise, `tem` remains 0.
    return tem
    #The program returns `tem`, which is 0 if `tem` was not greater than 0, or `tem - C` if `tem` was greater than 0, where `C` is an integer.
#Overall this is what the function does:The function `func_1` reads two inputs: a space-separated string containing two integers `N` and `C`, and a space-separated string of `N` integers representing prices. It then processes these inputs to find the maximum difference between consecutive prices (`x[i] - x[i + 1]`) such that the difference minus `C` is greater than 0. If such a difference exists, it returns the maximum difference minus `C`; otherwise, it returns 0. The function assumes valid input where `2 ≤ N ≤ 100`, `0 ≤ C ≤ 100`, and each price `0 ≤ x[i] ≤ 100`. Edge cases include when all price differences are less than or equal to `C`, resulting in a return value of 0.

