#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball after each second, times is an integer representing the number of seconds passed.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of list `arr` and the element at the index calculated as `max(-n, -1 - times)`
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It calculates the difference between the last element of the list `arr` and the element at an index determined by `max(-n, -1 - times)`, where `n` is the length of `arr`. The function then returns this calculated difference.

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
        
    #State: Output State: `totalOne` is `0`, `s1` is a string of length `n` consisting of characters '<' and '>', `pre` is an empty list, `preOne` is an empty list, `suffZero` is a list of integers where each integer is the cumulative sum of indices of '<' up to that point in `s1`, `ans` is a list of `n` integers calculated based on the conditions inside the loop.
    print(*ans)
    #This is printed: ans (where ans is a list of n integers calculated based on the conditions inside the loop involving the string s1 and other lists)
#Overall this is what the function does:The function `func_2` accepts a string `s1` consisting of characters '<' and '>' and its length `n`. It calculates and returns a list `ans` of `n` integers. Each element in `ans` represents the difference between the number of zeros and ones under certain conditions derived from the balance of '<' and '>' characters in `s1`. The function processes the string `s1` from right to left, updating the counts and lists used for calculations until it reaches the leftmost character. Finally, it prints the list `ans`.

