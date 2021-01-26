# NOT TESTED

n = input('Entrez N : ')
n = int(n)

e = input('Entrez E : ')
e = int(e)

# Cle Publique
print ('La Cle publique :', e, n,)

Message = input("Entrez le nombre a chiffrer : ")
Message = int(Message)



firstmn = pow(Message, e, n)
print ('Premiere iteration :', firstmn)

c = 2
while(True):
    nextit = pow(firstmn, c, n)
    if(firstmn == nextit) :
        print ('Group cyclic en :', c)
        print ('puissance suivante :', nextit)
        break
    c = c + 1


