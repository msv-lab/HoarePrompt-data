#State of the program right berfore the function call: Each pair consists of a word (string) and a page number (integer), where the word has at most 30 characters and the page number is less than or equal to 1000. The number of pairs is less than or equal to 100. Each word appears on a page number at most once.
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict with `word` as key and a list containing all the integer values of `page` appended throughout all iterations of the loop.
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict with all keys sorted, each key's associated list is printed in sorted order containing all the integer values of `page` appended throughout all iterations of the loop.
    exit()
#Overall this is what the function does:The function `func_1` reads word-page pairs from the standard input, creates a dictionary where each word is a key mapped to a list of corresponding page numbers. It then prints each word followed by its associated page numbers in sorted order. The function does not accept any parameters and terminates after processing the input.

