def func_1(h, m):
    """Check if the time h:m contains a '7'."""
    return '7' in str(h) or '7' in str(m)

def func_2():
    x = int(input())
    (hh, mm) = map(int, input().split())
    snooze_count = 0
    while not func_1(hh, mm):
        snooze_count += 1
        mm -= x
        if mm < 0:
            mm += 60
            hh -= 1
            if hh < 0:
                hh += 24
    print(snooze_count)
if __name__ == '__main__':
    func_2()