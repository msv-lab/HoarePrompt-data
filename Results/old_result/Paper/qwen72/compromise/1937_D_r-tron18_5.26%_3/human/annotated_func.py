#State of the program right berfore the function call: arr is a list of integers, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-l, -1 - times)`, where `l` is the length of `arr` and `times` is a non-negative integer such that 0 <= times <= l.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` (where 0 <= `times` <= len(arr)). It returns the difference between the last element of `arr` and the element at the index `max(-len(arr), -1 - times)`. This effectively means it returns the difference between the last element and the element that is `times` positions before the last element in the list. If `times` is 0, it returns 0. If `times` is equal to the length of the list, it returns the difference between the last element and the first element.

#State of the program right berfore the function call: s1 is a string of length n, consisting only of characters '<' and '>', and n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: `ans` is a list of length `n` where each element represents the difference in the cumulative sum of the positions of '>' characters and the cumulative sum of the positions of '<' characters up to that index, adjusted by the total length of the string and the position of the characters. `preOne` is an empty list. `suffZero` is a list with a single element, 0. `totalOne` is 0.
    print(*ans)
    #This is printed: [element_0] [element_1] ... [element_n-1] (where each element_i is the difference in the cumulative sum of the positions of '>' characters and the cumulative sum of the positions of '<' characters up to index i, adjusted by the total length of the string and the position of the characters)
#Overall this is what the function does:The function `func_2` accepts a string `s1` and an integer `n`. The string `s1` consists only of characters '<' and '>', and `n` is the length of `s1`, with the constraint 1 <= n <= 5 * 10^5. After processing, the function prints a list `ans` of length `n`, where each element at index `i` represents the difference in the cumulative sum of the positions of '>' characters and the cumulative sum of the positions of '<' characters up to that index, adjusted by the total length of the string and the positions of the characters. The function does not return any value; it only prints the result.

