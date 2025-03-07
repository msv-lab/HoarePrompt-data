#State of the program right berfore the function call: arr is a list of integers, and times is an integer such that -len(arr) <= times <= len(arr) - 1.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of list `arr` minus the maximum of the last element of `arr` and the element at index `max(-n, -1 - times)` in `arr`
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It returns the last element of `arr` minus the maximum value between the last element of `arr` and the element at the index calculated as `max(-len(arr), -1 - times)` in `arr`. This calculation ensures that the index used is within the bounds of the list.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is an integer such that 1 <= n <= 5 * 10^5.
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
        
    #State: Output State: The loop has executed all its iterations, meaning `i` is now `-1`. At this point, `preOne` is a list where each element is the cumulative sum of the elements in `pre` starting from 0, but it has been reduced by the number of iterations (which is `n`). `totalOne` is 0 because it has been decremented until it reaches 0. `suffZero` is a list containing only 0, as it was appended to in each iteration but never removed from. `ans` is a list of length `n` filled with zeros, as no non-zero values were added to it within the loop since the conditions for updating `ans` were not met in any iteration.
    #
    #In natural language: After all iterations of the loop, the variable `i` has reached `-1`, indicating the loop has completed. The list `preOne` has been reduced to a size of `n` minus the number of iterations, `totalOne` is 0, `suffZero` contains only the initial 0, and `ans` remains a list of zeros of length `n`.
    print(*ans)
    #This is printed: 0 0 0 ... 0 (n times)
#Overall this is what the function does:The function accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It processes the string to compute a list `ans` of length `n`, where each element is calculated based on the positions of '>' characters in `s1`. After processing, it prints a list of zeros of length `n`.

