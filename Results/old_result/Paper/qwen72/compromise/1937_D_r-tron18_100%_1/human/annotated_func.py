#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball on the grid, and times is a non-negative integer representing the number of times the pinball has moved.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last position of the pinball in the list `arr` and the position of the pinball `times` moves before the last position.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times`. It returns the difference between the last position in `arr` and the position `times` moves before the last position. If `times` is greater than or equal to the length of `arr`, it returns the difference between the last position and the first position in `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: `s1` remains unchanged, `pre` is empty, `totalOne` is 0, `preOne` is [0], `suffZero` is a list of length `n + 1` with all elements initialized to 0, `ans` is a list of length `n` with each element calculated based on the loop logic.
    print(*ans)
    #This is printed: [ans[0], ans[1], ..., ans[n-1]] (where each element of `ans` is calculated based on the loop logic, and `n` is the length of the `ans` list)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>', and a positive integer `n` such that 1 <= n <= 5 * 10^5. It calculates and prints a list `ans` of length `n`, where each element in `ans` represents a specific value derived from the positions of '<' and '>' characters in `s1`. The string `s1` remains unchanged after the function execution. The function does not return any value.

