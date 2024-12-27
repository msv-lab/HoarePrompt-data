
def main():
    n = input()
    a = list(map(int, raw_input().split()))
    #n = 9
    #a = [0 for i in range(9)]
    totalSum = sum(a)
    poss = 0
    theseSums = [sum(a)]
    normalSums = [a[0]]
    for i in range(1,len(a)):
        theseSums.append(theseSums[i-1]-a[i-1])
        normalSums.append(normalSums[i-1]+a[i])
    areTheirSumsGood = [k==totalSum/3 for k in theseSums]
    letsReverse = list(reversed(areTheirSumsGood))
    sumsReverse = [letsReverse[0]]
    for i in range(1,len(a)):
        sumsReverse.append(sumsReverse[i-1]+letsReverse[i])
    sumsUntil = list(reversed(sumsReverse))
    for i in range(len(a)-2):
        if normalSums[i] == totalSum/3:
            #print(i, sumsUntil[i])
            poss += sumsUntil[i+2]
    print(poss)

if __name__ == '__main__':
    main()

    
    

