
def Goldbach(primos:list,resultado:int):
    for x in range(2,resultado+1):
        for i in range(2,x):
            if x % i==0:
                break 
        else: 
            primos.append(x)
    #print(primos)


    for x in range(len(primos)):
        for i in range(len(primos)-1,0, -1):
            if primos[x] + primos[i] == resultado:  
                return(f'O primo {primos[x]} + {primos[i]} e igual a {resultado}')
        


pri = []
res = 20
print(Goldbach(pri,res))
