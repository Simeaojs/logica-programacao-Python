

v1=int(input(' valor1:'))
v2=int(input(' valor2:'))
v3=int(input(' valor3:'))

maior=-1
menor=9999999
# achar o maoir
if v1>maior: maior=v1
if v2>maior: maior=v2
if v3>maior: maoir=v3
#achar o menor
if v1<menor: menor=v1
if v2<menor: menor=v2
if v3<menor: menor=v3

medio= (v1+v2+v3)-(maior+menor)

print(menor,medio,maior)
