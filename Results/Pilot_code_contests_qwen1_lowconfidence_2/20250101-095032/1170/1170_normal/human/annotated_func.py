#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. Each book is represented by a pair of integers ti and wi, where 1 <= ti <= 2 and 1 <= wi <= 100, and these pairs are stored in a list or similar data structure.
def func():
    n = int(raw_input())
    myBooks = []
    W = 0
    for i in range(0, n):
        t, w = map(int, raw_input().split())
        
        W += w
        
        myBooks.append([w, t])
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `myBooks` is a list of lists where each inner list contains the weight `w` and type `t` of a book, `W` is the sum of all weights `w` in `myBooks`.
    myBooks.sort()
    myBooks.reverse()
    T = 0
    for book in myBooks:
        T += book[1]
        
        W -= book[0]
        
        if W <= T:
            break
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer, `myBooks` is a list of lists in reverse order of its original sorted state with possibly some elements removed, `W` is the sum of the weights of the remaining books, and `T` is the sum of the values of the remaining books. If `W <= T` at any point during the loop, the loop will terminate early and these conditions will remain unchanged. Otherwise, after all iterations, `W` will be 0 and `T` will be the sum of the values of all the books in `myBooks`.
    print(T)
#Overall this is what the function does:The function reads a series of book pairs (ti, wi) where ti represents the type of the book and wi represents the weight of the book. It processes these inputs to determine the maximum total value of books that can be selected such that the total weight of selected books does not exceed their total value. It sorts the books in descending order based on their weight and iteratively selects books until the remaining total weight of unselected books is less than or equal to the total value of selected books. The function then prints the total value of the selected books. The function accepts no parameters and returns nothing. Potential edge cases include when the input list is empty or contains only one book. If the list is empty, the function will output 0. If the list contains only one book, the function will output the value of that book if the weight of the book is less than or equal to its value; otherwise, it will output 0.

