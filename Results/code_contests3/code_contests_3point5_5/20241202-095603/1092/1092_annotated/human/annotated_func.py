#State of the program right berfore the function call: n is a positive integer representing the length of the text. The text consists of n words separated by single spaces, with each word consisting of small and capital Latin letters.**
def func():
    raw_input()
    l = raw_input().split()
    m = 0
    for i in l:
        s = 0
        
        for j in i:
            if j.isupper():
                s += 1
        
        m = max(s, m)
        
    #State of the program after the  for loop has been executed: `n` is a positive integer, `l` is a list of words, `m` is the maximum value between the total count of uppercase letters in all words in the list `l` and 0
    print(m)
#Overall this is what the function does:The function reads a text input consisting of words separated by spaces and calculates the maximum number of uppercase letters in a single word. It does not explicitly require any input parameters, so the annotations regarding `n` are irrelevant. The function does not return any value, it only prints the maximum count of uppercase letters in a word. Additionally, the function lacks error handling for cases where the input is not in the expected format or if there are no uppercase letters in any word.

