import string
alphbet = string.ascii_lowercase
for i in range(int(input())):
    number = int(input())
    if number > 26 :
        a = number % 26
        b = number - a
        c = b - 26
        b -= c
        if c == 0:
            c += 1
            a -= 1
            print(alphbet[c-1]+alphbet[a-1]+alphbet[b-1])
            break
    else:
        a = 1
        b = 1
        c = number - 2

    print(alphbet[a-1]+alphbet[b-1]+alphbet[c-1])