# Zahlenraten

import random
zufallszahl = (random.randint(1,100))
titel = "Willkommen beim Zahlen-Rate-Spiel!"
text = "Bitte versuche meine Zahl zwischen 1 und 100 zu erraten"
eingabeText = "Bitte gib eine Zahl ein: "

print (titel)
print (text)
fertig = False
anzahlDerVersuche = 0
while fertig == False:
    zahl = int(input(eingabeText))
    anzahlDerVersuche = anzahlDerVersuche + 1
    
    if (zahl == zufallszahl):
        print("gewonnen!")
        fertig = True
    elif(zahl < zufallszahl):
        print("die gesuchte Zahl ist größer")
        
    else:
       print("die gesuchte Zahl ist kleiner")
       
print("super, du hast dafür nur ", anzahlDerVersuche, "Versuche benötigt")
print("ende")

