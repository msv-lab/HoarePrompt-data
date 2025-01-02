#State of the program right berfore the function call: n is a positive integer (1 ≤ n ≤ 10^5), and a is a list of n integers where each element a_i satisfies 0 ≤ a_i ≤ 3.
def func():
    rints = lambda : [int(x) for x in stdin.readline().split()]
    out = []
    n, a = int(input()), rints()
    mem, cols, rows = defaultdict(deque), n, n
    mem2 = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        if a[i] == 1:
            out.append('%d %d' % (rows, i + 1))
            if rows < 1:
                print(-1)
                exit()
            rows -= 1
            mem[1].append([rows + 1, i + 1])
        elif a[i] == 2:
            if mem[1]:
                out.append('%d %d' % (mem[1][0][0], i + 1))
            else:
                print(-1)
                exit()
            mem[1].popleft()
            mem[2].append(i + 1)
        elif a[i] == 3:
            if mem[3]:
                out.append('%d %d' % (rows, i + 1))
                out.append('%d %d' % (rows, mem[3][0]))
                if rows < 1:
                    print(-1)
                    exit()
                rows -= 1
                mem[3].popleft()
            elif mem[2]:
                out.append('%d %d' % (rows, i + 1))
                out.append('%d %d' % (rows, mem[2][0]))
                if rows < 1:
                    print(-1)
                    exit()
                rows -= 1
                mem[2].popleft()
            elif mem[1]:
                out.append('%d %d' % (rows, i + 1))
                out.append('%d %d' % (rows, mem[1][0][1]))
                if rows < 1:
                    print(-1)
                    exit()
                rows -= 1
                mem[1].popleft()
            else:
                print(-1)
                exit()
            mem[3].append(i + 1)
        
    #State of the program after the  for loop has been executed: `n` is the input integer, `a` is a list of `n` integers where each element `a_i` satisfies 0 ≤ `a_i` ≤ 3, `out` is a list of strings generated during the loop, `mem` is a `defaultdict` of `deque` objects containing elements added during the loop, `rows` is `n - k` where `k` is the number of times `rows` is decremented, `mem2` is a list of `n + 1` zeros.
    print('%d\n%s' % (len(out), '\n'.join(out)))
#Overall this is what the function does:The function `func` processes a positive integer `n` and a list `a` of `n` integers, where each element of `a` is between 0 and 3. It generates a series of operations based on the values in `a` and prints the results. Specifically, it handles three types of operations (1, 2, and 3) and maintains a list of output strings (`out`). For each element in `a`:
- If the element is 1, it appends a string indicating a row assignment and decrements the available rows.
- If the element is 2, it reuses a previously assigned row if available; otherwise, it prints `-1` and exits.
- If the element is 3, it attempts to assign two rows, reusing previously assigned rows if necessary; otherwise, it prints `-1` and exits.
The function ensures that the number of rows does not go below zero. After processing all elements in `a`, it prints the total number of operations and the list of operations. If at any point the function cannot perform the required operation, it prints `-1` and exits.

