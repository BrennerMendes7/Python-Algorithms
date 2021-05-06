def mostrar_informacoes(p1, p2, p3, p4):
    print("Seu salário antigo: R$", p1)
    print("Percentual de aumento aplicado: ", p2, "%")
    print("O valor do aumento: R$", p3)
    print("Seu novo salário: R$", p4)
    
salario_antigo = float(input("Digite o seu salário: "))
salario_novo = 0
percentual = 0
aumento = 0

if salario_antigo < 280:
   percentual = 20
   aumento = salario_antigo * 0.2
   salario_novo = aumento + salario_antigo
   mostrar_informacoes(salario_antigo, percentual, aumento, salario_novo)
   
if salario_antigo >= 280 and salario_antigo < 700:
   percentual = 15
   aumento = salario_antigo * 0.15
   salario_novo = aumento + salario_antigo
   mostrar_informacoes(salario_antigo, percentual, aumento, salario_novo)
   
if salario_antigo >= 700 and salario_antigo < 1500:
   percentual = 10
   aumento = salario_antigo * 0.1
   salario_novo = aumento + salario_antigo
   mostrar_informacoes(salario_antigo, percentual, aumento, salario_novo)
   
if salario_antigo >= 1500:
   percentual = 5
   aumento = salario_antigo * 0.05
   salario_novo = aumento + salario_antigo
   mostrar_informacoes(salario_antigo, percentual, aumento, salario_novo)