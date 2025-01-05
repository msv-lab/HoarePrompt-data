#State of the program right berfore the function call: The input is a non-empty string consisting of characters 'C' and 'P', with a length that does not exceed 100 characters.
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
        
    #State of the program after the  for loop has been executed: `str` is a non-empty string consisting of characters 'C' and 'P'; `n` is a positive integer not exceeding 100; `count` is the number of segments of different characters in `str`; `hand` is a list containing the last segment of identical characters (up to 5) from `str.
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function accepts a non-empty string consisting of characters 'C' and 'P', processes it to count the number of segments of different characters, where each segment can consist of up to 5 identical characters. It returns the total count of these segments, incrementing by one if the last segment is not empty. The function does not handle edge cases related to invalid characters in the input string or strings longer than 100 characters, as assumed by the precondition.

