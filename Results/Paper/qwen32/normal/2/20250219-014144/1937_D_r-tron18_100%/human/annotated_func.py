#State of the program right berfore the function call: arr is a list of integers representing some accumulated times or positions, and times is an integer representing the number of times a certain event has occurred, such that times >= 0.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of `arr` and the element at position `-n` if `times` is 0, or the element at position `-1 - times` if `times` is greater than 0.
#Overall this is what the function does:The function calculates and returns the difference between the last element of the list `arr` and another element in `arr` based on the value of `times`. If `times` is 0, it subtracts the first element of `arr`; otherwise, it subtracts the element at the position that is `times` steps before the last element.

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
        
    #State: `s1` is a string of length `n` consisting of characters '<' and '>'; `n` is a positive integer; `pre` is a list of integers representing the 1-based indices of '>' characters in `s1`; `totalOne` is 0; `preOne` is `[0]`; `suffZero` is a list of cumulative sums starting with 0 and including the cumulative sums of indices for '<' characters; `ans` is a list of `n` integers where each element is determined based on the conditions involving `ol`, `zr`, `zeroInd`, `oneInd`, and `fi`.
    print(*ans)
    #This is printed: [a1, a2, ..., an] (where ai are the integers in the ans list determined by the given conditions)
#Overall this is what the function does:The function `func_2` takes a string `s1` of length `n` consisting of characters '<' and '>', and computes a list of integers based on the positions of these characters. It then prints this list.

