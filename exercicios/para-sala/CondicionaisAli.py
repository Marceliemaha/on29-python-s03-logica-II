nota = 7
recuperacao = 6


if nota >= 7:    
    print("APROVADO!!")
elif nota >= 5 :
    print("RECUPERAÇÃO.")
    if recuperacao >= 7:
        print("APROVADO NA RECUPERAÇÃO.")
    elif recuperacao > 5:
        print("APROVADO EM TURMA ESPECIAL.")
    else:
        print("REPROVADO.")
else: 
    print("REPROVADO!!")
print("Final do programa!")