#State of the program right berfore the function call: arr is a list of integers representing positions, and times is a non-negative integer such that 0 <= times <= len(arr).
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last element of the list `arr` and the element at the position `max(-n, -1 - times)` in the list `arr`. Here, `arr` is a list of integers representing positions, `times` is a non-negative integer such that 0 <= `times` <= len(`arr`), and `n` is the length of `arr`. The position `max(-n, -1 - times)` ensures that the index does not go out of bounds.
#Overall this is what the function does:The function `func_1` takes a list of integers `arr` and a non-negative integer `times` (where `0 <= times <= len(arr)`). It returns the difference between the last element of `arr` and the element at the position `max(-n, -1 - times)`, where `n` is the length of `arr`. This ensures that the index does not go out of bounds. The function does not modify the input list `arr`.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', and n is a positive integer such that 1 ≤ n ≤ 5 * 10^5.
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
        
    #State: After the loop executes all iterations, `i` is -1, `el` is the first character of `s1`, `totalOne` is 0, `preOne` is empty, `suffZero` contains the cumulative sums of the 1-based indices of all '<' characters in `s1`, and `ans` contains the computed values for each position in the string `s1`.
    print(*ans)
    #This is printed: the computed values for each position in the string s1 (where s1 is the input string and ans contains the computed values for each position in s1)
#Overall this is what the function does:The function `func_2` takes a string `s1` of length `n` consisting of characters '<' and '>', and a positive integer `n` within the range 1 ≤ n ≤ 5 * 10^5. It computes a list `ans` of length `n`, where each element in `ans` represents a specific value derived from the positions of '<' and '>' characters in `s1`. After computing these values, the function prints the elements of `ans` separated by spaces. The final state of the program is that `ans` contains the computed values for each position in the string `s1`, and these values are printed to the console.

