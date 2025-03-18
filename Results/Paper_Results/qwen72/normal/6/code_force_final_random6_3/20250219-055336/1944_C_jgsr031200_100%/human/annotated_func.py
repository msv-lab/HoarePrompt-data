#State of the program right berfore the function call: arr is a list of non-negative integers where each integer is less than the length of arr, and the length of arr is between 1 and 2 * 10^5.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: `arr` is a list of non-negative integers where each integer is less than the length of `arr`, and the length of `arr` is between 1 and 2 * 10^5. `freq` is a list where each element at index `i` corresponds to the number of times the integer `i` appears in `arr`.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: `arr` is a list of non-negative integers where each integer is less than the length of `arr`, and the length of `arr` is between 1 and 2 * 10^5. `freq` is a list where each element at index `i` corresponds to the number of times the integer `i` appears in `arr`. `n` remains unchanged, and `i` is the index at which the loop either prints a value and breaks or completes all iterations without printing. `cou` is 2 if two unique integers were found, otherwise it is 1 or 0. If `cou` is 2 or a 0 frequency integer is encountered, the loop prints that integer and breaks. If the loop completes all iterations without printing, `i` is `n + 1`.
#Overall this is what the function does:The function `func_1` accepts a list `arr` of non-negative integers, where each integer is less than the length of `arr`, and the length of `arr` is between 1 and 2 * 10^5. It calculates the frequency of each integer in `arr` and then prints the first integer that appears exactly once in `arr` if there are at least two unique integers, or the first integer that does not appear in `arr` if encountered. If no such integer is found, the function does not return any value.

