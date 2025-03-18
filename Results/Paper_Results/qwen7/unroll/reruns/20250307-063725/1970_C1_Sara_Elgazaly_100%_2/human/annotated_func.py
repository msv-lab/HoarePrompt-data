#State of the program right berfore the function call: n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u and v are integers such that 1 ≤ u, v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n.
def func():
    x, y = map(int, input().split())
    lst = defaultdict(list)
    rev = defaultdict(list)
    for _ in range(x - 1):
        a, b = map(int, input().split())
        
        lst[a].append(b)
        
        rev[b].append(a)
        
    #State: x is an integer, y is an integer, n is an integer such that 2 ≤ n ≤ 2 × 10^5, t is an integer such that t = 1, u is an integer such that 1 ≤ u ≤ n, v is an integer such that 1 ≤ v ≤ n, and the list of integers for the starting node(s) contains exactly one integer u_1 such that 1 ≤ u_1 ≤ n; lst is a defaultdict where each key (integer) maps to a list of integers representing its adjacent nodes, and rev is a defaultdict where each key (integer) maps to a list of integers representing its reverse adjacency nodes based on the edges provided in the loop.
    z = int(input())
    tmp = z
    one = True
    while lst[tmp] != []:
        one = not one
        
        tmp = lst[tmp].pop()
        
    #State: The variable `one` will be flipped to its opposite value, and `tmp` will be set to the last element in the list corresponding to the original `tmp` in the `lst` defaultdict.
    two = True
    tmp = z
    while rev[tmp] != []:
        two = not two
        
        tmp = rev[tmp].pop()
        
    #State: Output State: `one` is flipped to its opposite value, `two` is False, `tmp` is equal to the last element in the list that was originally assigned to `tmp`.
    #
    #Explanation: The loop continues as long as `rev[tmp]` is not empty. Inside the loop, `two` is toggled (flipped) with each iteration, and `tmp` is set to the last element in the list `rev[tmp]`. After all iterations, `two` will be False if it started as True (or True if it started as False), because it is toggled with each iteration. `tmp` will be set to the last element in the list that was originally assigned to `tmp`, as the `pop()` method removes and returns the last element from the list each time the loop runs until the list is empty.
    print('Hermione' if two and one else 'Ron')
    #This is printed: Ron
#Overall this is what the function does:The function reads input values for \(x\), \(y\), and \(z\), constructs a graph represented by two dictionaries (`lst` and `rev`), and then determines whether certain conditions about the graph's structure are met. Specifically, it checks if traversing the graph in one direction results in an alternating pattern (storing odd/even nodes) and if traversing the graph in the reverse direction also results in an alternating pattern. Based on these checks, it prints either "Hermione" or "Ron".

