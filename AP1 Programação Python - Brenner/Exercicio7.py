numero = int(input("Digite um número que você deseja ver a tabuada: "))
operacao = 0
for i in range(1,11):
   operacao = numero * i
   print(numero, "X", i, "=", operacao)
   