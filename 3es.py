


# if maschi[indice]<=femmine[indice]:
    #     if k>=maschi[indice]:
    #         inizio[0]=maschi[indice]
    #         inizio[1]=k-maschi[indice]
    #     else:
    #         inizio[0]=k
    # else:
    #     if k>=femmine[indice]:
    #         inizio[1]=femmine[indice]
    #         inizio[0]=k-femmine[indice]
    #     else:
    #         inizio[1]=k





























# maschi=[2,2,4]
# femmine=[4,5,2]
m=[
    [2,2,1],
    [4,2,4]
]
k=3
d={}
def ric(indice,maschiattuali,femmineattuali):
    if indice>=len(m[0]):
        return abs(maschiattuali-femmineattuali)
    if (maschiattuali,femmineattuali) in d:
        return d[(maschiattuali,femmineattuali)]
    #maschi=0,femmine=1
    inizio=[0,0]
    grande=0 if m[0][indice]>=m[1][indice] else 1
    piccolo=1-grande
    
    if k>=m[piccolo][indice]:
        inizio[piccolo]=m[piccolo][indice]
        inizio[grande]=k-m[piccolo][indice]
    else:
        inizio[piccolo]=k
    minimoLocale=10000000

    while(inizio[piccolo]>0 and inizio[grande]<m[grande][indice]):
        inizio[grande]+=1
        inizio[piccolo]-=1
        val=ric(indice+1,maschiattuali+inizio[0],femmineattuali+inizio[1])
        if val<minimoLocale:
            minimoLocale=val
    d[(maschiattuali,femmineattuali)]=minimoLocale
    return minimoLocale

if __name__ == '__main__':
    print(ric(0,0,0))