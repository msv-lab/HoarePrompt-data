#State of the program right berfore the function call: **
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the last element of array `arr` minus the element at the index which is the maximum of `-n` and `-1 - times`
#Overall this is what the function does:Functionality: The function accepts an array `arr` and an integer `times`. It calculates and returns the difference between the last element of `arr` and the element at an index determined by the maximum value between `-n` (where `n` is the length of `arr`) and `-1 - times`.

#State of the program right berfore the function call: s1 is a string consisting of characters '<' and '>', n is an integer representing the length of the string s1, and t is the number of test cases where 1 ≤ t ≤ 10^5 and for each test case 1 ≤ n ≤ 5 × 10^5.
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
        
    #State: Output State: `suffZero` is [1, 3, 6, 10], `ans` is [4, -2, 2, -2].
    print(*ans)
    #This is printed: 4 -2 2 -2
#Overall this is what the function does:The function accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It calculates and stores the result of certain conditions related to the characters in `s1` into a list `ans`. After processing, it prints the contents of `ans`. The final state of the program includes the `ans` list containing integers that represent the calculated values based on the input string `s1` and its length `n`.

