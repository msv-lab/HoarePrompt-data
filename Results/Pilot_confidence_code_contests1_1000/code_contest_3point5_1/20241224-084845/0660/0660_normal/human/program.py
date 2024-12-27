def ebne(n):
    if n % 2 == 0:
        return False
    if sum([int(i) for i in str(n)]) % 2 == 0:
        return True
    else:
        return False

def ebnifier(n):
    if all(int(i) % 2 == 0 for i in str(n)):
        return -1
    if ebne(n):
        return n
    else:
        if n % 2 == 0:
            for i in range(len(str(n))-1, -1, -1):
                if int(str(n)[i]) % 2 == 0:
                    n = int(str(n)[0:len(str(n)) - 1])
                else:
                    break
        else:
            for i in range(1, 10, 2):
                if str(i) in str(n):
                    n = int(str(n).replace(str(i), "", 1))
                    break
        return ebnifier(n)

num = int(input("n of test"))
ebnes = []
for i in range(num):
    dig = input("digits")
    n = input("number")
    ebnes.append(int(n))
for i in ebnes:
    print(ebnifier(i))
