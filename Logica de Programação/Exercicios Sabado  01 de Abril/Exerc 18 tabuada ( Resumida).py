
'''tabuada = int(input('Tabuada do numero?:'))
for cont in range(0, 10):
    print("%dx%d=%d" % (tabuada, cont+1, tabuada*(cont+1)))'''

'''num=int(input("Tabuada do numero?:"))

for n in range(11):
    print(f"{num} x {n} = {num*n}")'''

'''n=int(input("Tabuada de qual numero?:"))
cont=1
while (cont<11):
    tab=n*cont
    print(n1,"x",cont,"=",tab)
    cont += 1'''
       
while True:
    num = int(input(' Qual tabuada quer saber?: '))   
    if num < 0: break
    for c in range (1,11):
        print(f'{num} x {c}= {num*c}')    
