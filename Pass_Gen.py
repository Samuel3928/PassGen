BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
#
import random, os, webbrowser
import time

def borrarpant():
    if os.name == "nt":
        os.system ("clear")
    else:
        os.system ("clear")

#Banner

borrarpant()
print(RED+":) INICIANDO PROGRAMA..."+RESET)
time.sleep(2)
print("")
print(GREEN+";) INICIADO CORRECTAMENTE"+RESET)
time.sleep(1)
borrarpant()
time.sleep(2)
print(BLUE+"")
print("                                                                          ")
print("       ██▓███   ▄▄▄        ██████   ██████   ▄████ ▓█████  ███▄    █      ")
print("      ▓██░  ██▒▒████▄    ▒██    ▒ ▒██    ▒  ██▒ ▀█▒▓█   ▀  ██ ▀█   █      ")
print("      ▓██░ ██▓▒▒██  ▀█▄  ░ ▓██▄   ░ ▓██▄   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒     ")
print("      ▒██▄█▓▒ ▒░██▄▄▄▄██   ▒   ██▒  ▒   ██▒░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒     ")
print("      ▒██▒ ░  ░ ▓█   ▓██▒▒██████▒▒▒██████▒▒░▒▓███▀▒░▒████▒▒██░   ▓██░     ")
print("      ▒▓▒░ ░  ░ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░ ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒      ")
print("      ░▒ ░       ▒   ▒▒ ░░ ░▒  ░ ░░ ░▒  ░ ░  ░   ░  ░ ░  ░░ ░░   ░ ▒░     ")
print("      ░░         ░   ▒   ░  ░  ░  ░  ░  ░  ░ ░   ░    ░      ░   ░ ░      ")
print("                     ░  ░      ░        ░        ░    ░  ░         ░      "+RESET)
print(RED+"                            PassGen(v.1.0)"+RESET) 
print (MAGENTA+"         ------------- by ꧁༺MR-X༻꧂ ------------- "+RESET)
print (GREEN+"                   Para Salir Presiona Ctrl+c"+RESET)
print (" ")



length=int(input (YELLOW+"> Longitud de la Password: "+RESET))

print ("")
time.sleep(2)

print (CYAN+"      LISTO, VUELTA HECHA! "+RESET)
print (" ")
time.sleep(1)

char="abcdefghijklmnopqrstuvwxyz1234567890@#$%~&*^"

password= (RED+"║Password:║ "+RESET)
print(RED+"╔═════════════╗"+RESET)

for i in range(length):

     password+=random.choice(char)


print(password)
print(RED+"╚═════════════╝"+RESET)

print ("")
quit()


