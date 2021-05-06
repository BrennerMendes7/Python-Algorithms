peso_ideal_mulher = 0
peso_ideal_homem = 0
altura = float(input("Digite a sua altura:"))
genero = int(input("Digite 1 se você é mulher ou digite 2 se você é homem:"))

if genero == 1:
    peso_ideal_mulher = (62.1 * altura) - 44.7
    print("Seu peso ideal mulher é: ", peso_ideal_mulher)
    
elif genero == 2:
    peso_ideal_homem = (72.7 * altura) - 58
    print("Seu peso ideal homem é: ", peso_ideal_homem)
