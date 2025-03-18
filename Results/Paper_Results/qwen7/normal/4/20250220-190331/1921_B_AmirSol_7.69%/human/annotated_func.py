#State of the program right berfore the function call: n is an integer such that 1 <= n <= 10^5, s1 and s2 are strings of length n consisting of '0' and '1', where the i-th character of s1 is '1' if there is a cat in the i-th box and '0' otherwise, and the i-th character of s2 is '1' if there should be a cat in the i-th box and '0' otherwise.
def func_1(n, s1, s2):
    counter = 0
    i = 0
    while i < n:
        if s1[i] != s2[i]:
            if i < n - 1 and s1[i + 1] != s2[i + 1] and s1[i] != s1[i + 1]:
                counter += 1
                i += 2
            else:
                counter += 1
                i += 1
        else:
            i += 1
        
    #State: The final value of `counter` will be the total number of positions from 0 to n-1 where `s1[i]` is not equal to `s2[i]`. The value of `i` will be `n`, indicating that the loop has completed all iterations. `n` will remain the same as the initial value, and both `s1` and `s2` will retain their original string values.
    return counter
    #The program returns the total number of positions from 0 to n-1 where `s1[i]` is not equal to `s2[i]`
#Overall this is what the function does:The function accepts three parameters: an integer `n`, and two strings `s1` and `s2` of length `n` consisting of '0' and '1'. It counts and returns the total number of positions from 0 to `n-1` where `s1[i]` is not equal to `s2[i]`.

