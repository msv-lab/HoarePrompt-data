#State of the program right berfore the function call: The input is a non-empty string consisting of the characters 'C' and 'P', with a length not exceeding 100 characters.
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
        
    #State of the program after the  for loop has been executed: `count` is a non-negative integer representing the number of segments processed, `hand` is a list containing the last segment of matching characters from `str`, with a maximum length of 5.
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function accepts a non-empty string of 'C' and 'P' characters, counts the number of segments of consecutive identical characters (with a maximum segment length of 5), and prints the total segment count.

