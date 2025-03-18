for _ in range(int(input())):
    n = int(input())
    ar = map(str , sorted(list(map(int,input().split()))))
    print(" ".join(ar))