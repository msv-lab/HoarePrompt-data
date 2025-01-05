def main():
    n=int(input())
    for i in range(1,(2*n)+1):
        for j in range(1,(2*n)+1):
            if (i%4==0 or i%4==3):
                if(j%4==0 or j%4==3):print('#',end='')
                else:print('.',end='')
            else:
                if(j%4==0 or j%4==3):print('.',end='')
                else:print('#',end='')
        print()

t=int(input())
for i in range(t):
    main()
