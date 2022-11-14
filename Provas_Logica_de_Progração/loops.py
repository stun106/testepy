'''[PT-A02] Faça um código que receba dois números (inteiros, positivos e diferentes entre si ) e imprima na tela todos os números "primos" que existem entre eles.'''

primos:list = list()
while True:
    try:
        entry1:int = int(input('informe um numero: '))
        entry2:int = int(input('informe outro numero: '))

        if entry1 < entry2:
            for a in range(entry1,entry2+1):
                pass
                if a > 1:
                    for b in range(2,a):
                        if a % b == 0:
                            break
                    else: 
                        primos.append(a)
            print(primos)
            primos.clear()
        else:
            for d in range(entry2,entry1):
                pass
                if d > 1:
                    for e in range(2,d):
                        if d % e == 0:
                            break
                    else:
                        primos.append(d)
            print(primos)
            primos.clear()
    except:
        print('Algo deu errado, verifique seus dados!')
            

        

