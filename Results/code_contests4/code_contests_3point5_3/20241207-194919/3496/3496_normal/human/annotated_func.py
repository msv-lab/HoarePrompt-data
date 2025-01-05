#State of the program right berfore the function call: The input string consists of only "C" and "P" characters.**
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
        
    #State of the program after the  for loop has been executed: `count` is the number of times the condition `str[i] != hand[-1] or hand.__len__() == 5` is met, `hand` is a list containing the last consecutive sequence of characters from the string `str` that are the same and less than 5 in length, `n` is the total number of elements in the string `str`, `i` is the last index processed by the loop
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function `func` reads a string input consisting of only "C" and "P" characters. It then iterates through the string, keeping track of consecutive sequences of characters that are the same and less than 5 in length. The function counts the number of times the condition `str[i] != hand[-1] or hand.__len__() == 5` is met and prints the count along with 1 if there is still a sequence being processed. The function does not have a specific output or return value.

