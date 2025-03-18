#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball in the grid, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element in the list `arr` and the element at the position `max(-n, -1 - times)` in the list `arr`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` (where `0 <= times <= len(arr)`). It returns the difference between the last element in `arr` and the element at the position `max(-n, -1 - times)` in `arr`. This effectively means it returns the difference between the last element and the element that is `times` positions before the last element, or the first element if `times` is greater than or equal to the length of `arr`.

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
        
    #State: `ans` is a list of length `n` where each element represents the difference between the sum of indices of all '<' characters to the right of the current index and the sum of indices of all '>' characters to the left of the current index, adjusted by the total length of the string `n` and the initial state of the lists `preOne` and `suffZero`. The lists `preOne` and `suffZero` are empty, and `totalOne` is 0.
    print(*ans)
    #This is printed: [difference between the sum of indices of '<' to the right and 0, adjusted by n] (for each element in the ans list)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>', and a positive integer `n` (1 <= n <= 5 * 10^5). It computes a list `ans` of length `n` where each element represents the difference between the sum of indices of all '<' characters to the right of the current index and the sum of indices of all '>' characters to the left of the current index, adjusted by the total length of the string `n`. After computing the list, it prints the elements of `ans` separated by spaces. The function does not return any value.

