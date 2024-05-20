nota = 6
presenca = 50

if nota >= 7 or presenca == 100:
    print("APROVADO!!")
elif nota < 7 and nota > 5:
    if nota > 5 and presenca >= 90:
        print("APROVADO!!")
    elif nota >= 6 and presenca >= 50:
        nota = 8
        print("Apto a fazer a recuperacao")
else:
    print("REPROVADO")
print("Fim do Programa")
