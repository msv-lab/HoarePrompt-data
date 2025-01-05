#State of the program right berfore the function call: The input is a non-empty string consisting of letters "C" and "P", with a length not exceeding 100 characters.
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
        
    #State of the program after the  for loop has been executed: `count` is the number of times a new character was appended to `hand`, `hand` contains the last sequence of characters processed from `str` that either matched or reset, `n` is the length of `str`, and `i` is `n - 1`.
    print(count + (hand.__len__() != 0))
#Overall this is what the function does:The function accepts a non-empty string consisting of characters "C" and "P" with a maximum length of 100 characters. It counts the number of times a new character is appended to a list called `hand`, which maintains a sequence of the same character (either "C" or "P") but is limited to a length of 5. Whenever the current character does not match the last character in `hand` or exceeds the limit, it increments the count. The function then prints the total count, adjusted by adding 1 if there are remaining characters in `hand`. The final output reflects the number of character sequences encountered in the string.

