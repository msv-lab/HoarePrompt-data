#State of the program right berfore the function call: arr is a list of integers, times is an integer such that -len(arr) <= times <= len(arr) - 1.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of the list `arr` minus the element at the index `max(-l, -1 - times)` in the list `arr`
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It returns the difference between the last element of the list `arr` and the element at the index calculated as `max(-len(arr), -1 - times)` in the list `arr`. This calculation ensures that the index is within the bounds of the list, even if `times` is negative.

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
        
    #State: All elements in `ans` are calculated based on the conditions within the loop.
    print(*ans)
    #This is printed: elements of ans (where each element is calculated based on conditions within the loop)
#Overall this is what the function does:The function accepts a string `s1` of length `n` consisting of characters '<' and '>' and an integer `n`. It calculates and stores values in a list `ans` based on the positions of '>' in `s1`. For each character in `s1` from the last to the first, it determines a value to assign to the corresponding position in `ans` based on the counts of '>' and '<' encountered so far. Finally, it prints the contents of `ans`.

