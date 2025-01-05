#State of the program right berfore the function call: The input consists of a list of pairs where each pair is a string (word with at most 30 characters) and an integer (page number less than or equal to 1000), with the total number of pairs not exceeding 100. Each word appears at most once per page.
def func_1():
    index = defaultdict(list)
    for line in stdin:
        word, page = line.split()
        
        index[word].append(int(page))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict of lists containing words as keys and lists of corresponding page numbers as values; `word` is the last word processed from stdin, `page` is the corresponding last page processed from stdin.
    for word in sorted(index):
        print(word)
        
        print(*sorted(index[word]))
        
    #State of the program after the  for loop has been executed: `index` is a defaultdict of lists containing all words as keys in sorted order; `word` is the last word in the sorted order of the keys; `page` is the corresponding page number for `word`; each `word` is printed followed by the sorted list of values from `index[word]`.
    exit()
#Overall this is what the function does:The function reads pairs of words and page numbers from standard input, where each word is associated with a list of page numbers. It stores these pairs in a dictionary with words as keys and lists of integers (page numbers) as values. After processing the input, it prints each word in alphabetical order followed by the sorted list of corresponding page numbers. The function does not take any parameters nor does it return any value; it directly prints the results to the standard output.

