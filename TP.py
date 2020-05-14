import random
import sys

nombre = random.randint(0, 10)
essais = 0
#print (nombre)

for essais in range(3):
	print ("Veuillez saisir un nombre :")
	saisie = int(input())
	if saisie == nombre:
		print ("Bonne réponse !")
		sys.exit(0)
	if saisie != nombre:
		if essais == 2: # 3 essais, dc 2 !
			print ("Game Over !")
			print ("le nombre était : " + str(nombre))
		else:
			print ("Mauvaise réponse ! Rejouer (y/n) ?")
			rejouer = input()
			if rejouer == "y":
				essais = essais + 1
			else:
				print ("Bye Bye !")
				sys.exit(0)
