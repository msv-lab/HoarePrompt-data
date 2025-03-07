#State of the program right berfore the function call: arr is a list of integers representing cumulative times at which the pinball would leave the grid from certain positions, and times is an integer representing the offset used to determine the starting point for calculating the difference in times.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at the index determined by `max(-n, -1 - times)`.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and the element at the index determined by `max(-n, -1 - times)`, where `n` is the length of `arr`. This effectively computes the difference between the last cumulative time and a previous cumulative time based on the offset `times`.

#State of the program right berfore the function call: s1 is a string consisting of characters '<' and '>', and n is a non-negative integer representing the length of the string s1 such that n = len(s1).
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
        
    #State: 
    print(*ans)
    #This is printed: the elements of ans separated by spaces (where ans is an iterable containing the values to be printed)
#Overall this is what the function does:The function `func_2` processes a string `s1` composed of '<' and '>' characters, calculating and returning a list of integers `ans` where each element corresponds to a computed value based on the positions of '<' and '>' in the string.

