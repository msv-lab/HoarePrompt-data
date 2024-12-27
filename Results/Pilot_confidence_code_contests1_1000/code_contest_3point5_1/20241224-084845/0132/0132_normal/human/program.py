y_test = raw_input().split()
kolvo = int(y_test[0])


if kolvo%2 == 0:
    ser = kolvo/2
else:
    ser = (kolvo + 1)/2

k = 0
ii = 0


for i in range(1,ser+1):
    if kolvo%i ==0:
        if i != 1:
            if(max(kolvo/i,i)%min(kolvo/i,i)!= 0):
                flag = 0
                for iii in range(max(kolvo/i,i)+1,ser):
                    if(iii%kolvo == 0 & iii%i ==0):
                        flag = 1
                    else:
                        pass
                if flag ==0 :
                    if max(kolvo/i,i) < max(ii,k):
                        ii= i
                        k = kolvo/i
        else:
            ii = i
            k = kolvo / i
print(ii)
print(k)
