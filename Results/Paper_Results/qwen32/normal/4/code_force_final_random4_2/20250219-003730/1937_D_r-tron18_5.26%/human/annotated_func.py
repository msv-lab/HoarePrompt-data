#State of the program right berfore the function call: arr is a list of integers representing the time steps at which the pinball leaves the grid from certain positions, and times is an integer representing the number of seconds or the index related to the position from which the pinball is placed. The length of arr is at least 1, and times is a non-negative integer such that times is less than the length of arr.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index `max(-n, -1 - times)` in `arr`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at the index `max(-n, -1 - times)` in `arr`. The input list `arr` contains integers representing time steps, and `times` is a non-negative integer used to determine the index for the calculation.

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
        
    #State: `s1` remains unchanged, `pre` is an empty list, `totalOne` is 0, `preOne` is an empty list, `suffZero` contains cumulative sums of positions of '<' characters, and `ans` contains the updated values based on the loop conditions.
    print(*ans)
    #This is printed: the elements of the list `ans` (where `ans` is a list of values determined by the loop conditions)
#Overall this is what the function does:The function `func_2` processes a string `s1` of length `n` consisting of characters '<' and '>', and returns a list `ans` of length `n` where each element is computed based on the positions of '<' and '>' characters in the string. The specific computation involves cumulative sums and conditions based on the counts of '<' and '>' characters encountered. The string `s1` remains unchanged after the function execution.

