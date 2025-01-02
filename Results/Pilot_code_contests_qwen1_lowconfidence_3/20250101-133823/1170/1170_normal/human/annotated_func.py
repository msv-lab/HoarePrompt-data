#State of the program right berfore the function call: n is an integer such that 1 <= n <= 100. For each book i (1 <= i <= n), ti is an integer such that ti = 1 or ti = 2, and wi is an integer such that 1 <= wi <= 100.
def func():
    n = int(raw_input())
    myBooks = []
    W = 0
    for i in range(0, n):
        t, w = map(int, raw_input().split())
        
        W += w
        
        myBooks.append([w, t])
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to 100, `myBooks` is a list containing `n` elements, each element is a list `[weight, type]` where `weight` is the sum of weights entered by the user and `type` is the type of book entered by the user, `W` is the sum of all weights entered by the user.
    myBooks.sort()
    myBooks.reverse()
    T = 0
    for book in myBooks:
        T += book[1]
        
        W -= book[0]
        
        if W <= T:
            break
        
    #State of the program after the  for loop has been executed: `n` is an integer within the range 1 to 100, `myBooks` is a reversed sorted list of `[weight, type]` elements, `W` is the sum of all weights minus the sum of the weights of all books in `myBooks`, `T` is the sum of all types of all books in `myBooks`, `book` is the last element in `myBooks` (if the loop executes at least once). If the loop does not execute, `W` remains the original value of `W`, `T` remains the original value of `T`, and `myBooks` remains the original list. If the loop executes at least once and `W` is less than or equal to `T`, we break out of the loop.
    print(T)
#Overall this is what the function does:The function accepts an integer `n` representing the number of books and a series of pairs `(t, w)` where `t` is the type of book (either 1 or 2) and `w` is the weight of the book (an integer between 1 and 100). It constructs a list of books, sorts and reverses this list based on weight, and calculates the sum of the types of the books until the remaining weight (`W`) is no longer sufficient to continue adding types. The function then prints the sum of the types of the books that can be added without violating the condition `W <= T`.

