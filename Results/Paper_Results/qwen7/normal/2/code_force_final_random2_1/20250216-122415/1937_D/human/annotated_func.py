#State of the program right berfore the function call: arr is a list of integers representing the positions of the pinball after each second, times is an integer representing the number of seconds to look back from the end of the array.
def func_1(arr, times):
    n = len(arr)
    return arr[-1] - arr[max(-n, -1 - times)]
    #The program returns 0
#Overall this is what the function does:The function accepts a list of integers `arr` and an integer `times`, calculates the difference between the last element of the list and the element `times` positions before the last element (if within bounds), and returns 0.

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
        
    #State: Output State: `totalOne` is equal to 0, `s1` is a string of length `n` consisting of characters '<' and '>', `pre` is a list of integers where each integer `i + 1` is added to the list if the character at index `i` in `s1` is '>', `preOne` is a list of cumulative sums starting from 0 without any elements (since `totalOne` is 0), `suffZero` is a list containing the cumulative sum of all indices `i + 1` for each character '<' in `s1` from the end to the beginning, `ans` is a list of zeros of length `n`, and `i` is -1 (indicating the loop has completed all its iterations).
    #
    #This means that after the loop completes all its iterations, `totalOne` will be 0 because it is decremented in each iteration until it reaches 0. The `pre` list will be modified according to the characters in `s1`, and `preOne` will be a list of cumulative sums of `pre` but will be empty since `totalOne` is 0. The `suffZero` list will contain the cumulative sum of all indices `i + 1` for each character '<' in `s1` from the end to the beginning, and `ans` will be a list of zeros of length `n` because no value is assigned to any index in `ans` during the loop's execution. The variable `i` will be -1, indicating that the loop has completed all its iterations.
    print(*ans)
    #This is printed: 0 0 0 ... 0 (n times)
#Overall this is what the function does:The function accepts a string `s1` consisting of characters '<' and '>' and an integer `n` representing the length of `s1`. It calculates and prints a list `ans` of length `n`, where each element is determined based on the positions of '>' and '<' in `s1`. Specifically, for each position `i` in `s1`, the value in `ans[i]` is computed using the counts of '>' and '<' characters to the left and right of position `i`. If the count of '>' characters to the left is less than or equal to the count of '<' characters to the right, or vice versa, the value in `ans[i]` is calculated accordingly. If neither condition is met, a more complex calculation involving cumulative sums is performed. After processing all positions in `s1`, the function prints a list of zeros of length `n`.

