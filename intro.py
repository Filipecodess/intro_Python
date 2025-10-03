# print("Hello world!")
# palavra = "olá"
# nome =" Fiipe"
# idade = 22

# print(palavra,"mundo!!")
# print ("olá ",end="")
# print ("mundo!!")
# print("olá","mundo!!", sep="--")
# print(f"meu nome é {nome} e faço {idade} anos em outubro") #sem o fSTRING a saída é literal#
# print("Meu nome é{} e faço {} anos em outubro".format(nome,idade))

# nome = input("Digite seu nome: ")
# print("O seu nome é: ", nome)

# datadenasc = input ("Data de nascimento: ")
# separador = "/"
# print ("A sua data de nascimento é: ", datadenasc, sep= separador)

# dia, mes, ano = input ("Data de nascimento:").split()
# print (f"A sua data de nascimento é: {dia}/{mes}/{ano}")

# idade = 2025 - 2003
# print ("a sua idade é: ", idade)

# print ("Digite a sua idade: ")
# idade = int(input ())
# print ("A sua idade é:", idade)

# try:
#     idade=int(input("Digite a sua idade: "))
#     print ("A sua idade é: ", idade)
# except ValueError:
#     print ("Você digitou a sua idade errado")

# =====================Operadores aritméticos=========================
# num1=10
# num2=2

# soma=num1 + num2 #12
# subt=num1 - num2 #8
# multp= num1 * num2 #20
# div = num1 / num2 #5.0
# divint = num1 // num2 #5
# mod = num1 % num2 #0
# expo = num1 ** num2 #100

# print(f"Operações Aritméticas:{soma}, {subt}, {multp}, {div}, {divint},  {mod}, {expo}")]

# ==========================Operadores de atribuição======================================

# num += 2 # = num = num + 2
# print(num)

#===========================Operadores comparação============================
# x=1456823

# if x % 2 == 0:
#     print (x, "é um número par")
# else:
#     print (x, "é um número ímpar")

# ===========================Operadores lógicos===============================
#and (e), or(ou), not(não)

# a= 5
# b=10
# print ((a > 0) and (b == 0))
# print ((a > 0) and (b != 0))

# a= 5
# b=10
# print ((a > 0) or (b == 0))
# print ((a > 0) or (b != 0))

# a= 5
# b=10
# print (not(a > 0) and (b == 0))
# print (not(a > 0) and (b != 0))

# ===================comandos condicionais================================
# x = int(input("Digite um número: "))
# impar = (x%2==1)
# if impar:
#     print("número ímpar")

# print("fim do programa")

# print("digite um número inteiro: ")
# x = int(input())
# impar = (x%2==1)
# if impar:
#     print("número ímpar")

# print("fim do programa")

# x: int
# x = x%2==1
# input(x)
# if x:
#     print ("impar") #não vai

# x = int(input("Digite um número: "))
# if x%2==1:
#     print("número ímpar")

# print("fim do programa")
# ========================================================================
# a = float(input("digite um número: "))
# b = float(input("digite outro número: "))
# if a > b:
#     print ("maior número é", a)
# else:
#     print ("O maior número é", b)

# a = float(input("digite um número: "))
# b = float(input("digite outro número: "))
# if a == b:
#     print ("Os dois números são iguais")
# else:
#     if a > b:
#         print ("maior número é", a)
#     else:
#         print ("O maior número é", b)
#====================================================================================================
# x = str(input("tá fazendo sol hoje? "))
# x = str(input("tem dinheiro? "))
# if x == "sim" and "sim":
#     print("Vamos para praia")
# else:
#     print("vamos assistir netflix")
#==================================================================================================
# clima = str(input("qual o climinha de hoje? [sol/chuva] "))
# if clima == "sol":
#     din = str(input("tem dinheiro? [sim/não] "))
#     if din =="sim":
#         din1 = int(input("têm quanto? "))
#         if din1 >= 100:
#             print ("vamo para praia!!")
#         else:
#             print("vamos assistir netflix")
#     else:
#         print("vamos assistir netflix")
# else:
#     print ("vamos assistir netflix")
#===============================================================================================
# idade = int(input("Qual a sua idade? "))
# print (f"sua idade é de {idade} anos")
# if idade >= 18:
#     print ("Você é maior de idade")
# else:
#     print ("Você é de menor idade")
# =================================== ESTRUTUTA DE REPETIÇÃO ===============================================================
# soma = 1
# x = int(input("Digite um número: ")) #entrada para start do processo
# while x != 0:
#     x = int(input("Digite um número: "))
#     soma += x
#     print (soma)
# i = 0
# while i <= 10:
#     print (i)
#     i+=1

# i = 1
# while i <= 10:
#     if  i % 2 == 0:
#         print(f"{i} - par")     
#     else:
#         print(f"{i} - impar")
#     i += 1

# i = 100
# while i <= 200:
#     if  i % 2 == 0:
#         print(f"{i} - par")
#     i += 1

# x = 1
# while x <= 100:
#     print(x)
#     x += 1
# print("fim do programa!!")
# totalgeral = 0
# i = 1
# while i <= 3:
#     qtd_acai = int(input(f"informe a quantidade de açaí vendidos no dia {i}: "))
#     total = qtd_acai *3
#     print(f"foram vendidos R$ {total:.2f} de açai.")
#     totalgeral = totalgeral + total
#     i+=1
# print (f"foram vendidos R${totalgeral} de açai em {i-1}")
#========================================ESTRUTURA FOR======================================================
# Sequencia de fibonacci
# n = 20
# n1 =0
# n2 = 1
# for x in range(n):
#     x = n1 + n2
#     print(x)
#     n1 = n2
#     n2 = x
# for x in range(20):
#     print(x)

# for x in range(1,20,2):
#     print(x)
# ==================================================================================================
# lista = [10,20,80,50,40,125,60,70,90,52]
# for posicaopar, valor in enumerate (lista, start=1):
#     if valor % 2 ==0:
#         print(f"posição {posicaopar} da lista é par: {valor}")
#=========================Condicional composta================================
# print("Temos as aulas:")
# print("Aula 1 com 15% de desconto ")
# print ("Aula 2 com 10% de desconto ")
# print ("E as demais aula com 5% de desconto")
# aulas = str(input("Qual aula você quer?"))

# if aulas == "aula 1":
#     print("Você recebeu 15 % de desconto")
# elif aulas == "aula 2":
#     print("Você recebeu 10% de desconto")
# else:
#     print ("Você recebeu 5% de desconto")

# idade = int(input("Qual a sua idade? "))
# print (f"sua idade é de {idade} anos")
# if idade >= 18:
#     print ("Você é maior de idade")
# elif idade >= 66:
#     print("Você é idoso")
# else:
#     print ("Você é de menor idade")
# erro de ordem do if e elif. ao executar com 66 o programa executa o if primeiro e acaba caindo nele.

# idade = int(input("Qual a sua idade? "))
# print (f"sua idade é de {idade} anos")
# if idade >= 66:
#     print ("Você é idoso")
# elif idade >= 18:
#     print("Você é maior de idade")
# else:
#     print ("Você é de menor idade")

#====================================================IMC=================================================================
# altura = float(input("Digite sua altura: "))
# peso = float(input("digite seu peso: "))
# print(f"A sua altura é {altura} M e o seu peso é {peso} kg")
# imc = peso / altura**2
# print(f"O seu IMC é de {imc:.2f}")
# if imc < 17:
#     print("muito abaixo do peso")
# elif 17 <imc< 18.49:
#     print ("abaixo do peso")
# elif 18.5 <imc<24.99:
#     print ("peso normal")
# elif 25<imc<29.99:
#     print ("acima do peso")
# elif 30<imc<34.99:
#     print ("obesidade I")
# elif 35<imc<39.99:
#     print ("obesidade II(severa)")
# else:
#     print("obesidade III (mótbida)")

#==================================================== EXERCICIO 1 =====================================================================
# 1. Faça um programa que exiba seu nome na tela
# print("Filipe Gabriel da Silva Araújo")
# 2. Cálculo do aumento de salário - Forma que ele calcule um aumento de 15% para um salário de R$ 1250
# salário = 1250
# porc = 1250*15/100
# aumento = porc + 1250
# print (f"Seu salário com o aumento é R$ {aumento}")
# 3. Converta as seguintes expressões matemáticas para que possam ser calculadas usando o interpretador Python.
# multsom = 10 + 20 * 30
# div = 42 / 30
# op = (94+2) * 6 - 1
# print(f"{multsom}, {div}, {op}")
# 4. Complete a tabela a seguir, marcando inteiro ou ponto flutuante dependendo do número apresentado.
# a = 5; b = 5.0; c = 4.3; d = -2; e = True; f = "Python"

# print(type (a), type (b), type(c), type(d), type(e), type(f))
# 5. Faça um programa em linguagem Python que converta metros para centímetros.
# metros = int(input("Digite um número: "))
# centimetro = metros * 100
# print ("A conversão de metros para centimetro é:", centimetro, "cm" )

# ========================================================EXERCICIO 2====================================================================
# 1. Faça um programa que recebendo um valor inteiro, informe se o número é positivo, negativo ou neutro.
# num = int(input("Digite um número "))
# if num > 0:
#     print(num, "é positivo")
# elif num < 0:
#     print(num, "é negativo")
# else:
#     print(num, "é neutro") 
# 2.	Faça um programa em linguagem Python que leia dois números inteiros e informe se estes são iguais ou diferentes.
# x = int(input("Digite um número: "))
# y = int(input("Digite outro número: "))

# if x==y:
#     print(f"{x} e {y} são números iguais")
# else:
#     print("os números são diferentes")
# 3. Crie um código em linguagem Python que peça o nome do usuário por meio da função input (). 
#    Se o nome for "Optimus Prime", imprima "Bem-vindo, você é um guerreiro de Cybertron". 
#    Caso contrário, imprima "Bom dia, NOME". (Substitua o NOME pelo nome do usuário).
# nome = str(input("Digite seu nome: "))
# if nome == "Optimus Prime":
#     print("Bem-vindo, você é um guerreiro de Cybertron")
# else:
#     print(f"Bom dia, {nome}")
# 4. Faça um programa que solicite ao usuário sua idade, depois disso, 
# exiba a classificação etária de acordo com as faixas de valores:

# idade = int(input(" Qual a sua idade: "))
# print(f"A minha idade é de {idade}")
# if 0 <= idade <= 11:
#     print("Você é criança!")
# elif 12 <= idade <= 17:
#     print("Você é adolescente!")
# elif 18 <= idade <= 24:
#     print("Você é jovem!")
# elif 25 <= idade <= 40:
#     print("Você é adulto!")
# elif 41 <= idade <= 59:
#     print("Você está na meia-idade!")
# else:
#     print("Você é idoso!")
# 5. Faça um algoritmo que solicite o ano que o usuário nasceu, 
# depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.
# anoNasc = int(input("Qual o ano do seu nascimento? "))
# anoAtual = 2025
# idade = 2025 - anoNasc
# anoIdade = anoNasc + 18
# if idade == 18:
#     print("Voçê tem 18 anos!")
# elif idade > 18:
#     print (f"Você fez 18 anos no ano de {anoIdade}")
# else:
#     print("Você ainda irá fazer 18 anos!")

# ==============================DESAFIO 01===============================================================
# Realize a refatoração do código abaixo, alterando a estrutura de 
# “def case” para o uso o “IF/ELIF”. Outras alterações no código poderão ser realizadas também:
# print("1-ANTARTICA R$6.00; 2-SKOL R$6.50")
# print("3-BRAHMA R$8.20; 4-SOL R$8.25")
# print("5-NORTENHA R$16.80; 6-PROIBIDA R$4.80")
# print("7-DEVASSA R$5.90; 8-HEINEKEN R$9.00")
# cerveja = int(input("digite o número para pegar a sua cerveja: "))
# if cerveja ==9:
#     print("número inválido")
# else:
#     print("qual a quantidade?")
#     qtd = int(input("Digite aqui a quantidade: "))
#     if cerveja == 1:
#         valor_cerveja1 = 6 * qtd
#         cerveja1 = "Antartica"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja1} no valor de R${valor_cerveja1}")
#     elif cerveja == 2:
#         valor_cerveja2 = 6.5 * qtd
#         cerveja2 = "Skol"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja2} no valor de R${valor_cerveja2}")
#     elif cerveja == 3:
#         valor_cerveja3 = 8.2 * qtd
#         cerveja3 = "Brahma"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja3} no valor de R${valor_cerveja3}")
#     elif cerveja == 4:
#         valor_cerveja4 = 8.25 * qtd
#         cerveja4 = "Sol"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja4} no valor de R${valor_cerveja4}")
#     elif cerveja == 5:
#         valor_cerveja5 = 16.8 * qtd
#         cerveja5 = "Nortenha"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja5} no valor de R${valor_cerveja5}")
#     elif cerveja == 6: 
#         valor_cerveja6 = 4.8 * qtd
#         cerveja6 = "Proibida"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja6} no valor de R${valor_cerveja6}")
#     elif cerveja == 7:
#         valor_cerveja7 = 5.90 * qtd
#         cerveja7 = "Devassa"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja7} no valor de R${valor_cerveja7}")
#     elif cerveja == 8:
#         valor_cerveja8 = 9 * qtd
#         cerveja8 = "Heineken"
#         print (f"A sua compra é de {qtd} cerveja(s) {cerveja8} no valor de R${valor_cerveja8}")
#     print("podemos confirmar a sua compra?")
#     print("sim - confirmar a compra")
#     print("não - cancelar a compra")
#     conf = str(input())
#     if conf == "sim":
#         print("COMPRA REALIZADA COM SUCESSO")
#     else:
#         print("COMPRA CANCELADA")