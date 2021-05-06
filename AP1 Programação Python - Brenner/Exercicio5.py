nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7 and media != 10:
   print("Você está aprovado ! Sua média foi ", media)

if media < 7:
   print("Você está reprovado ! Sua média foi ", media)
   
if media == 10:
   print("Aprovado com Distinção ! Sua média foi ", media)