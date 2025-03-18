#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, representing the number of nodes in the tree. The tree is represented by n-1 edges, each connecting two nodes u and v where 1 ≤ u, v ≤ n. The tree has exactly two leaves. The initial node for the game is an integer u_1 where 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: After all iterations of the loop, `x` is 1, `lst` contains all the appended values of `b` corresponding to each `a` from the inputs, and `rev` contains all the appended values of `a` corresponding to each `b` from the inputs. The other variables (`n`, `u_1`, `y`) remain unchanged.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: After all iterations of the loop, `x` is 1, `lst` contains all the appended values of `b` corresponding to each `a` from the inputs, but the lists within `lst` that were accessed and modified during the loop are now empty. `rev` contains all the appended values of `a` corresponding to each `b` from the inputs, `n`, `u_1`, `y` remain unchanged, `z` is an input integer, `tmp` is the last element that was removed from the list it was accessing when the loop terminated, and `one` is False if the total number of iterations is odd, or True if the total number of iterations is even.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: After all iterations of the loop, `x` is 1, `lst` contains all the appended values of `b` corresponding to each `a` from the inputs, but the lists within `lst` that were accessed and modified during the loop are now empty, `rev` contains all the appended values of `a` corresponding to each `b` from the inputs except the elements that were popped during the loop, `n`, `u_1`, `y` remain unchanged, `z` is an input integer, `tmp` is the last element of `rev[z]` before the final pop operation, `one` is False if the total number of iterations is odd, or True if the total number of iterations is even, `two` is True if the total number of iterations is even, or False if the total number of iterations is odd, and `rev[z]` and any other lists within `rev` that were accessed are now empty.
    print('Hermione' if two and one else 'Ron')
    #This is printed: 'Hermione' if the total number of iterations is even, or 'Ron' if the total number of iterations is odd
#Overall this is what the function does:The function reads a series of inputs to construct a tree with `n` nodes and `n-1` edges. It then determines the winner of a game played on this tree, starting from a specified node `u_1`. The game alternates between two players, Hermione and Ron, moving along the edges of the tree. The function prints 'Hermione' if the total number of moves made by both players is even, and 'Ron' if the total number of moves is odd. The function does not return any value; it only prints the result.

