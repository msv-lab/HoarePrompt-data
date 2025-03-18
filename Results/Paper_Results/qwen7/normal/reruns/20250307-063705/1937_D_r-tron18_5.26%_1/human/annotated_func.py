#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball after each second, times is an integer representing the number of seconds that have passed, and n is the length of the grid.
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of the list `arr` minus the element at the index which is the maximum of -n and -1 minus the number of seconds that have passed (`times`).
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It calculates and returns the difference between the last element of `arr` and the element at an index determined by the maximum value between -n and -1 minus `times`.

#State of the program right berfore the function call: s1 is a string consisting of characters '<' and '>', and n is an integer representing the length of the string s1.
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
        
    #State: All elements in `ans` are calculated based on the final values of `totalOne`, `preOne`, and `suffZero`, with `i` being -1 after the loop completes.
    print(*ans)
    #This is printed: [values of ans] (where ans is a list populated based on the final values of totalOne, preOne, and suffZero)
#Overall this is what the function does:The function `func_2` accepts two parameters: `s1`, a string consisting of characters '<' and '>'; and `n`, an integer representing the length of the string `s1`. It calculates and populates a list `ans` based on the positions of '>' in `s1` and prints the list. If the length of `s1` is less than `n`, it does not return any value but prints an error message. Otherwise, it returns the populated list `ans` which contains values derived from the positions of '>' and '<' in `s1`.

