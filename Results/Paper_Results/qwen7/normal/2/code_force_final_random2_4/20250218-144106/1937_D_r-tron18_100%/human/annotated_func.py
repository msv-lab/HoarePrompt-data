#State of the program right berfore the function call: arr is a list of integers, and times is an integer such that -n <= times <= 0.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of list `arr` and the element at the index calculated as `max(-n, -1 - times)`
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`. It calculates the difference between the last element of `arr` and the element at the index determined by `max(-n, -1 - times)`, where `n` is the length of `arr`. The function then returns this calculated difference.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', where n is a positive integer, and t is the number of test cases such that 1 ≤ t ≤ 10^5.
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
        
    #State: All elements in `ans` are calculated based on the final values of `s1`, `pre`, `totalOne`, and `preOne`, with `suffZero` updated to its final state.
    print(*ans)
    #This is printed: [s1, pre, totalOne, preOne] (where s1, pre, totalOne, and preOne are their respective final values)
#Overall this is what the function does:The function accepts a string `s1` of length `n` consisting of characters '<' and '>' and an integer `n`. It calculates and stores the difference between the count of zeros and ones for each position in the string based on the balance of '<' and '>' characters. The final state of the program includes an array `ans` containing these differences for each position in `s1`, and the updated states of `pre`, `totalOne`, and `preOne`. The function prints the array `ans`.

