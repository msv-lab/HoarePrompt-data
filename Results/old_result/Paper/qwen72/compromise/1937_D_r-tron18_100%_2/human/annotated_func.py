#State of the program right berfore the function call: arr is a list of integers, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-n, -1 - times)` in the list `arr`. Here, `n` is the length of `arr`, and `times` is a non-negative integer such that 0 <= `times` <= `n`. The index `max(-n, -1 - times)` ensures that the index is within the bounds of the list, and the returned value is the result of subtracting the element at this index from the last element of the list.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` (where 0 <= `times` <= len(arr)). It returns the difference between the last element of `arr` and the element at the index `max(-n, -1 - times)`, where `n` is the length of `arr`. This ensures the index is within the bounds of the list, and the returned value is the result of subtracting the element at this index from the last element of the list.

#State of the program right berfore the function call: s1 is a string of length n consisting only of characters '<' and '>', and n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: `ans` is a list of length `n` where each element represents the difference between the cumulative sum of the indices of '<' characters and the cumulative sum of the indices of '>' characters, adjusted based on the conditions inside the loop. `preOne` is an empty list. `totalOne` is 0. `suffZero` is a list with a single element 0.
    print(*ans)
    #This is printed: [ans[0], ans[1], ..., ans[n-1]] (where each element is the difference between the cumulative sum of the indices of '<' characters and the cumulative sum of the indices of '>' characters, adjusted based on the conditions inside the loop)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting only of characters '<' and '>', and a positive integer `n` such that 1 <= n <= 5 * 10^5. It computes a list `ans` of length `n` where each element represents the difference between the cumulative sum of the indices of '<' characters and the cumulative sum of the indices of '>' characters, adjusted based on the conditions inside the loop. After the function concludes, `ans` is printed as a list of integers, and the internal state of the function is such that `preOne` is an empty list, `totalOne` is 0, and `suffZero` is a list with a single element 0.

