#State of the program right berfore the function call: n and m are positive integers such that 1 ≤ n, m ≤ 10000. The log stream consists of strings in the format "2012-MM-DD HH:MM:SS:MESSAGE".**
def func():
    n, m = map(int, raw_input().split())
    log = sys.stdin.readlines()
    logtime = []
    last = 0
    for line in log:
        a = line.find(' ')
        
        year, month, day = map(int, line[:a].split('-'))
        
        b = line.rfind(':')
        
        hour, minute, second = map(int, line[a:b].split(':'))
        
        now = datetime.datetime(year, month, day, hour, minute, second)
        
        logtime.append(now)
        
        print(line[:b], last)
        
        for x in logtime[last:]:
            delta = int((now - x).total_seconds())
            print(delta)
            if delta >= n:
                last += 1
            else:
                break
        
        if len(logtime) - last >= m:
            print(line[:b])
            break
        
    #State of the program after the  for loop has been executed: After all iterations of the loop, `n`, `m`, `logtime`, `last`, `line`, `a`, `b`, `hour`, `minute`, `second`, `now` remain unchanged. If the length of `logtime` minus `last` is greater than or equal to `m`, then the substring of `line` starting from index 0 up to index `b` (excluding `b`) is printed. If that condition is never met, -1 is printed.
#Overall this is what the function does:The function `func` reads input for two positive integers `n` and `m`, and processes a log stream containing timestamped messages. It extracts timestamp information from each log entry and stores it for comparison. The function iterates through the log entries, calculating the time difference between each entry and the current one. If the time difference is greater than or equal to `n`, it increments a counter. If the total number of entries minus the counter is greater than or equal to `m`, the function prints out the timestamp of the current entry. If this condition is never met, the function prints -1.

