for _ in range(int(input())):
    n = int(input())
    if n == 1 or n%2!= 0:
        print('No')
    else:
         stri = 'AAB'*(n//2)
         print('Yes')
         print(stri)