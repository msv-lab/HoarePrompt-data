#State of the program right berfore the function call: arr is a list of integers representing positions, and times is a non-negative integer indicating the number of times a certain operation is applied, such that 0 <= times <= len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element in `arr` and the element at the position `max(-n, -1 - times)` from the end of `arr`. Here, `arr` is a list of integers representing positions, `times` is a non-negative integer indicating how many positions back from the end of the list to consider, and `n` is the number of elements in `arr`.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` and a non-negative integer `times` as inputs. It calculates and returns the difference between the last element in `arr` and the element that is `times` positions back from the end of the list. If `times` exceeds the length of `arr`, the function considers the first element of the list. The function does not modify the input list `arr`.

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
        
    #State: After the loop has executed all iterations, `s1` remains a string of length `n` consisting of characters '<' and '>'. The variable `n` is still a positive integer such that 1 <= `n` <= 5 * 10^5. The list `pre` still contains the 1-based indices of all '>' characters in `s1`. The variable `totalOne` is now 0, indicating that all '>' characters have been processed. The list `preOne` is empty, as it has been popped for each '>' character encountered. The list `suffZero` contains `n + 1` elements, where each element represents the cumulative sum of the indices of '<' characters encountered from the end of the string. The list `ans` is a list of length `n` where each element has been updated based on the conditions within the loop, reflecting the final result of the computation.
    print(*ans)
    #This is printed: [ans[0]] [ans[1]] ... [ans[n-1]] (where each element in ans is the result of the computation for the corresponding position in the string s1)
#Overall this is what the function does:The function `func_2` takes a string `s1` of length `n` consisting of characters '<' and '>', and a positive integer `n` (1 <= n <= 5 * 10^5). It processes the string to compute a list `ans` of length `n`, where each element in `ans` represents a specific calculation based on the positions of '<' and '>' characters in `s1`. After processing, the function prints the elements of `ans` in a space-separated format. The original string `s1` and the integer `n` remain unchanged. The list `ans` is the final output of the function, reflecting the computed values for each position in the string.

