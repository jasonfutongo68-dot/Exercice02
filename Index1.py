print("Bienvenue !")

a = input("Entrez votre prémier nombre: ")
while a == "" :
    print("Veuillez entrer le premier nombre: ")
    a = input("Entre votre premier nombre: ")
b = input("Entrez votre deuxème nombre: ")
while b == "":
    print("veuillez entre votre deuxième nombre: ")
    b = input("Entrez votre deuxième nombre: ")
    
print(f"Le résultat de l'additiion entre {a} et {b} est égal à {int(a) + int(b)}")