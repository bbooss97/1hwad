

#boys
#girls
schools=[
    [20,20,10,50],
    [40,20,50,34]
]
k=40
dp={}
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
    result=recursive(0,0,0)
    print(result)
    