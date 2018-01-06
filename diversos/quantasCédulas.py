def contaCedulas():
	n = int(input("\nQuanto vc quer depositar?"))

	n1 = n
	n2 = 0
	n5 = 0
	n10 = 0
	n20 = 0
	n50 = 0
	n100 = 0

	while n1 >= 100:
	    n1 -= 100
	    n100 += 1

	while 50 <= n1 < 100:
	    n1 -= 50
	    n50 += 1

	while 20 <= n1 < 50:
	    n1 -= 20
	    n20 += 1

	while 10 <= n1 < 20:
	    n1 -= 10
	    n10 += 1

	while 5 <= n1 < 10:
	    n1 -= 5
	    n5 += 1

	while 2 <= n1 < 5:
	    n1 -= 2
	    n2 += 1

	print("%d\n%d nota(s) de R$ 100,00\n%d nota(s) de R$ 50,00\n"
	      "%d nota(s) de R$ 20,00\n%d nota(s) de R$ 10,00\n"
	      "%d nota(s) de R$ 5,00\n%d nota(s) de R$ 2,00\n"
	      "%d nota(s) de R$ 1,00\n" %(n, n100, n50, n20, n10, n5, n2, n1))
contaCedulas()
while True:	
	again = input("Digite [S] para depositar mais algum valor: ")
	if again == "s" or again == "S":
		contaCedulas()
	else:
		break	
		