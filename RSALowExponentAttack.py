
def mod_inverse(x,m):
    for n in range(m):
        if (x * n) % m == 1:
            return n
            break

        elif n == m - 1:
            return 0
        else:
            continue

def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':

    print "### Attaques sur RSA - low-exponent attack ###"

    #combien de message crypte vous avez
    #print " combien de message crypte vous avez ?"
    #nbc = int(raw_input("nbc : "))

    e = int(raw_input("Entrer le e : "))
    lesN = []
    lesC = []

    leMessage = int(raw_input("le message : "))


    for i in range(e):
        N = int(raw_input("Entrer N"+str(i)+" : "))
        lesN.append(N)

    for j in range(e):
        if (j + 1 < e):
            if (pgcd(lesN[j], lesN[j + 1]) != 1):
                raise ValueError('Les nombres ne sont pas premiers entre eux !')

    for i in range(e):
        #C = int(raw_input("Entrer C N" + str(i) + " (message crypte pour N" + str(i) + "): "))
        C = pow(leMessage,e,lesN[i])
        lesC.append(C)



    #Theoreme des restes chinois
    # X = (a1M1y1 + ... + anMnyn) mod M
    # Mi = M/mi
    # yi = Mi^(-1) mod mi

    M = 1
    for c in range(e):
        M = M*lesN[c]




    G_N = 1
    for j in range(e):
       print " x = "+str(lesC[j])+" mod "+str(lesN[j])
       G_N = G_N * lesN[j]


    X = 0
    for j in range(e):
        Mi = M/lesN[j]
        #yi = ( Mi ** (-1) ) % lesN[j]
        yi = mod_inverse(Mi,lesN[j])
        ai = lesC[j]
        print "ai = "+str(ai)+" Mi = "+str(Mi)+" yi = "+str(yi)
        X = X + (ai*Mi*yi)

    X = X % (G_N)
    print " l'equation : X = "+str(X)

    racine = 1.0 / e
    Mss = pow(X, racine)
    print " M = " + str(X)+" racine de "+str(racine)
    print " M = " + str(Mss)