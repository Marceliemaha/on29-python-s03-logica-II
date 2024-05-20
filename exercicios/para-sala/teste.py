nota = float(input("Qual a sua nota?: "))
presenca = int(input("qual a sua porcentagem de presença (%)?: "))
media = 7

if (nota >= media or presenca == 100) or (nota > 5 and presenca > 90):
    print("Você está Aprovado!!")
elif nota < 7 and nota > 5:
    if nota > 5 and presenca >= 90:
        print("APROVADO!!")
    elif nota >= 6 and presenca >= 50:
        print("Apto a fazer a recuperacao")
else:
    print("REPROVADO")
print("Fim do Programa")
