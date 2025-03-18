numCases = int(input())
for i in range(numCases):
    numInteger = int(input())
    numbers = input().split()
    numbers.sort(reverse=False)
    suma = 0
    while numbers != []:
        a = int(numbers.pop(0))
        b = int(numbers.pop(0))
        suma += min(a, b)
    print(suma)