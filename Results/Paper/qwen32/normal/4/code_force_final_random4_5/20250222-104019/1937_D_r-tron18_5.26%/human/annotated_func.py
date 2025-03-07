#State of the program right berfore the function call: arr is a list of integers representing the time steps when the pinball leaves the grid from specific positions, and times is an integer representing the position from which the pinball is initially placed (0-indexed). The length of arr is at least 1, and times is a non-negative integer such that 0 <= times < len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element in the list `arr` and the element at the index `max(-n, -1 - times)` in the list `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the last element in the list `arr` and the element at the index determined by `max(-n, -1 - times)` in the list `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a non-negative integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: `s1` is unchanged, `pre` is unchanged, `totalOne` is 0, `preOne` is `[0]`, `suffZero` is a list of cumulative sums based on the positions of '<' characters, and `ans` is a list of `n` integers where each element is calculated based on the conditions described in the loop.
    print(*ans)
    #This is printed: ans (where ans is a list of n integers)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>', and computes a list of integers `ans` where each element is derived based on the positions of '<' and '>' characters in the string. The function prints the list `ans` after processing the string.

