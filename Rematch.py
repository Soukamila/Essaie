def jwenn_karakte_nan_mitan(chenn):
    mots = chenn.split()   

    for mo in mots:
        if 'hidden' in mo or 'endpass' in mo:
            milieu = len(mo) // 2  
            karakte_nan_mitan = mo[milieu]  
            return karakte_nan_mitan 

    return None 


chenn_karakte = input("Entrer yon chaine ki gen hidden ak enpass la danl")
resultat = jwenn_karakte_nan_mitan(chenn_karakte)

if resultat:
    print(f"Karaktè ki nan mitan: {resultat}")
else:
    print("Pa gen karaktè ki nan mitan 'hidden' ak 'endpass' nan chenn sa a.")
