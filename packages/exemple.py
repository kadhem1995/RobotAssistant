
import os 
def choix():
	print("1:Arabe")
	print("2:Anglais")
	print("3:Francais")
	langue=input("choisissez la langue")

	if(langue=='1'):
		print("ar")
		os.system('cd /home/hiba/Desktop/file/')
		os.system('python3 arab.py')
	elif(langue=='2'):
		print("An")
		os.system('cd /home/hiba/Desktop/file/')
		os.system('python3 maiin.py')
	elif(langue=='3'):
		print("Fr")
	else: 
		print("Erreur")

while(True):
	choix()
