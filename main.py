"""
exercício 1
Você está analisando um conjunto de dados de vendas e precisa garantir que todos os registros tenham valores positivos para quantidade e preço.
Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos forem positivos ou "Dados inválidos" caso contrário.
"""

# quant=10
# price=10

# if quant>0 and price>0:
#     print('Dados Válidos')
# else:
#     print('Dados Invalidos')


"""
exercício 2
Imagine que você está trabalhando com dados de sensores IoT.
 Os dados incluem medições de temperatura.
 Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
Temperatura < 18°C é 'Baixa'
Temperatura >= 18°C e <= 26°C é 'Normal'
Temperatura > 26°C é 'Alta'

"""
# temp=25

# if temp<18:
#     print("Baixa")
# elif temp>=18 and temp<=26:
#     print("Normal")
# else:
#     print("alta")

"""
Você está analisando logs de uma aplicação e precisa filtrar mensagens com severidade 'ERROR'.
 Dado um registro de log em formato de dicionário como log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
 , escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
"""

# log={'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level']=="ERROR":
#     print("erro")

"""
Antes de processar os dados de usuários em um sistema de recomendação,
 você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha fornecido um email válido.
 Escreva um programa que valide essas condições e imprima "Dados de usuário válidos" ou o erro específico encontrado.
"""

# email="theo_lou@hotmail.com"
# idade=19

# if idade<18 and idade>65:
#     print("digite uma idade válida")
# elif "@" not in email and "." not in email:
#     print("email inválido")
# else:
#     print("sucesso")

"""
ocê está trabalhando em um sistema de detecção de fraude e precisa identificar transações suspeitas.
Uma transação é considerada suspeita se o valor for superior a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h).
   Dada uma transação como transacao = {'valor': 12000, 'hora': 20}, verifique se ela é suspeita.
"""

# transacao={'valor': 12000, 'hora': 20}

# if transacao['valor']>12000 or (transacao['hora']<9 or transacao['hora']>18):
#     print("Transacao suspeita")


"""
6. Contagem de Palavras em Textos
Objetivo: Dado um texto, contar quantas vezes cada palavra única aparece nele.
"""

# texto = "oi meu nome é é é theo souza prado lourenção oi"

# texto_ls=texto.split()
# lista=[]
# registro={}

# for p in texto_ls:
#     if p not in registro:
#         registro[p]=1
#     else:
#         registro[p]+=1

# print(registro)

"""
7.
Objetivo: Normalizar uma lista de números para que fiquem na escala de 0 a 1.
"""

# numeros=[3,13,16,300,450,650]
# lista_normalizada=[]

# maior=max(numeros)
# menor=min(numeros)

# intervalo_geral=maior-menor

# for i in numeros:
#     numero_corrente=i
#     range_begin=numero_corrente-menor
#     escala= range_begin/intervalo_geral
#     lista_normalizada.append(escala)

# print(lista_normalizada)

"""
8.
Objetivo: Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
"""



# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos= [usuario for usuario in usuarios if usuario['email']]
        
# print(usuarios_validos)


"""

9. Extração de Subconjuntos de Dados
Objetivo: Dada uma lista de números, extrair apenas aqueles que são pares.

"""

# valores= range(1,12)

# pares = [x for x in valores if x % 2==0]
# print(pares)

"""
10.Agregação de Dados por Categoria
Objetivo: Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
"""

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]

total_por_categoria = {}

for venda  in vendas:
    categoria=venda["categoria"]
    valor = venda["valor"]
    if categoria in total_por_categoria:
        total_por_categoria[categoria]+=valor
    else:
        total_por_categoria[categoria]=valor


print(total_por_categoria)