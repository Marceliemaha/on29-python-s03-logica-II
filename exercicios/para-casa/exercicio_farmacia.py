preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0


primeiro_produto = int(input())
segundo_produto = int(input())

# desenvolva a logica condicional

#como identificar o valor do código com preço

if primeiro_produto == 54:  #se o primeiro produto for o produto 00054
    primeiro_produto = preco_codigo_0054 #se o primeiro produto for 0054, entra aqui, pega o código 0054 e transforma no preço do produto correspondente
elif primeiro_produto == 53:  #se não, verifica se o primeiro produto é o produto 00053
    primeiro_produto = preco_codigo_0053 #se o primeiro produto for 0053, entra aqui, pega o código 0053 e transforma no preço do produto correspondente
else:       #caso seja negativa as condições anteriores, então o primeiro produto é o produto 00045 
    primeiro_produto =  preco_codigo_0045 # nesse caso, entra aqui, pega o código 0045 e transforma no preço do produto correspondente

if segundo_produto == 54:  #se o segundo produto for o produto 00054
    segundo_produto = preco_codigo_0054  #se o segundo produto for 0054, entra aqui, pega o código 0054 e transforma no preço do produto correspondente
elif segundo_produto == 53:  #se não, verifica o segundo produto é o produto 00053
    segundo_produto = preco_codigo_0053 #se o segundo produto for 0053, entra aqui, pega o código 0053 e transforma no preço do produto correspondente
else:    #caso seja negativa as condições anteriores, então o segundo produto é o produto 00045
    segundo_produto =  preco_codigo_0045 # nesse caso, entra aqui, pega o código 0045 e transforma no preço do produto correspondente

#lógica para desconto

if primeiro_produto == segundo_produto: # se o primeiro produto for igual ao segundo produto, então entra nessa condição
    print((primeiro_produto + segundo_produto) - 5) #logo, vai somar o primeiro produto mais o segundo produto e tirar 5 reais de desconto (desconto para produtos iguais)
elif primeiro_produto == preco_codigo_0054 or segundo_produto == preco_codigo_0054: #aqui verifica se uma dos dois produtos é o código 0054, por que se for, aplica o desconto de 50% no produto 0054
    if preco_codigo_0054 == preco_codigo_0054: #verifica se o preço do código 0054 é igual ao preço do código 0054, se for entra no print
        print((primeiro_produto/2) + segundo_produto)  #atendendo a condição à cima, que verifica se o primeiro produto é o produto 0054, então printar o preço do primeiro produto dividido por 2 mais o preço do segundo produto
    else:  #  não atendendo todas as outras condições, se não é o primeiro produto, logo será o segundo, entra nesse print
        print((segundo_produto/2) + primeiro_produto)  # o segundo produto sendo igual ao produto 0054, dividi o preço do segundo produto por 2 e soma com o preço do primeiro produto
else: # se não (se os produtos não forem iguais e nenhum deles for o produto 0054), então entra nesse print aqui
    print(primeiro_produto + segundo_produto) #soma o primeiro produto com o segundo produto, sem nenhum desconto 


