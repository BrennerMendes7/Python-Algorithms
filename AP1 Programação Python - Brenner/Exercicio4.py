valor_hora = float(input("Quanto você ganha por hora ? "))
horas_trabalhadas_mes = float(input("Quantas horas você trabalhou no mês ? "))

salario_bruto = valor_hora * horas_trabalhadas_mes
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - imposto_renda - inss - sindicato

print("Seu salário bruto: R$", salario_bruto)
print("Quantia paga ao imposto de renda: R$", imposto_renda)
print("Quantia paga ao INSS: R$", inss)
print("Quantia paga ao sindicato: R$", sindicato)
print("Seu salário líquido: R$", salario_liquido)




