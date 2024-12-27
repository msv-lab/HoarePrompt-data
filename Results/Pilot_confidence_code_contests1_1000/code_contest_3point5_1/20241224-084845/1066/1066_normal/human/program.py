n,k,a,b=map(int,raw_input().split())#attendu:12
def f(pos,amp,debut,fins):
    global a,b
    #print(pos,amp,debut,fins)
    if debut==fins:
        return a
    if amp==1:
        return b*(fins-debut)
    else:
        borne=pos+amp//2
        deb=debut-1#à l'issue de la dicho, deb doit indiquer le dernier avanger de la première moitié ou avant,j'ai galéré pourc omprendre qu'il fallaaitmettre début-1
        fin=fins
        while fin-deb>1:
            m=(fin+deb)//2
            if antman[m]>=borne:
                fin=m
            else:
                deb=m
            #if amp==4:
                #print(m,antman[m],borne,deb,fin)
        r=min(f(pos,amp//2,debut,fin)+f(borne,amp//2,fin,fins),b*amp*(fins-debut))
        #print(r,pos,amp,debut,fins,deb,fin)
        return r
antman=sorted(map(int,raw_input().split()))
print(f(1,2**n,0,k))#pointeur au début et pointeur en dehors
