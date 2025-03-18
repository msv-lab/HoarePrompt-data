#State of the program right berfore the function call: arr is a list of non-negative integers where each integer \(a_i\) satisfies \(0 \le a_i < n\), and \(n\) is the length of the list.
def func_1(arr):
    freq = [0] * (n + 1)
    for i in arr:
        freq[i] += 1
        
    #State: Output State: `freq` is a list of length `n + 1` where each element `freq[i]` represents the number of times `i` appears in the original list `arr`. All other variables remain unchanged.
    cou = 0
    for i in range(n + 1):
        if freq[i] >= 2:
            continue
        
        if freq[i] == 1:
            cou += 1
        
        if cou == 2 or freq[i] == 0:
            print(i)
            break
        
    #State: Output State: `cou` is 0, `freq` is a list of length `n + 1` where each element `freq[i]` represents the number of times `i` appears in the original list `arr`. No value is printed because the conditions to print (either `cou == 2` or `freq[i] == 0`) are not met for any `i` in the range of `n + 1`.
#Overall this is what the function does:The function accepts a list of non-negative integers `arr` and returns nothing. It calculates the frequency of each integer in `arr` and prints the first integer that appears exactly once or does not appear at all, breaking the loop once such an integer is found. If no such integer is found, it prints nothing.

