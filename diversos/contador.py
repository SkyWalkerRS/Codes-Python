import sys
import time
import os

def limpar():
  os.system('cls' if os.name == 'nt' else 'clear')
  

milesimos = 0
segundos = 0
minutos = 0

total_min = int(input("Digite os minutos:"))
total_seg = int(input("Digite os segundos:"))


while True:
  limpar()
  print("0",minutos,":",segundos,":",milesimos)
  time.sleep(0.1)
  milesimos += 1
  if milesimos >= 9:
    segundos +=1
    milesimos = 0
  if segundos >= 60:
    minutos += 1
    segundos = 0
  if minutos == total_min: 
	  if segundos >= total_seg:
	    limpar()
	    print("Terminando...")
	    sys.exit()
	

  
  


