from fonc import add,multi,divi,exposant,factorielle,sous,racine_carree

#Addition
print("Vous allez faire une addition")
q=int(input("Entrer un nombre"))
v=int(input("Entrer un nombre"))

result=add(q,v)
print ("la somme est :", result)

 #soustraction
print("Vous allez faire une soustraction")
r=int(input("Entrer un nombre"))
a=int(input("Entrer un nombre"))

re=sous(r,a)
print ("le reste est :", re)

#multiplication
print("Vous allez faire une multiplication")
l=int(input("Entrer un nombre"))
z=int(input("Entrer un nombre"))

re=multi(l,z)
print ("le produit  est :", re)

#division
print("Vous allez faire une division")
h=int(input("Entrer un nombre"))
k=int(input("Entrer un nombre"))
re=divi(h,k)
print ("le quotient  est :", re)

#factorielle
print("Vous allez chercher la factorielle d'un nombre")
nombre = int(input("Entrez un nombre entier positif : "))
res = factorielle(nombre)

if res != -1:
    print("La factorielle de", nombre, "est :", res)
else:
    print("La factorielle n'est pas définie pour les nombres négatifs.")

#exposant
print("Vous etes dans la case : exposant")
n = int(input("Entrez un nombre entier: "))
e = int(input("Entrez l'exposant: "))

re=exposant(n,e)
print("le resultat est:",re)


#  racine_carree
print("Vous etes dans la case : racine carre")
nombre = float(input("Entrez un nombre : "))
resultat = racine_carree(nombre)
print("La racine carrée de", nombre, "est  :", resultat)
