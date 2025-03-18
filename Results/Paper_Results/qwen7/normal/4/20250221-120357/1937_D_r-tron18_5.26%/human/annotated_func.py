#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 5⋅10^5, and arr is a string of length n consisting of characters '<' and '>'.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the character at index -1 of `arr` minus the character at the index `max(-n, -1 - times)` of `arr`
#Overall this is what the function does:The function accepts a string `arr` consisting of characters '<' and '>' and an integer `times`. It returns the character at the last position of `arr` minus the character at the position determined by `max(-n, -1 - times)`, where `n` is the length of `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', where n is a positive integer.
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
        
    #State: All elements in `ans` are filled according to the logic defined within the loop, `totalOne` is 0, `preOne` is an empty list, and `suffZero` contains the cumulative sum of indices from the end of `s1` for each occurrence of '<'.
    print(*ans)
    #This is printed: the elements of the list ans (where the elements were determined by the logic within the loop)
#Overall this is what the function does:The function `func_2` accepts a string `s1` of length `n` consisting of characters '<' and '>' and an integer `n`. It calculates and returns a list `ans` where each element represents the balance of '<' and '>' characters up to that position in the string `s1`. The balance is determined based on the number of '>' characters encountered so far and the number of '<' characters from the end of the string up to that position. The function updates the list `ans` by iterating through the string `s1` from the end to the beginning and performing the necessary calculations. After completing the iteration, the function prints the elements of the list `ans`.

