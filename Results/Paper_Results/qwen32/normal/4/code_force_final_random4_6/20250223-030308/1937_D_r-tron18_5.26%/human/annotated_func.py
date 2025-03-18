#State of the program right berfore the function call: arr is a list of integers representing some cumulative or processed times, and times is an integer representing the number of seconds or moves. The length of arr is denoted by l, which is a non-negative integer.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index determined by `max(-n, -1 - times)`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at an index determined by `max(-n, -1 - times)`. The index is effectively used to look back a certain number of positions from the end of the list, based on the value of `times`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a positive integer representing the length of the string s1.
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
        
    #State: `s1` remains unchanged, `pre` remains unchanged, `totalOne` is `0`, `preOne` is `[0]`, `suffZero` contains cumulative sums of indices for '<' characters, and `ans` is a list of `n` integers calculated based on the loop conditions.
    print(*ans)
    #This is printed: n integers (where n is the length of the list `ans` and the integers are the values calculated based on the loop conditions)
#Overall this is what the function does:The function `func_2` processes a string `s1` of length `n` consisting of characters '<' and '>'. It calculates and prints a list of `n` integers based on the positions and counts of '<' and '>' characters in the string. The final state of the program includes the original string `s1` remaining unchanged, while the output is a list of integers derived from the specified conditions and calculations within the function.

