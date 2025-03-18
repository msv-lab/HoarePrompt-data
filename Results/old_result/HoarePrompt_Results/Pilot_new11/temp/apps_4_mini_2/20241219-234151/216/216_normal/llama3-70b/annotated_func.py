#State of the program right berfore the function call: n is an integer between 1 and 200, and s is a string consisting only of lowercase and uppercase Latin letters with a length equal to n.
def func():
    n = int(input())
    s = input()
    lowercase = [i for i, c in enumerate(s) if c.islower()]
    print(len(lowercase))
#Overall this is what the function does:The function reads an integer n and a string s from user input. It then counts the number of lowercase letters in the string s and prints this count. The inputs are constrained such that n is between 1 and 200, and the length of s matches this value. The function does not return a value but outputs the count of lowercase letters directly. Notably, the function lacks error handling for unexpected input formats and does not validate that the length of s is equal to n, which could lead to potential inconsistencies if the input is incorrect.

