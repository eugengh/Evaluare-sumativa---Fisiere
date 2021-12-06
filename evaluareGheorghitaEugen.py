with open('c:/Users/user/Desktop/INPUT.txt', 'rt')as f: 
    linii=list(f) 
print('NR. Nume   Prenume nota1 nota2 nota3  ') 
with open("INPUT.txt", "r")as g:
    lista = g.readlines()
for i in lista:
    print(i)
with open("Rezerva.txt", "w") as e:
    for i in lista:
        e.write(i)
with open("Output.txt", "w") as f:
    f.write('NR. '+'Nume   '+'Prenume '+'Media'+'\n')
for i in linii:
    nota=i.split()
    x=nota[0]+' '+nota[1]+' '+nota[2]
    media=str((float(nota[3])+float(nota[4])+float(nota[5]))/3)
    y=x+' '+media+'\n'
    with open('OUTPUT.txt','a') as f:
        f.write(y)
with open('OUTPUT.txt','r') as f:
    list3=f.readlines()

