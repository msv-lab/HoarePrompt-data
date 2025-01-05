#State of the program right berfore the function call: The input consists of pairs of strings (words) and integers (page numbers), where each word is a string with at most 30 characters and each page number is an integer less than or equal to 1000. The total number of pairs is less than or equal to 100, and a word does not appear on the same page more than once.
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict of lists mapping each `word` to a list of `page` numbers where the word appears; if no lines were processed, `index` is empty.
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict of lists mapping each `word` to a list of `page` numbers where the word appears; all words in `index` have been printed in sorted order along with their corresponding sorted lists of page numbers.
    exit()
#Overall this is what the function does:The function reads pairs of words and page numbers from input, storing them in a defaultdict that maps each word to a list of unique page numbers where the word appears. It then prints each word in sorted order followed by the sorted list of associated page numbers. The function does not accept any parameters and does not return a value; it only outputs the results directly to the standard output. It assumes that the input consists of valid pairs of strings and integers, with words not exceeding 30 characters and page numbers being less than or equal to 1000.

