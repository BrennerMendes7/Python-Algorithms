def valorPagamento(pres, atra):
   c1 = (3 * pres) / 100
   c2 = (0.1 * atra) / 100
   if atra == 0:
      multa = 0
      juros = 0
   elif atra != 0:
      multa = c1 + pres
      juros = c2 * pres
   
   return multa + juros
 
 
lista = []
prestacao = int(input("Digite o valor da prestação: "))
atraso = int(input("Digite o número de dias em atraso: "))
calculo = valorPagamento(prestacao, atraso)

while prestacao != 0:
    lista.append(calculo)
    prestacao = int(input("Digite o valor da prestação: "))
    atraso = int(input("Digite o número de dias em atraso: "))


qtd_lista = len(lista) 
soma_lista = sum(lista)
print("\n Relatório do Dia:", "\n Quantidade de prestações pagas no dia: ", qtd_lista,
"\n Valor total de prestações pagas no dia: R$", soma_lista)