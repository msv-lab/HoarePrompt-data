#State of the program right berfore the function call: N is an integer where 1 ≤ N ≤ 1000, and li is a list of N integers where each integer is a natural number not exceeding 1000.
def func():
    input = sys.stdin
    output = sys.stdout
    """
input = open('input.txt','r')
output = open('output.txt','w')
"""
    input.readline()
    woods = map(lambda x: int(x), input.readline().strip().split(' '))
    d = {}
    for w in woods:
        d[w] = d.setdefault(w, 0) + 1
        
    #State of the program after the  for loop has been executed: `N` is an integer where 1 ≤ N ≤ 1000, `li` is a list of N integers where each integer is a natural number not exceeding 1000, `input` is a file object opened in read mode pointing to 'input.txt' with the file pointer advanced to the next line, `output` is a file object opened in write mode pointing to 'output.txt', `woods` is a map object containing integers from the current line of `input`, `d` is a dictionary where each key is an integer from `woods` and the value associated with each key is the count of how many times that integer appears in `woods`. If `woods` is empty, `d` remains an empty dictionary.
    output.write('%d %d' % (max(d.values()), len(d)))
    output.close()
#Overall this is what the function does:The function reads from a file named 'input.txt' and writes to a file named 'output.txt'. It expects the first line of 'input.txt' to contain an integer `N` (1 ≤ N ≤ 1000) indicating the number of integers in the subsequent line. The second line contains `N` space-separated integers, each not exceeding 1000. The function then counts the occurrences of each unique integer and writes two values to 'output.txt': the maximum frequency of any integer and the total number of unique integers. The function does not return any value. Edge cases include handling an empty input file or a file with invalid data formats, which are not explicitly managed by the code.

