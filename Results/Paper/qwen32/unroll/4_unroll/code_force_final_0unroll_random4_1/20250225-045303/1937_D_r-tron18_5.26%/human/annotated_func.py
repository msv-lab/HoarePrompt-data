#State of the program right berfore the function call: arr is a list of integers representing the time steps at which the pinball reaches certain positions, and times is an integer representing the number of seconds or moves. The length of arr (l) is at least 1, and times is a non-negative integer.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index determined by `max(-l, -1 - times)` in the list `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the last time step in the list `arr` and the time step at a position determined by `times`. If `times` is greater than or equal to the length of `arr`, it compares the last element with the first element.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a positive integer such that len(s1) = n.
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
        
    #State: `s1` is unchanged, `pre` is unchanged, `totalOne` is 0, `preOne` is [], `suffZero` contains cumulative sums of indices of '<' characters, `ans` contains computed values based on the loop conditions.
    print(*ans)
    #This is printed: [contents of ans] (where ans contains computed values based on the loop conditions)
#Overall this is what the function does:The function `func_2` processes a string `s1` of length `n` consisting of characters '<' and '>', and computes a list of values based on the sequence of characters in `s1`. It prints this list as output. The string `s1` remains unchanged after the function execution.

