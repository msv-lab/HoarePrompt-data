def main():
    T = int(input())
    while T > 0:
        T -= 1
        n = int(input())
        A = []
        B = []
        C = []
        flag = True
        count = [0]*n
        for _ in range(3):
            lst = list(map(int, input().split()))
            if len(A) == 0:
                A = lst
            elif len(B) == 0:
                B = lst
            else:
                C = lst
        for i in range(n):
            temp = set()
            temp.add(abs(A[i]))
            temp.add(abs(B[i]))
            temp.add(abs(C[i]))
            if len(temp) != 2:
                print("NO")
                flag = False
                break
            if abs(A[i]) in temp and abs(B[i]) in temp:
                count[i] += 1
            if abs(A[i]) in temp and abs(C[i]) in temp:
                count[i] += 1
            if abs(B[i]) in temp and abs(C[i]) in temp:
                count[i] += 1
        if flag:
            ans = True
            for i in count:
                if i != 2:
                    ans = False
                    break
            if ans:
                print("YES")
            else:
                print("NO")
main()