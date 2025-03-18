#State of the program right berfore the function call: arr is a list of integers representing the time steps at which the pinball leaves the grid from each cell, and times is an integer representing the index of the cell from which the pinball is initially placed, such that 0 <= times < len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at index `max(-n, -1 - times)` in the list `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at the index determined by `max(-n, -1 - times)` in the list `arr`.

#State of the program right berfore the function call: s1 is a string consisting of characters '<' and '>', and n is a non-negative integer such that n equals the length of s1.
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
        
    #State: `s1` is a string consisting of characters '<' and '>', `n` is a non-negative integer such that `n` equals the length of `s1`, `pre` is a list of 1-based indices where the character '>' appears in `s1`, `totalOne` is 0, `preOne` is an empty list, `suffZero` is a list containing cumulative sums of indices for '<' characters, `ans` is a list of `n` integers calculated based on the loop conditions.
    print(*ans)
    #This is printed: ans (where ans is a list of n integers calculated based on the loop conditions involving preOne and suffZero)
#Overall this is what the function does:The function `func_2` processes a string `s1` consisting of '<' and '>' characters, along with its length `n`, to compute and print a list `ans` of integers. The list `ans` is derived based on the positions of '<' and '>' characters in `s1` and specific calculations involving cumulative sums and indices.

