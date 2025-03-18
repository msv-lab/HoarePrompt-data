#State of the program right berfore the function call: arr is a list of integers, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the index `max(-n, -1 - times)`. Here, `n` is the length of `arr`, and `times` is a non-negative integer such that 0 <= `times` <= `len(arr)`. The index `max(-n, -1 - times)` will always point to a valid element in the list, either the last element or an element before it, depending on the value of `times`.
#Overall this is what the function does:The function `func_1` accepts a list of integers `arr` and a non-negative integer `times`. It returns the difference between the last element of `arr` and the element at the index `max(-n, -1 - times)`, where `n` is the length of `arr`. The index `max(-n, -1 - times)` will always point to a valid element in the list, either the last element or an element before it, depending on the value of `times`. The function does not modify the input list `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting only of the characters '<' and '>', and n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: The loop has executed `n` times, and `i` is -1. `s1` remains a string of length `n` consisting only of the characters '<' and '>'. `pre` is a list of integers representing the 1-based indices of the characters in `s1` that are equal to '>'. `totalOne` is 0, indicating that all '>' characters have been processed. `preOne` is an empty list, as all elements have been removed during the loop execution. `suffZero` is a list containing the cumulative sums of the indices of '<' characters encountered during the loop, starting from 0. `ans` is a list of length `n` where each element has been updated based on the logic within the loop, reflecting the calculated values for each position in `s1`.
    print(*ans)
    #This is printed: [ans[0] ans[1] ... ans[n-1]] (where each ans[i] is the calculated value for the i-th position in the string s1)
#Overall this is what the function does:The function `func_2` accepts a string `s1` consisting only of the characters '<' and '>', and a positive integer `n` such that 1 <= n <= 5 * 10^5. It processes the string to calculate a list `ans` of length `n`, where each element `ans[i]` represents a specific value derived from the positions of '<' and '>' characters in `s1`. The function prints the elements of `ans` and does not return any value. After the function concludes, `s1` remains unchanged, `pre` is a list of the 1-based indices of '>' characters in `s1`, `totalOne` is 0, `preOne` is an empty list, and `suffZero` is a list containing cumulative sums of the indices of '<' characters encountered.

