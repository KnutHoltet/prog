import random 

dorer = ["geit", "bil", "geit"]
random.shuffle(dorer)

#spiller velger dør
#tar input
dor = int(input("Skriv et tall fra 1 - 3: "))
valg1 = dor - 1
#velg en av dørene
print(f"Du har valgt dør nummer {dor}")

if dorer[valg1] == dorer[0]:
  svar = input("Vil du velge en annen dør? [y/n]: ")
  if svar == "n":
    print(f"Du fikk på denne døren {dorer[valg1]}")
  else:
    valg2 = int(input("Skriv inn den andre døren: "))
    if dorer[valg2] == dorer[1]: # Dette er for dør 2
      print(f"Du fikk på denne døren: {dorer[valg2]}")
    else:
      print(f"Du fikk på denne døren: {dører[valg2]}")# Dette er for dør 3
elif dorer[valg1] == dorer[1]:
  svar = input("Vil du velge en annen dør? [y/n]: ")
  if svar == "n":
    print(f"Du fikk på denne døren {dorer[valg1]}")
  else:
    valg2 = int(input("Skriv inn den andre døren: "))
    if dorer[valg2] == dorer[1]: # Dette er for dør 2
      print(f"Du fikk på denne døren: {dorer[valg2]}")
    else:
      print(f"Du fikk på denne døren: {dører[valg2]}")# Dette er for dør 3
else:
  svar = input("Vil du velge en annen dør? [y/n]: ")
  if svar == "n":
    print(f"Du fikk på denne døren {dorer[valg1]}")
  else:
    valg2 = int(input("Skriv inn den andre døren: "))
    if dorer[valg2] == dorer[1]: # Dette er for dør 2
      print(f"Du fikk på denne døren: {dorer[valg2]}")
    else:
      print(f"Du fikk på denne døren: {dører[valg2]}")# Dette er for dør 3


