#State of the program right berfore the function call: a and b are binary strings, i is an integer representing the current index in string a being checked, and j is an integer representing the current index in string b being checked.
def func_1(a, b, i, j):
    index = b[j:].find(a[i])
    if (index != -1) :
        return j + index
        #The program returns the value of j plus index, where index is the starting position of a[i] in the substring of b starting from index j.
    else :
        return -1
        #The program returns -1
#Overall this is what the function does:The function accepts two binary strings `a` and `b`, and two integers `i` and `j`. It searches for the character `a[i]` in the substring of `b` starting from index `j`. If the character is found, it returns the value of `j` plus the starting index of `a[i]` within the substring of `b`. If the character is not found, it returns `-1`.

