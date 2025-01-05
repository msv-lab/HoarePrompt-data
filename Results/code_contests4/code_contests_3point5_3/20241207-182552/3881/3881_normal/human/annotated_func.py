#State of the program right berfore the function call: Each pair consists of a word (string of at most 30 characters) and a page number (integer less than or equal to 1000). The number of pairs is less than or equal to 100. Each word appears in the pairs at most once.**
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a dictionary where each key is a word and the corresponding value is a list of page numbers associated with that word. Each word from the input pairs will have its page number appended to its list in the `index` dictionary.
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: `index` is a dictionary where each key is a word and the corresponding value is a list of page numbers associated with that word; `word` is the last word in the sorted list of keys. The sorted list of page numbers associated with the last word in the sorted list of keys is printed. The loop has executed for all words in the `index` dictionary.
    exit()
#Overall this is what the function does:The function `func_1` reads pairs of words and page numbers from the standard input. It then creates a dictionary `index` where each word is a key with a corresponding list of page numbers. The function prints each word followed by its sorted list of page numbers. Finally, the function exits without returning any value.

