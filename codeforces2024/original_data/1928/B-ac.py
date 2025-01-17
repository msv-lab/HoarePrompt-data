import sys
import threading

def main():
    import sys
    import bisect

    t = int(sys.stdin.readline())
    for _ in range(t):
        n = int(sys.stdin.readline())
        a = list(map(int, sys.stdin.readline().split()))
        unique_a = set(a)
        events = []
        for val in unique_a:
            start = val +1
            end = val +n
            events.append((start, 1))
            events.append((end +1, -1))
        events.sort()
        current =0
        max_count =0
        for x, typ in events:
            current += typ
            if current > max_count:
                max_count = current
        print(max_count)

threading.Thread(target=main,).start()
