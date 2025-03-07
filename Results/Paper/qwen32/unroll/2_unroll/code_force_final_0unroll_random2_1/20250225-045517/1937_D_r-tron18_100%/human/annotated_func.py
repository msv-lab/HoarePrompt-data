#State of the program right berfore the function call: arr is a list of integers representing the time at which the pinball leaves the grid from each cell, and times is an integer representing the index of the cell from which the pinball is initially placed, such that 0 <= times < len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `-1 - times` in the list `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the time at which the pinball leaves the grid from the last cell and the time at which it leaves from the cell that is `times + 1` positions from the end of the list `arr`. If `times` is such that `-1 - times` is out of bounds, it uses the first element of the list instead.

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
        
    #State: `s1` is unchanged, `pre` is unchanged, `totalOne` is 0, `preOne` is [], `suffZero` is a list of `n` cumulative sums of indices of '<' characters from the end to the start, and `ans` is a list of computed values based on the positions of '<' and '>' characters.
    print(*ans)
    #This is printed: [elements of ans] (where ans is a list of computed values based on the positions of '<' and '>' characters)
#Overall this is what the function does:The function takes a string `s1` of length `n` composed of '<' and '>' characters and computes a list of values based on the positions of these characters. The final output is a list `ans` that contains computed values related to the positions of '<' and '>' characters in the string. The string `s1` remains unchanged after the function execution.

