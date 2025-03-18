#State of the program right berfore the function call: **
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of array `arr` minus the element at the index which is the maximum of -n and -1 minus `times`.
#Overall this is what the function does:Functionality: The function accepts an array `arr` and an integer `times`. It calculates and returns the difference between the last element of the array and the element at an index derived from the length of the array and the value of `times`. Specifically, it subtracts the element at the index which is the maximum of -n (where n is the length of the array) and -1 minus `times` from the last element of the array.

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
        
    #State: All elements in `ans` are updated according to the final conditions of the loop, and the lengths of `pre` and `preOne` are reduced by the number of iterations where `el` was '>', while `suffZero` contains the cumulative sums up to the last index processed.
    print(*ans)
    #This is printed: the elements of ans (where ans is the list updated according to the loop conditions)
#Overall this is what the function does:The function accepts a string `s1` of length `n` consisting of characters '<' and '>', and computes a list `ans` where each element represents the balance of '<' and '>' characters up to that position in the string. Specifically, for each character in `s1`, it calculates the difference between the count of '>' characters seen so far and the count of '<' characters seen so far, adjusted by the remaining indices. The function then prints the list `ans`.

