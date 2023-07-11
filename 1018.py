numeroDeNotas100 = 0
numeroDeNotas50 = 0
numeroDeNotas20 = 0
numeroDeNotas10 = 0
numeroDeNotas5 = 0
numeroDeNotas2 = 0
numeroDeNotas1 = 0

valorDesejado = int(input())
print("%d" % valorDesejado)

while((valorDesejado - (numeroDeNotas100 * 100)) >= 100 ):
    numeroDeNotas100 += 1
    valorDesejado - 100

print("%d nota(s) de R$ 100,00" % numeroDeNotas100)

while(((valorDesejado - (numeroDeNotas100 * 100)) - (numeroDeNotas50 * 50)) >= 50):
    numeroDeNotas50 += 1
    valorDesejado - 50

print("%d nota(s) de R$ 50,00" % numeroDeNotas50)

while(((valorDesejado - (numeroDeNotas100 * 100 + numeroDeNotas50 * 50)) - (numeroDeNotas20 * 20)) >= 20):
    numeroDeNotas20 += 1
    valorDesejado - 20

print("%d nota(s) de R$ 20,00" % numeroDeNotas20)

while(((valorDesejado - (numeroDeNotas100 * 100 + numeroDeNotas50 * 50 + numeroDeNotas20 * 20))- (numeroDeNotas10 * 10)) >= 10):
    numeroDeNotas10 += 1
    valorDesejado - 10
    
print("%d nota(s) de R$ 10,00" % numeroDeNotas10)

while(((valorDesejado - (numeroDeNotas100 * 100 + numeroDeNotas50 * 50 + numeroDeNotas20 * 20)) - (numeroDeNotas5 * 5)) >= 5):
    numeroDeNotas5 += 1
    valorDesejado - 5

print("%d nota(s) de R$ 5,00" % numeroDeNotas5)

while(((valorDesejado - (numeroDeNotas100 * 100 + numeroDeNotas50 * 50 + numeroDeNotas20 * 20 + numeroDeNotas5 * 5)) - (numeroDeNotas2 * 2)) >= 2):
    numeroDeNotas2 += 1
    valorDesejado - 2

print("%d nota(s) de R$ 2,00" % numeroDeNotas2)

while(((valorDesejado - (numeroDeNotas100 * 100 + numeroDeNotas50 * 50 + numeroDeNotas20 * 20 + numeroDeNotas5 * 5 + numeroDeNotas2 * 2)) - (numeroDeNotas1 * 1)) >= 1):
    numeroDeNotas1 += 1
    valorDesejado - 1

print("%d nota(s) de R$ 1,00" % numeroDeNotas1)
