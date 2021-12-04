#boys
#girls
schools=[
    [5,4,1,5,4,3,1,1,1],
    [5,6,3,2,6,8,3,5,4]
]
k=4
dp={}
def solver(schools,k):
    presiAttualmente=[[0 for i in range(len(schools[0]))] for j in range(2)]
    possocambiare=[0 for i in range(len(schools[0]))]
    sommamaschi=0
    sommafemmine=0
    for i in range(len(schools[0])):
        if schools[0][i]>=k:
            presiAttualmente[0][i]=k
            sommamaschi+=k
        else:
            presiAttualmente[0][i]=schools[0][i]
            presiAttualmente[1][i]=k-schools[0][i]
            sommamaschi+=schools[0][i]
            sommafemmine+=k-schools[0][i]    
        possocambiare[i]=min(schools[1][i]-presiAttualmente[1][i],presiAttualmente[0][i])
    for i in range(len(schools[0])): 
        if sommamaschi<=sommafemmine+1:
            break
        val=min(possocambiare[i],int((sommamaschi-sommafemmine)/2))
        sommamaschi-=val
        sommafemmine+=val
        presiAttualmente[0][i]-=val
        presiAttualmente[1][i]+=val

    return sommamaschi-sommafemmine


def recursive(schoolIndex,boys,girls):
    if schoolIndex>=len(schools[0]):
        return abs(boys-girls)
    if (boys,girls) in dp:
        return dp[(boys,girls)]
    #boys=0,girls=1
    chosen=[0,0]
    biggestGroup=0 if schools[0][schoolIndex]>=schools[1][schoolIndex] else 1
    smallestGroup=1-biggestGroup
    if k>=schools[smallestGroup][schoolIndex]:
        chosen[smallestGroup]=schools[smallestGroup][schoolIndex]
        chosen[biggestGroup]=k-schools[smallestGroup][schoolIndex]
    else:
        chosen[smallestGroup]=k
    localMinimum=10000000
    while(chosen[smallestGroup]>=0 and chosen[biggestGroup]<=schools[biggestGroup][schoolIndex]):
        val=recursive(schoolIndex+1,boys+chosen[0],girls+chosen[1])
        chosen[biggestGroup]+=1
        chosen[smallestGroup]-=1
        if val<localMinimum:
            localMinimum=val
    dp[(boys,girls)]=localMinimum
    return localMinimum





if __name__ == '__main__':
    
    print(solver(schools,k))
    print(recursive(0,0,0))
    
    