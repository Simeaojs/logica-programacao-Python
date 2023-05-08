

a=int(input(' numero 1: '))
b=int(input(' numero 2: '))
c=int(input(' numero 3: '))
menor = a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior =a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior= c

print(' o menor valor é',menor)
print(' o maior valor é ',maior)
