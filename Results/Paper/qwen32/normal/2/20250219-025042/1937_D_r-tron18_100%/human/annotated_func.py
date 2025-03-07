#State of the program right berfore the function call: arr is a list of integers representing some cumulative or positional data, and times is an integer representing a specific index or offset into the list arr such that -len(arr) <= times < len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index `max(-n, -1 - times)` in `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at the index determined by `max(-len(arr), -1 - times)`. This effectively computes the difference between the last element and an element that is `times` positions before the end of the list, ensuring the index does not go out of bounds.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a positive integer representing the length of the string s1.
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
        
    #State: `s1` is the original string, `pre` is the original list of indices of '>' characters, `totalOne` is 0, `preOne` is [0], `suffZero` is a list of cumulative sums of indices of '<' characters, and `ans` is a list of integers calculated based on the loop conditions.
    print(*ans)
    #This is printed: [contents of ans] (where ans is a list of integers calculated based on the counts of '>' and '<' characters and their indices in the string s1)
#Overall this is what the function does:The function `func_2` takes a string `s1` of length `n` consisting of characters '<' and '>' and calculates a list of integers based on the positions and counts of these characters. The resulting list `ans` is printed, where each element is derived from specific conditions related to the indices of '>' and '<' characters in the string.

