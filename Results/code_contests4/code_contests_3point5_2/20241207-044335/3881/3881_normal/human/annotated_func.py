#State of the program right berfore the function call: Each pair consists of a word (string) with at most 30 characters and a page number (integer) less than or equal to 1000. The number of pairs is less than or equal to 100.**
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict that can store lists where each list at key `word` contains all the integer values of `page` appended to it after each iteration of the loop
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: All integers in the lists corresponding to the keys in `index` are printed in sorted order
    exit()
#Overall this is what the function does:The function `func_1` processes pairs of words and page numbers from the input stream. It stores these pairs in a dictionary `index`, where each word is a key mapping to a list of corresponding page numbers. After processing, it prints each word followed by its associated page numbers in sorted order. The function does not accept any parameters and terminates after printing the processed data.

