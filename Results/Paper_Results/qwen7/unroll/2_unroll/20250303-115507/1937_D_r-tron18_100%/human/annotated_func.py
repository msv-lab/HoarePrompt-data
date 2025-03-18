#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball on the grid after each second, times is an integer representing the initial cell index (0-based) where the pinball is placed on the grid.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last position of the pinball in the list `arr` and the position of the pinball at the index `max(-n, -1 - times)` in the list `arr`.
#Overall this is what the function does:The function accepts a list of integers `arr` representing the positions of the pinball on a grid over time and an integer `times` representing the initial cell index. It calculates and returns the difference between the last position of the pinball in the list and the position of the pinball at an index determined by `max(-n, -1 - times)`, where `n` is the length of the list `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is an integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: Output State: `totalOne` is 0, `s1` is a string of length `n` consisting of characters '<' and '>', `pre` is an empty list, `preOne` is an empty list, `suffZero` is a list of length `n+1` where each element is the cumulative sum of indices from `s1` in reverse order starting from 0, `ans` is a list of `n` integers calculated based on the conditions within the loop.
    print(*ans)
    #This is printed: the elements of the list ans (where ans is a list of n integers calculated based on the conditions within the loop)
#Overall this is what the function does:The function `func_2` accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It calculates and returns a list `ans` of `n` integers. Each element in `ans` represents the difference between the number of zeros and ones under certain conditions derived from the balance of '<' and '>' characters in `s1`. The function processes the string `s1` from right to left, updating the counts and lists `preOne` and `suffZero` accordingly, and finally prints the list `ans`.

