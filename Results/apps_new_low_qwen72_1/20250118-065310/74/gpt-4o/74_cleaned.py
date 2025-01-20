def func_1():
    (c, v_0, v_1, a, l) = map(int, input().split())
    days = 0
    pages_read = 0
    current_speed = v_0
    while pages_read < c:
        days += 1
        if days == 1:
            pages_read += v_0
        else:
            pages_read += min(current_speed, v_1) - l
            current_speed += a
        current_speed = min(current_speed, v_1)
        if pages_read < 0:
            pages_read = 0
    print(days)
if __name__ == '__main__':
    func_1()