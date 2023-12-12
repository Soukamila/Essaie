print("Hello Tout le monde")
chaine = input("Entrer une chaine comme celle ci :<1T >7H >3C <5Y >13J <2C <5W >4A\n")
chaine_upper = chaine.upper()  
mots = chaine_upper.split()
resultat = ""
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for mot in mots:
    if len(mot) == 3:  
        premye = mot[0]
        deux = int(mot[1])
       # print (mot[1])
        trois = mot[2]

        if premye == '>':
            if trois in alpha:  
                trouve = alpha.index(trois)
                new = (trouve + deux) % 26
                lettre = alpha[new]
                resultat += lettre
            else:
                print(f"No trouver '{trois}' .")
        elif premye == '<':
            if trois in alpha:  
                trouve = alpha.index(trois)
                new = (trouve - deux) % 26
                lettre = alpha[new]
                resultat += lettre
            else:
                print(f"La lettre '{trois}' spécifiée dans la séquence n'est pas une lettre majuscule valide.")

    elif len(mot) > 3:  
        premye = mot[0]
        deux = int(mot[1:3])  
        trois = mot[3]

        if premye == '>':
            if trois in alpha:  
                trouve = alpha.index(trois)
                new = (trouve + deux) % 26
                lettre = alpha[new]
                resultat += lettre
            else:
                print(f"No trouver '{trois}' .")
        elif premye == '<':
            if trois in alpha:  
                trouve = alpha.index(trois)
                new = (trouve - deux) % 26
                lettre = alpha[new]
                resultat += lettre
            else:
                print(f"La lettre '{trois}' spécifiée dans la séquence n'est pas une lettre majuscule valide.")

print(resultat)

