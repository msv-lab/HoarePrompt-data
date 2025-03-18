#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball on the grid after each second, times is an integer representing the number of seconds passed, and l is the length of the grid (n).
def func_1(arr, times):
    l = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns the difference between the last position of the pinball in the list `arr` and the position of the pinball at the time `max(-l, -1 - times)` seconds ago.
#Overall this is what the function does:The function accepts a list of integers `arr` representing the positions of the pinball on a grid over time, an integer `times` representing the elapsed seconds, and an integer `l` representing the length of the grid. It calculates and returns the difference between the pinball's position at the current time and its position at a time `max(-l, -1 - times)` seconds ago.

#State of the program right berfore the function call: s1 is a string of length n consisting of characters '<' and '>', where n is a positive integer (1 ≤ n ≤ 5 × 10^5).
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
        
    #State: Output State: `totalOne` is 0, `s1` is a string of length `n` consisting of characters '<' and '>', `pre` is an empty list, `preOne` is an empty list, `suffZero` is a list of length `n+1` where each element is the sum of all indices up to that point in `s1`, `ans` is a list of length `n` with each element calculated based on the conditions inside the loop.
    print(*ans)
    #This is printed: the elements of the list ans (where each element is calculated based on the conditions inside the loop)
#Overall this is what the function does:The function `func_2` accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It calculates and returns a list `ans` of length `n`, where each element is determined based on the balance of '<' and '>' characters in `s1`. Specifically, for each character in `s1` from the end to the beginning, the function computes a value that reflects the difference between the number of zeros and ones under certain conditions, updating the list `ans` accordingly. After processing all characters, the function prints the list `ans`.

