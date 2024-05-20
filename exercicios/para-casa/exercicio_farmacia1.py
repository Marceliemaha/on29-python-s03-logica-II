preco_codigo_0054 = 10.4
preco_codigo_0053 = 4.6
preco_codigo_0045 = 50.0

valor = 0

primeiro_produto = int(input())
segundo_produto = int(input())

if (primeiro_produto == 54):
    valor += preco_codigo_0054
elif (primeiro_produto == 53):
    valor += preco_codigo_0054
elif (primeiro_produto == 45):
    valor+=preco_codigo_0045

if (segundo_produto == 54):
    valor += preco_codigo_0054
elif (segundo_produto == 53):
    valor += preco_codigo_0054
elif (segundo_produto == 45):
    valor+=preco_codigo_0045


if primeiro_produto == segundo_produto:
    valor += preco_codigo_0054 
