#State of the program right berfore the function call: arr is a list of integers representing the time points at which the pinball leaves the grid from specific positions, and times is an integer representing the number of seconds or the index offset used to calculate the difference in times.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index determined by `max(-n, -1 - times)`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at the index determined by `max(-n, -1 - times)`, where `n` is the length of `arr`. This effectively computes the difference between the last time point and a time point that is `times` positions before the last, with a safeguard to ensure the index does not go out of bounds.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a non-negative integer such that 0 <= n <= 5 * 10^5.
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
        
    #State: s1 is a string of length n consisting of characters '<' and '>', pre is a list of 1-based indices where the character '>' appears in s1, totalOne is 0, preOne is [0], suffZero is a list containing cumulative sums of indices of '<' characters, ans is a list of n values updated with the calculated differences.
    print(*ans)
    #This is printed: ans (where ans is a list of n values calculated based on the cumulative sums of '>' and '<' characters in the string s1)
#Overall this is what the function does:The function `func_2` takes a string `s1` of length `n` consisting of characters '<' and '>', and calculates a list of values based on the cumulative sums of indices of '>' and '<' characters in the string. The final output is a list `ans` of length `n` where each element represents a calculated difference based on the positions of '<' and '>' characters.

