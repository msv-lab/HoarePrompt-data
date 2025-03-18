for i in range(int(input())):
      n = [int(i)for i in input().split()][0]
      p = [0]*n;ind = n
      for i in range(0,n,2):p[i]=ind;ind -= 2
      ind = 1 + n%2
      for i in range(1,n,2):p[i]=ind;ind += 2
      print(*p)