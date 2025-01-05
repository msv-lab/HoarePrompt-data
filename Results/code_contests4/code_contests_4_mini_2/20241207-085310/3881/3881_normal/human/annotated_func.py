#State of the program right berfore the function call: The input consists of pairs of strings (words) and integers (page numbers), where each word is at most 30 characters long, the page number is a positive integer less than or equal to 1000, and the number of pairs does not exceed 100. Each word appears at most once per page.
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict with list as the default factory, containing pairs of words and their corresponding page numbers as lists of integers, corresponding to all lines read from stdin.
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict with list as the default factory containing all words as keys in sorted order; each word has been printed followed by its associated page numbers in sorted order.
    exit()
#Overall this is what the function does:The function processes pairs of strings (words) and positive integers (page numbers) inputted from standard input. It creates a mapping of each word to a list of page numbers where the word appears. After processing the input, it prints each word in sorted order followed by the sorted list of page numbers associated with that word. The function does not return any value but terminates after printing the results. It assumes valid input constraints such as words being at most 30 characters long, page numbers being positive integers not exceeding 1000, and each word appearing at most once per page.

