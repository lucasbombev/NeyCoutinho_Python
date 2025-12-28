"""Corrija o programa a seguir:

média = input("Digite sua média:")
if média < 4:
    print("Infelizmente você reprovou")
if média < 7:
    print("Você ficou de recuperação")
if média > 7:
    print("Você passou de ano")"""

media = float(input("Digite sua média: "))
if media < 4:
    print("Reprovado!")
elif media < 7:
    print("Recuperação!")
else: 
    print("Aprovado! ")
