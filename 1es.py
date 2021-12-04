relatives=[[15.2,9.4,11.1],
        [9.7,12.2,7.5,10.8],  
        [5.2,6.3,5.6,10.2],   
        [4.9,2,3.5,2.9],
        [1,6.4,4.6,2.1]]
dp={}
def ric(dist,pr):
    dp={}
    if dist>=len(relatives):
        return 0
    maximumGift=0
    if (dist,pr)in dp:
            return dp[(dist,pr)]
    lista=relatives[dist]+[pr]
    for i in lista:
        totalValueAtRow=0
        if i<=pr:
            for j in range(len(relatives[dist])):
                if relatives[dist][j]>=pr:
                    totalValueAtRow+=pr
                elif i<=relatives[dist][j]:
                    totalValueAtRow+=relatives[dist][j]
            val=totalValueAtRow+ric(dist+1,i)
            if val>maximumGift:
                maximumGift=val
    dp[(dist,pr)]=maximumGift
    return maximumGift
if __name__ == "__main__":
    maximumVr=0
    for i in range(len(relatives)):
        for j in range(len(relatives[i])):
            if relatives[i][j]>maximumVr:
                maximumVr=relatives[i][j]
    result=ric(0,maximumVr)
    print(round(result,1))

    
 









def recursive(dist,pr):
    dp={}
    if dist>=len(relatives):
            return 0
    maximumGift=0
    if (dist,pr)in dp:
            return dp[(dist,pr)]
    for i in range(pr+1):
        totalValueAtRow=0
        for j in range(len(relatives[dist])):
            if relatives[dist][j]>=pr:
                totalValueAtRow+=pr
            elif i<=relatives[dist][j]:
                totalValueAtRow+=relatives[dist][j]
        val=totalValueAtRow+recursive(dist+1,i)
        if val>maximumGift:
            maximumGift=val
    dp[(dist,pr)]=maximumGift
    return maximumGift
