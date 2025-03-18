#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball on the grid at different times, where the index represents the time step and the value at each index represents the cell position. times is an integer representing the initial time step when the pinball is placed on the grid (1 <= times <= n).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element in the list `arr` and the element at the index calculated as `max(-l, -1 - times)`
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It calculates the difference between the last element in the list `arr` and the element at an index derived from `times`, ensuring the index is within valid bounds. The function then returns this calculated difference.

#State of the program right berfore the function call: s1 is a string consisting of characters '<' and '>', and n is an integer such that 1 <= n <= 5 * 10^5 and s1 has length n.
def func_2(s1, n):
    pre = [(i + 1) for i, el in enumerate(s1) if el == '>']
    totalOne = len(pre)
    preOne = list(accumulate(pre, initial=0))
    suffZero = [0]
    ans = [0] * n
    for i in range(n - 1, -1, -1):
        el = s1[i]
        
        if el == '>':
            ol, zr = totalOne, len(suffZero) - 1
            if ol <= zr:
                zeroInd = 2 * func_1(suffZero, ol)
                oneInd = 2 * preOne[-1] - func_1(preOne, 1)
                ans[i] = zeroInd - oneInd
            else:
                zeroInd = 2 * suffZero[-1]
                oneInd = func_1(preOne, zr) + func_1(preOne, zr + 1)
                oneInd -= func_1(preOne, 1)
                fi = func_1(preOne, zr + 1) - func_1(preOne, zr)
                ans[i] = zeroInd - oneInd + n + 1 - fi
            preOne.pop()
            totalOne -= 1
        else:
            suffZero.append(suffZero[-1] + i + 1)
            ol, zr = totalOne, len(suffZero) - 1
            if zr <= ol:
                zeroInd = suffZero[-1] + suffZero[-2]
                oneInd = 2 * func_1(preOne, zr)
                ans[i] = zeroInd - oneInd + n + 1
            else:
                zeroInd = 2 * func_1(suffZero, ol + 1) - func_1(suffZero, 1)
                oneInd = 2 * preOne[-1]
                ans[i] = zeroInd - oneInd
        
    #State: After the loop executes all iterations, `i` will be `-1`, meaning the loop has completed its execution. The value of `el` will be irrelevant since `i` is out of bounds. `suffZero` will contain the cumulative sum of indices of characters `>` in `s1` from the end, adjusted according to the loop's logic. `ol` will be `totalOne` (or `totalOne - 1` if the last element processed was `'> '`). `zr` will be the length of `suffZero` minus 1. `preOne` will be empty as it is reduced by one element in each iteration until it is exhausted. `ans` will contain the calculated values for each index `i` processed by the loop, adjusted by the conditions specified within the loop body.
    print(*ans)
    #This is printed: the calculated values in the list ans
#Overall this is what the function does:The function `func_2` accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It calculates and returns a list `ans` where each element represents a specific balance value based on the characters '<' and '>' in `s1`. The calculation involves iterating through `s1` from the end to the beginning, updating counts and indices, and adjusting the balance values according to the encountered characters. The final state of the program is the printing of the list `ans`, which contains the calculated balance values for each position in `s1`.

