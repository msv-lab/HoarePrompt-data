#State of the program right berfore the function call: **Precondition**: The input string consists of only the letters "C" and "P". The length of the string does not exceed 100 characters.
def func():
    str = raw_input()
    n = len(str)
    count = 0
    hand = []
    for i in range(0, n):
        if hand.__len__() == 0:
            hand.append(str[i])
        elif str[i] == hand[-1] and hand.__len__() < 5:
            hand.append(str[i])
        else:
            count = count + 1
            hand = [str[i]]
        
    #State of the program after the  for loop has been executed: `str` is a non-empty string consisting of only "C" and "P", `n` is the length of the string, `count` is the number of times a character changed in `hand` from "C" to "P" or vice versa, and `hand` is a list containing consecutive characters from `str` with a maximum length of 5.
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function reads an input string containing only "C" and "P", and then determines the number of times a character changes from "C" to "P" or vice versa consecutively. It prints the count of such changes along with checking if there are any remaining characters in the current consecutive sequence in the list `hand`.

