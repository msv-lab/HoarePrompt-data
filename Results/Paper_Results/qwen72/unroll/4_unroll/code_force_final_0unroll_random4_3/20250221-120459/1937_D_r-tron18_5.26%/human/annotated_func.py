#State of the program right berfore the function call: arr is a list of integers, times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-n, -1 - times)`, where `n` is the length of `arr` and `times` is a non-negative integer such that 0 <= `times` <= `len(arr)`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` such that 0 <= `times` <= `len(arr)`. It returns the difference between the last element of `arr` and the element at the index `max(-len(arr), -1 - times)`. This means it calculates the difference between the last element and the element that is `times` positions from the end of the list. If `times` is 0, the difference is between the last element and itself, resulting in 0. If `times` is equal to the length of `arr`, the difference is between the last element and the first element of the list.

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
        
    #State: `s1` remains unchanged, `totalOne` is 0, `preOne` is empty, `suffZero` contains the cumulative sums of the indices of all '<' characters in `s1`, plus the initial 0, and `ans` contains the calculated values for each index in `s1`.
    print(*ans)
    #This is printed: [ans[0], ans[1], ..., ans[len(s1) - 1]] (where each ans[i] is the calculated value for the i-th index in the string s1)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>', where `n` is a positive integer between 1 and 500,000. It calculates and prints a list of integers `ans` of length `n`, where each `ans[i]` represents a value derived from the positions of '<' and '>' characters in `s1`. The string `s1` remains unchanged after the function execution. The final state of the program includes `s1` unchanged, `totalOne` set to 0, `preOne` being an empty list, and `suffZero` containing the cumulative sums of the indices of all '<' characters in `s1`, plus the initial 0. The list `ans` is printed, showing the calculated values for each index in `s1`.

