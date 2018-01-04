N = int(input("Quanto vc quer depositar?"))

v1 = N
v2 = 0
v5 = 0
v10 = 0
v20 = 0
v50 = 0
v100 = 0

while v1 >= 100:
    v1 -= 100
    v100 += 1

while 50 <= v1 < 100:
    v1 -= 50
    v50 += 1

while 20 <= v1 < 50:
    v1 -= 20
    v20 += 1

while 10 <= v1 < 20:
    v1 -= 10
    v10 += 1

while 5 <= v1 < 10:
    v1 -= 5
    v5 += 1

while 2 <= v1 < 5:
    v1 -= 2
    v2 += 1

print("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n"
      "%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n"
      "%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n"
      "%d nota(s) de R$ 1,00\n" %(N, v100, v50, v20, v10, v5, v2, v1))