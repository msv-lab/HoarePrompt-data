#State of the program right berfore the function call: n and q are positive integers where 1 ≤ n, q ≤ 300,000. Each event is represented as a tuple (typei, xi or ti), where typei is an integer (1 ≤ typei ≤ 3) indicating the type of the event, and xi or ti are integers (1 ≤ xi ≤ n, 1 ≤ ti ≤ q) depending on the event type. Initially, there are no notifications.
def func():
    n, q = list(map(int, sys.stdin.readline().strip().split(' ')))
    notifications = []
    unread = [(0) for i in range(n + 1)]
    last_unread = 0
    ans = 0
    for q0 in range(q):
        i, x = list(map(int, sys.stdin.readline().strip().split(' ')))
        
        if i == 1:
            unread[x] += 1
            ans += 1
            notifications.append(x)
        elif i == 2:
            ans -= unread[x]
            unread[x] = 0
        else:
            for j in range(last_unread, x):
                unread[notifications[j]] -= 1
                ans -= 1
            last_unread = x
        
        print(ans)
        
    #State of the program after the  for loop has been executed: `n` and `q` are positive integers where 1 ≤ n, q ≤ 300,000, `notifications` is a list containing the indices `x` for which `i == 1` was encountered, `unread` is a list of length `n + 1` representing the number of unread notifications for each index, `last_unread` is the last value of `x` for which `i == 3` was encountered or 0 if no such operation occurred, `ans` is the final count of unread notifications.
#Overall this is what the function does:The function `func` processes a series of events represented as tuples `(typei, xi or ti)`. It maintains a list of notifications and a count of unread notifications for each index. The function supports three types of events:
1.

