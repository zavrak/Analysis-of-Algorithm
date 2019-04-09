def fibo_rec(n):
    if(n<2):
        return n
    else:
        return(fibo_rec(n-1)+fibo_rec(n-2))
//1
dizi=[50,25,10,5,1]
kullanılan=[]
kalan =180
i=0
while(dizi[i]<=kalan and kalan!=0):
    kalan = kalan - dizi[i]
    kullanılan.append(dizi[i])
    if(kalan<dizi[i]):
        i =  i + 1
print(kullanılan)
//2

def recMC(coinValueList,change,knownResults):
    minCoins = change
    if(change in coinValueList):
        knownResults[change] = 1
        return 1
    else:
        for i in[c for c in coinValueList if c<= change]:
            numCoins = 1 +recMC(coinValueList,change-1,knownResults)
            if(numCoins<minCoins):
                minCoins = numCoins
                knownResults[change] = minCoins
        return minCoins
for i in range(8,200):
    print(i," ",recMC([1,5,10,25,50],i,[0]*(i+1)))
    //3
