#State of the program right berfore the function call: a and b are binary strings, i and j are non-negative integers such that 0 <= i <= len(a) and 0 <= j <= len(b).
def func_1(a, b, i, j):
    index = b[j:].find(a[i])
    if (index != -1) :
        return j + index
        #The program returns the value of j plus the index of the first occurrence of a[i] in b[j:]
    else :
        return -1
        #The program returns -1
#Overall this is what the function does:The function accepts two binary strings `a` and `b`, and two non-negative integers `i` and `j`. It searches for the character at index `i` of string `a` within the substring of string `b` starting from index `j`. If the character is found, it returns the index of the first occurrence relative to `j`. If the character is not found, it returns `-1`.

