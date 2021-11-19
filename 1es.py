gruppo=[[15.2,9.4,11.1],
        [9.7,12.2,7.5,10.8],  
        [5.2,6.3,5.6,10.2],   
        [4.9,2,3.5,2.9],
        [1,6.4,4.6,2.1]]
#ris=116.3




d={}
decimali=1

def ric(indicegruppo,massimo):
    if indicegruppo>=len(gruppo):
            return 0
    massimoLocale=0
    for i in range(massimo+1):
        regaliTotaliParenti=0
        if (indicegruppo,i,massimo)in d:
            if d[(indicegruppo,i,massimo)]>massimoLocale:
                massimoLocale=d[(indicegruppo,i,massimo)]
            continue
        for j in range(len(gruppo[indicegruppo])):
            if gruppo[indicegruppo][j]>=massimo:
                regaliTotaliParenti+=massimo
            elif i<=gruppo[indicegruppo][j]:
                regaliTotaliParenti+=gruppo[indicegruppo][j]
        val=regaliTotaliParenti+ric(indicegruppo+1,i)
        d[(indicegruppo,i,massimo)]=val
        if val>massimoLocale:
            massimoLocale=val
    return massimoLocale


if __name__ == "__main__":
    for i in range(len(gruppo)):
        for j in range(len(gruppo[i])):
            gruppo[i][j]=int(gruppo[i][j]*(10*decimali))
    massimo=0
    for i in range(len(gruppo)):
        for j in range(len(gruppo[i])):
            if gruppo[i][j]>massimo:
                massimo=gruppo[i][j]
    risultato=ric(0,massimo)/(10*decimali)
    #print(d)
    
    print(risultato)
 
