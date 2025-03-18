#State of the program right berfore the function call: arr is a list of integers, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-l, -1 - times)` in the list `arr`, where `l` is the length of `arr` and `times` is a non-negative integer such that 0 <= `times` <= `l`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times` (where 0 <= `times` <= len(arr)). It returns the difference between the last element of `arr` and the element at the index `max(-l, -1 - times)`, where `l` is the length of `arr`. This means it calculates the difference between the last element and an element near the end of the list, depending on the value of `times`. If `times` is 0, it returns the difference between the last element and itself (which is 0). If `times` is greater than 0, it returns the difference between the last element and the element `times` positions before the last element.

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
        
    #State: `i` is `-1`, `el` is the last character of `s1` that was processed, `totalOne` is `0`, `preOne` is an empty list, `suffZero` is a list with `n + 1` elements, `ans` is a list of length `n` with all elements updated based on the loop logic.
    print(*ans)
    #This is printed: - The `print(*ans)` statement will print all elements of the list `ans` separated by spaces.
    #
    #Given the initial state and the context, the most precise description of the output is:
    #
    #Output:
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>', and a positive integer `n` such that 1 <= n <= 5 * 10^5. It processes the string and computes a list `ans` of length `n`, where each element in `ans` represents a specific calculation based on the positions of '<' and '>' characters in `s1`. After processing, the function prints the elements of `ans` separated by spaces. The final state of the program is that `ans` is a list of length `n` with all elements updated, and this list is printed to the console.

