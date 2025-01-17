n = int(input())
ticket = input()
erased = [i for i in range(n) if ticket[i] == '?']
happy = sum(int(ticket[i]) for i in range(n) if ticket[i] != '?' and i < n // 2) == sum(int(ticket[i]) for i in range(n) if ticket[i] != '?' and i >= n // 2)

if happy:
    print("Bicarp")
else:
    if len(erased) % 4 == 0:
        print("Bicarp")
    else:
        print("Monocarp")
