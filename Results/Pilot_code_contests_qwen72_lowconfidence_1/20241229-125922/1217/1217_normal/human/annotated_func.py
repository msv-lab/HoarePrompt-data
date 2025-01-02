#State of the program right berfore the function call: a and b are non-negative integers, and at least one of them is not zero.
def func_1(a, b):
    return a if b == 0 else func_1(b, a % b)
    #The program returns the greatest common divisor (GCD) of `a` and `b`. If `b` is 0, it returns `a`. Otherwise, it recursively calls `func_1` with arguments `b` and `a % b` until `b` becomes 0.
#Overall this is what the function does:The function `func_1` accepts two non-negative integer parameters `a` and `b`, where at least one of them is not zero. It returns the greatest common divisor (GCD) of `a` and `b`. If `b` is 0, the function immediately returns `a`. Otherwise, it recursively calls itself with the arguments `b` and `a % b` until `b` becomes 0, at which point it returns the GCD. The function correctly handles the edge case where either `a` or `b` is zero, ensuring that the GCD is returned even if one of the inputs is zero.

#State of the program right berfore the function call: n is a non-negative integer representing a vertex in the tree, and parent is an integer representing the parent vertex of n or -1 if n is the root.
def func_2(n, parent):
    if visited[n] :
        return
        #The program returns nothing (None)
    #State of the program after the if block has been executed: *n is a non-negative integer representing a vertex in the tree, and parent is an integer representing the parent vertex of n or -1 if n is the root. The vertex n has not been visited.
    visited[n] = True
    if (parent != -1) :
        newgcd = func_1(gcdinfo[parent].gcd, a[n])
        gcdinfo[n].gcd = newgcd
        if (newgcd < gcdinfo[parent].gcd) :
            gcdinfo[n].tor1 = a[n]
            gcdinfo[n].ifr1 = gcdinfo[parent].gcd
            if (gcdinfo[parent].ifr1 == 0) :
                gcdinfo[n].tor2 = gcdinfo[parent].gcd
                gcdinfo[n].ifr2 = a[n]
            #State of the program after the if block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`, the current value of `newgcd` is less than `gcdinfo[parent].gcd`, `gcdinfo[n].tor1 = a[n]`, `gcdinfo[n].ifr1 = gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is 0, `gcdinfo[n].ifr2 = a[n]`.
        else :
            if gcdinfo[parent].ifr1 :
                newgcd1 = func_1(gcdinfo[parent].ifr1, a[n])
            else :
                newgcd1 = 1
            #State of the program after the if-else block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`, and `newgcd` is greater than or equal to `gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is true, `newgcd1` is equal to `func_1(gcdinfo[parent].ifr1, a[n])`. Otherwise, `newgcd1 = 1`.
            if gcdinfo[parent].ifr2 :
                newgcd2 = func_1(gcdinfo[parent].ifr2, a[n])
            else :
                newgcd2 = 1
            #State of the program after the if-else block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`, `newgcd` is greater than or equal to `gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is true, `newgcd1` is equal to `func_1(gcdinfo[parent].ifr1, a[n])`. Otherwise, `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2 = func_1(gcdinfo[parent].ifr2, a[n])`. If `gcdinfo[parent].ifr2` is false, `newgcd2 = 1`.
            if (newgcd1 > newgcd2) :
                gcdinfo[n].tor1 = gcdinfo[parent].tor1
                gcdinfo[n].ifr1 = gcdinfo[parent].ifr1
            else :
                if (newgcd2 > newgcd1) :
                    gcdinfo[n].tor1 = gcdinfo[parent].tor2
                    gcdinfo[n].ifr1 = gcdinfo[parent].ifr2
                #State of the program after the if block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`, `newgcd` is greater than or equal to `gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is true, `newgcd1` is equal to `func_1(gcdinfo[parent].ifr1, a[n])`. Otherwise, `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2 = func_1(gcdinfo[parent].ifr2, a[n])`. If `gcdinfo[parent].ifr2` is false, `newgcd2 = 1`. Additionally, `newgcd1` is less than or equal to `newgcd2`. If `newgcd2` is greater than `newgcd1`, `gcdinfo[n].tor1` is equal to `gcdinfo[parent].tor2`, and `gcdinfo[n].ifr1` is equal to `gcdinfo[parent].ifr2`.
            #State of the program after the if-else block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`, `newgcd` is greater than or equal to `gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is true, `newgcd1` is equal to `func_1(gcdinfo[parent].ifr1, a[n])` otherwise `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2 = func_1(gcdinfo[parent].ifr2, a[n])` otherwise `newgcd2 = 1`. If `newgcd1 > newgcd2`, then `gcdinfo[n].tor1 = gcdinfo[parent].tor1` and `gcdinfo[n].ifr1 = gcdinfo[parent].ifr1`. Otherwise, if `newgcd1 <= newgcd2`, then `gcdinfo[n].tor1` is equal to `gcdinfo[parent].tor2` and `gcdinfo[n].ifr1` is equal to `gcdinfo[parent].ifr2`.
        #State of the program after the if-else block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n`, `visited[n] = True`, `parent` is not -1, `newgcd` is equal to `func_1(gcdinfo[parent].gcd, a[n])`, `gcdinfo[n].gcd = newgcd`. If `newgcd < gcdinfo[parent].gcd`, then `gcdinfo[n].tor1 = a[n]` and `gcdinfo[n].ifr1 = gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is 0, `gcdinfo[n].ifr2 = a[n]`. Otherwise, if `newgcd >= gcdinfo[parent].gcd`, then: If `gcdinfo[parent].ifr1` is true, `newgcd1` is equal to `func_1(gcdinfo[parent].ifr1, a[n])` otherwise `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2 = func_1(gcdinfo[parent].ifr2, a[n])` otherwise `newgcd2 = 1`. If `newgcd1 > newgcd2`, then `gcdinfo[n].tor1 = gcdinfo[parent].tor1` and `gcdinfo[n].ifr1 = gcdinfo[parent].ifr1`. Otherwise, if `newgcd1 <= newgcd2`, then `gcdinfo[n].tor1` is equal to `gcdinfo[parent].tor2` and `gcdinfo[n].ifr1` is equal to `gcdinfo[parent].ifr2`.
    #State of the program after the if block has been executed: *`n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n` or -1 if `n` is the root, and `visited[n] = True`. If `parent` is not -1, `newgcd` is set to `func_1(gcdinfo[parent].gcd, a[n])`, and `gcdinfo[n].gcd` is updated to `newgcd`. If `newgcd < gcdinfo[parent].gcd`, then `gcdinfo[n].tor1 = a[n]` and `gcdinfo[n].ifr1 = gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is 0, `gcdinfo[n].ifr2 = a[n]`. Otherwise, if `newgcd >= gcdinfo[parent].gcd`: If `gcdinfo[parent].ifr1` is true, `newgcd1` is set to `func_1(gcdinfo[parent].ifr1, a[n])`; otherwise, `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2` is set to `func_1(gcdinfo[parent].ifr2, a[n])`; otherwise, `newgcd2 = 1`. If `newgcd1 > newgcd2`, then `gcdinfo[n].tor1 = gcdinfo[parent].tor1` and `gcdinfo[n].ifr1 = gcdinfo[parent].ifr1`. If `newgcd1 <= newgcd2`, then `gcdinfo[n].tor1` is set to `gcdinfo[parent].tor2` and `gcdinfo[n].ifr1` is set to `gcdinfo[parent].ifr2`. If `parent` is -1, no changes are made to `gcdinfo[n]` or any other variables.
    for neigh in graph[n]:
        func_2(neigh, n)
        
    #State of the program after the  for loop has been executed: `n` is a non-negative integer representing a vertex in the tree, `parent` is an integer representing the parent vertex of `n` or -1 if `n` is the root, `visited[n] = True`, `graph[n]` contains all the neighbors of `n`, `func_2(neigh, n)` has been called for each neighbor `neigh` of `n`. If `parent` is not -1, `newgcd` is set to `func_1(gcdinfo[parent].gcd, a[n])`, and `gcdinfo[n].gcd` is updated to `newgcd`. If `newgcd < gcdinfo[parent].gcd`, then `gcdinfo[n].tor1 = a[n]` and `gcdinfo[n].ifr1 = gcdinfo[parent].gcd`. If `gcdinfo[parent].ifr1` is 0, `gcdinfo[n].ifr2 = a[n]`. Otherwise, if `newgcd >= gcdinfo[parent].gcd`: If `gcdinfo[parent].ifr1` is true, `newgcd1` is set to `func_1(gcdinfo[parent].ifr1, a[n])`; otherwise, `newgcd1 = 1`. If `gcdinfo[parent].ifr2` is true, `newgcd2` is set to `func_1(gcdinfo[parent].ifr2, a[n])`; otherwise, `newgcd2 = 1`. If `newgcd1 > newgcd2`, then `gcdinfo[n].tor1 = gcdinfo[parent].tor1` and `gcdinfo[n].ifr1 = gcdinfo[parent].ifr1`. If `newgcd1 <= newgcd2`, then `gcdinfo[n].tor1` is set to `gcdinfo[parent].tor2` and `gcdinfo[n].ifr1` is set to `gcdinfo[parent].ifr2`. If `parent` is -1, no changes are made to `gcdinfo[n]` or any other variables.
#Overall this is what the function does:The function `func_2` is designed to traverse a tree structure, starting from a given vertex `n`. It marks the vertex `n` as visited and updates the `gcdinfo` dictionary based on the GCD (Greatest Common Divisor) calculations involving the values stored in `a` and the parent's `gcdinfo`. The function recursively visits all neighbors of the current vertex `n` in the tree. Here are the key points about its functionality:

1.

