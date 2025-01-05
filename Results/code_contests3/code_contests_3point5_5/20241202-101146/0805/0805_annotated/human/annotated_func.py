#State of the program right berfore the function call: N is an integer such that 0 <= N <= 26. S is a string consisting of uppercase English letters with length between 1 and 10^4.**
def func():
    n = int(input())
    strings = input()
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_strings = ''
    for s in strings:
        index = letters.index(s)
        
        added_index = index + n
        
        new_index = added_index % 26
        
        new_s = letters[new_index]
        
        new_strings += new_s
        
    #State of the program after the  for loop has been executed: N is an integer between 0 and 26, S is a string of uppercase English letters, new_strings is a string containing the characters at the new_index positions in the letters list, strings is a non-empty string, s is the last character in the string S, index is assigned the index of the last character in the letters list, added_index is index + N, new_index is the remainder of added_index divided by 26
    print(new_strings)
#Overall this is what the function does:The function func takes an integer input N and a string S consisting of uppercase English letters. It then shifts each letter in the string S by N positions in the alphabet, wrapping around if necessary. The function outputs the modified string with the shifted letters. The code does not handle edge cases where N is outside the range of 0 to 26 or if the input string is empty.

