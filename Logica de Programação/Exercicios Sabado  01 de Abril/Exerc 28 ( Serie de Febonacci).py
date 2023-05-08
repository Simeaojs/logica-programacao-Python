# Loop While
print()

n = int(input('Quanto Termos quer saber?: '))
t1 = 1
t2 = 1
print(t1,',', t2, end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' , ', t3, end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print()
