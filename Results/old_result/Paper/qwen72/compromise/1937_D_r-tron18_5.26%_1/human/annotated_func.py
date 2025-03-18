#State of the program right berfore the function call: arr is a list of integers, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-n, -1 - times)`, where `n` is the length of `arr` and `times` is a non-negative integer such that 0 <= times <= len(arr).
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` such that 0 <= times <= len(arr). It returns the difference between the last element of `arr` and the element at the index `max(-n, -1 - times)`, where `n` is the length of `arr`. After the function concludes, the input list `arr` remains unchanged, and the function provides a numerical result representing this difference.

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
        
    #State: s1 remains unchanged, pre remains unchanged, totalOne is 0, preOne is an empty list, suffZero is a list of length n + 1 containing cumulative sums of indices of '<' characters from the end of the string, ans is a list of length n with each element updated according to the loop logic.
    print(*ans)
    #This is printed: [ans[0] ans[1] ... ans[n-1]] (where each element ans[i] is the value of the i-th element in the list ans after the loop logic has been applied)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` containing only '<' and '>' characters, and a positive integer `n` within the range 1 to 5 * 10^5. It processes the string to compute a list `ans` of length `n`, where each element `ans[i]` is determined based on the positions of '<' and '>' characters in `s1`. The function prints the elements of `ans` and does not return any value. After the function concludes, `s1` remains unchanged, `pre` is a list of indices of '>' characters, `totalOne` is 0, `preOne` is an empty list, and `suffZero` is a list of length `n + 1` containing cumulative sums of indices of '<' characters from the end of the string.

