#State of the program right berfore the function call: a and b are binary strings, i and j are non-negative integers representing the current indices of strings a and b respectively, such that 0 <= i <= len(a) and 0 <= j <= len(b).
def func_1(a, b, i, j):
    index = b[j:].find(a[i])
    if (index != -1) :
        return j + index
        #The program returns the position of `a[i]` in `b` starting from index `j`
    else :
        return -1
        #The program returns -1
#Overall this is what the function does:The function takes two binary strings `a` and `b`, and two non-negative integers `i` and `j`. It returns the position of the character `a[i]` in the string `b`, starting the search from index `j`. If `a[i]` is not found in `b` starting from index `j`, it returns -1.

