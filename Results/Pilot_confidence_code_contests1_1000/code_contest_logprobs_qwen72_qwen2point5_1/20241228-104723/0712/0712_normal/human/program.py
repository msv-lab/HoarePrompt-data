def main():
    x,y = map(int,raw_input().split())

    n = min(x,y)+1
    print(n)
    for i in range(n):
        print(' '.join([str(i)]*2))

main()