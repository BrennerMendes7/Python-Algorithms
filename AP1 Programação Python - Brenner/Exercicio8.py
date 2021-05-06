def maiores_valores(lista2):

     soma = 0

     for numero in lista2:
          soma += numero

     media2 = soma / len(lista2)

     maiores=[]

     for i in lista2:
          if i > media2:
               maiores.append(i)

     return len(maiores)
     
def menores_valores_sete(lista3):

     maiores2=[]

     for i in lista3:
          if i < 7:
               maiores2.append(i)

     return len(maiores2)
     
lista = []
valor = int(input("Digite um número: "))

while valor != -1:
   lista.append(valor)
   valor = int(input("Digite um número: "))
   
print("Tamanho da lista: ", len(lista), "números")

print(*lista, sep = ", ")

lista_reversa = lista[::-1]
print(*lista_reversa, sep = "\n")

soma_lista = sum(lista)
print("A soma dos valores da lista: ", soma_lista)

tamanho = len(lista)
media = soma_lista / tamanho
print("A média dos valores da lista: ", media)

print("Quantidade de valores maiores que a média: ", maiores_valores(lista))

print("Quantidade de valores menores que 7: ", menores_valores_sete(lista))

print("Eu tenho o melhor de professor de Python do mundo :) :) :)")



