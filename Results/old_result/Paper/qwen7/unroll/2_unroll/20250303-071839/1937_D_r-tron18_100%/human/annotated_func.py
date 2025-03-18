#State of the program right berfore the function call: arr is a list of integers, and times is an integer such that -len(arr) <= times <= len(arr) - 1.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of the list 'arr' minus the maximum of the last element of 'arr' or the element at index 'max(-n, -1 - times)' in 'arr'.
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It returns the last element of `arr` minus the maximum of the last element of `arr` or the element at index `max(-len(arr), -1 - times)` in `arr`. This means if `times` is non-positive, it subtracts the last element of `arr` from itself, resulting in zero. If `times` is positive, it subtracts either the last element of `arr` or the element at the calculated index, whichever is greater.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', where n is a positive integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: ans is a list of n elements, preOne is an empty list, totalOne is 0, suffZero is a list containing the value [0].
    print(*ans)
    #This is printed: [element1, element2, ..., elementN]
#Overall this is what the function does:The function accepts a string `s1` and an integer `n`, and calculates and prints a list of integers `ans` based on the positions of '>' characters in `s1`. For each position `i` in `s1`, `ans[i]` contains a value calculated based on the number of '>' characters to the left and the number of positions to the right. The function modifies the input string `s1` and constructs the list `ans` which is printed at the end.

