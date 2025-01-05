#State of the program right berfore the function call: The input string consists of only the letters "C" and "P". The length of the string does not exceed 100 characters.**
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
        
    #State of the program after the  for loop has been executed: `count` is the number of times the conditions in the loop were not met, `hand` is a list containing elements based on the conditions. If the loop did not execute, `count` remains 0 and `hand` is an empty list.
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function `func` reads an input string that only contains the letters "C" and "P" with a maximum length of 100 characters. It then processes the string based on certain conditions, counting the number of times these conditions are not met. The function does not return any value but prints the final count after processing the string. The function handles cases where the input string is empty, or where the conditions are met repeatedly, ensuring accurate count calculation.

