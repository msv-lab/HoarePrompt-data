c, v0, v1, a, l = map(int, input().split())

days = 0
pages_read = 0
current_speed = v0

while pages_read < c:
    days += 1
    pages_read += current_speed

    if current_speed + a <= v1:
        current_speed += a
    else:
        current_speed = v1

    if pages_read >= c:
        break

    pages_read -= l

print(days)