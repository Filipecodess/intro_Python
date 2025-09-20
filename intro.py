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

# =========== ESTRUTUTA DE REPETIÇÃO ====================
# soma = 1
# x = int(input("Digite um número: ")) #entrada para start do processo
# while x != 0:
#     x = int(input("Digite um número: "))
#     soma += x
#     print (soma)

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
# 4. 


