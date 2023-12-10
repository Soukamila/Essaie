from random import choice,randrange



def valide_modpas(mot_de_passe):
    
    if len(mot_de_passe) < 7:
        return False


    majuscule = False
    minuscule = False
    chif = False
    caract = False
    caracter = False

    caracterep = ''
    for char in mot_de_passe:
        
        if char.isupper():
            majuscule = True
        elif char.islower():
            minuscule= True
        elif char.isdigit():
            chif = True
        elif char in "!@#$%^&*()-_+=[]{};:,.<>?/|":
            caractere_special_present = True

       
        if char == caracterep:
            caracter = True
            break

        caractere_precedent = char

  
    if majuscule and minuscule and chif and caractere_special_present and not caracter:
        return True
    else:
        return False


mot_de_passe = input("Entrer yon mot passe pou nou verifye")


est_valide = valide_modpas(mot_de_passe)

if est_valide:
    print(f"Le mot de passe '{mot_de_passe}' est valide.")
else:
    print(f"Le mot de passe '{mot_de_passe}' n'est pas valide.")




