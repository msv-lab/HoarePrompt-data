#State of the program right berfore the function call: list is a list of non-negative integers, and n is an integer representing the length of the list.
def func_1(list, n):
    for i in range(n):
        if list[i] != 0:
            return False
        
    #State: Output State: The list remains unchanged, and the value of n remains unchanged. The loop checks each element in the list; if any element is not zero, it returns False. If all elements are zero, it never returns and completes all iterations, but no changes are made to the list or n.
    return True
    #The program returns True, indicating that all elements in the list are zero.
#Overall this is what the function does:The function accepts a list of non-negative integers and an integer representing the length of the list. It checks whether all elements in the list are zero. If any element is not zero, it returns False immediately. If all elements are zero, it returns True after completing the iteration. The list and the integer n remain unchanged throughout the process.

#State of the program right berfore the function call: `list` is a list of integers representing the array `a`, and `n` is an integer such that 3 <= n <= 2 * 10^5. Each element in the list is an integer in the range [0, 10^9].
def func_2(list, n):
    for i in range(1, n - 1):
        while list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0:
            list[i - 1] -= 1 * list[i - 1]
            list[i] -= 2 * list[i - 1]
            list[i + 1] -= 1 * list[i - 1]
        
    #State: Output State: The list will be transformed such that for every element at index `i` (where 1 < i < n-1), if `list[i]` was greater than 1 and both `list[i-1]` and `list[i+1]` were greater than 0, then `list[i]` will be reduced by twice the value of `list[i-1]`, `list[i-1]` will be reduced by itself, and `list[i+1]` will be reduced by the value of `list[i-1]`. This process continues until the condition `list[i] > 1 and list[i - 1] > 0 and list[i + 1] > 0` is no longer satisfied for any `i`. The elements at the boundaries (`list[0]` and `list[n-1]`) remain unchanged throughout the process.
    if func_1(list, n) :
        print('YES')
        #This is printed: YES
    else :
        print('NO')
        #This is printed: NO
    #State: The list remains unchanged, all elements are integers, and for every element at index \(i\) (where \(1 < i < n-1\)), if \(list[i] > 1\) and both \(list[i-1] > 0\) and \(list[i+1] > 0\), then \(list[i]\) is reduced by twice the value of \(list[i-1]\), \(list[i-1]\) is reduced by itself, and \(list[i+1]\) is reduced by the value of \(list[i-1]\). This process continues until the condition \(list[i] > 1\) and \(list[i - 1] > 0\) and \(list[i + 1] > 0\) is no longer satisfied for any \(i\). The elements at the boundaries (\(list[0]\) and \(list[n-1]\)) remain unchanged throughout the process. The function `func_1(list, n)` returns `True` if the transformation is applied, otherwise the list remains unchanged.
#Overall this is what the function does:The function accepts a list of integers and an integer `n`. It iterates through the list (excluding the first and last elements) and, for each element, if it is greater than 1 and its adjacent elements are also greater than 0, it reduces the current element by twice the value of the previous element, the previous element by itself, and the next element by the value of the previous element. This process continues until no further reductions can be made under the given conditions. Finally, it calls another function `func_1(list, n)`. If `func_1` returns `True`, it prints 'YES', otherwise it prints 'NO'. The list is modified during the process, but the boundary elements remain unchanged.

