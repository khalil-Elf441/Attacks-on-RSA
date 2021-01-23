def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise ValueError('l inverse modulaire n existe pas.')
    else:
        return x % m


def attack(c1, c2, e1, e2, N):
    if gcd(e1, e2) != 1:
        raise ValueError("exposant) e1 et e2 doivent etre premier")
    s1 = modinv(e1, e2)
    s2 = (gcd(e1, e2) - e1 * s1) / e2
    temp = modinv(c2, N)
    m1 = pow(c1, s1, N)
    m2 = pow(temp, -s2, N)
    return (m1 * m2) % N


def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

if __name__ == '__main__':

    print '### Attaques sur RSA - common modulus attack ### ';

    N = int(raw_input("Entrer le N : "))
    c1 = int(raw_input("Entrer le c1 : "))
    c2 = int(raw_input("Entrer le c2 : "))
    e1 = int(raw_input("Entrer le e1 : "))
    e2 = int(raw_input("Entrer le e2 : "))

    print 'Attaque commencee...'
    try:
        message = attack(c1, c2, e1, e2, N)
        print 'Attaque terminee!'
        print " message: ", message

    except Exception as e:
        print 'L attaque a echoue!'
        print e.message

