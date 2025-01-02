#State of the program right berfore the function call: S is a string of length N where 1 ≤ N ≤ 10^5, and each character in S is either '0' or '1'.
def func():
    s = input()
    c = 0
    for (i, a) in enumerate(s):
        if i % 2 == 0 and a == '0':
            c += 1
        
        if i % 2 == 1 and a == '1':
            c += 1
        
    #State of the program after the  for loop has been executed: `S` is a string of length `N` where `1 ≤ N ≤ 10^5`, and each character in `S` is either '0' or '1'; `s` is the input string (same as `S`); `c` is the count of characters in `s` where the character at an even index is '0' or the character at an odd index is '1'.
    print(min(c, len(s) - c))
#Overall this is what the function does:The function `func` reads a string `S` from the input, where `S` is a string of length `N` (1 ≤ N ≤ 10^5) consisting of characters '0' or '1'. It then counts the number of positions in `S` where the character at an even index is '0' or the character at an odd index is '1'. Finally, it prints the minimum of this count and the total number of characters in `S` minus this count. The function does not return any value; it only prints the result. Edge cases include strings of length 1, where the function will always print 0 if the string is '1' and 1 if the string is '0'. Additionally, if the string is empty, the function will raise an error because it expects input.

