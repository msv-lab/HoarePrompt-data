#State of the program right berfore the function call: n is an integer such that 1 ≤ n ≤ 100. Each of the next n lines contains two integers ti and wi, where 1 ≤ ti ≤ 2 and 1 ≤ wi ≤ 100, representing the thickness and width of the i-th book, respectively.
def func():
    n = int(raw_input())
    myBooks = []
    W = 0
    for i in range(0, n):
        t, w = map(int, raw_input().split())
        
        W += w
        
        myBooks.append([w, t])
        
    #State of the program after the  for loop has been executed: `n` is an integer such that \(1 \leq n \leq 100\), `i` is equal to `n`, `W` is the sum of all integers `w` entered, `myBooks` is a list containing pairs `[w, t]` where each pair corresponds to the integer `w` and its corresponding integer `t` entered for each iteration of the loop.
    myBooks.sort()
    myBooks.reverse()
    T = 0
    for book in myBooks:
        T += book[1]
        
        W -= book[0]
        
        if W <= T:
            break
        
    #State of the program after the  for loop has been executed: `T` is the sum of `t` values from the remaining books in `myBooks`, `W` is the sum of `w` values from the remaining books in `myBooks`, and `myBooks` remains unchanged or truncated based on the loop condition.
    print(T)
#Overall this is what the function does:The function processes a list of books, where each book is represented by a tuple containing its thickness and width. It sorts the books in descending order based on their width, calculates the total thickness (`T`) of the books that can be placed on a shelf without exceeding the total width (`W`). The function then prints the total thickness of the selected books. The function does not return any value. Potential edge cases include when all books cannot fit on the shelf due to their combined thickness exceeding their combined width, and the function stops adding books once this condition is met.

