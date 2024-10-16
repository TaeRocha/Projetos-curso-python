import random

multiplicadores_1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
multiplicando_cpf = []
CPF_INT = []
somando_numero = multip_por_10 = resto_divisao_11 = 0
validacao = ""

for i in range(9):
	CPF_INT.append(random.randint(0, 9))

# Nessa parte dividimos os numeros e indices, 
	# multiplicamos os numeros com os multiplicadores e
	# somamos todos os numeros gerados em uma unica variável.

for i, numero in enumerate(CPF_INT):
	multiplicando_cpf.append(numero * multiplicadores_1[i])
	somando_numero += multiplicando_cpf[i]

multip_por_10 = somando_numero * 10 # Multiplicando em 10 o resultado da soma dos numeros do CPF
resto_divisao_11 = multip_por_10 % 11 # Pegando o resto da divisão por 11, caso seja o 10 digito do cpf, é veridico
confimacao_cpf_1 = resto_divisao_11 if resto_divisao_11 <= 9 else 0
CPF_INT.append(confimacao_cpf_1)
  

# Limpando variáveis para conferir o segundo dígito
multiplicando_cpf.clear()

multiplicadores_1.insert(0, 11) # Colocando o 11 para multiplicar no indice 0 para não precisar criar uma nova lista
somando_numero = resto_divisao_11 = 0

# Multiplicando separadamente e somando todos os numeros do 2 digito
for i, numero in enumerate(CPF_INT):
	multiplicando_cpf.append(numero * multiplicadores_1[i])
	somando_numero += multiplicando_cpf[i]

# Mesmo processo do anterior usando + primeiro digito
# Poderia ser uma função, já que uso duas vezes

multip_por_10 = somando_numero * 10
resto_divisao_11 = multip_por_10 % 11
confimacao_cpf_2 = resto_divisao_11 if resto_divisao_11 <= 9 else 0
CPF_INT.append(confimacao_cpf_2)

condicao_cpf_1 = confimacao_cpf_1 == int(CPF_INT[9])
condicao_cpf_2 = confimacao_cpf_2 == int(CPF_INT[10])
# Sempre lembrar de transformar em inteiro por que ao 
	# comparar fica diferente

validacao = "".join(str(numero) for numero in CPF_INT)
# Usei o join() para juntar os números, mas dentro dele 
	# transformei em str e usei um for para colocar 
	# toda a lista dentro da variavel

if condicao_cpf_1 and condicao_cpf_2:
	print(f"O CPF {validacao} é válido")
else:
	print(f"O CPF {validacao} não é válido")
