# #Questão1============================
# num1, num2=input("Digite 2 números que eu direi o maior: ").split()
# num1 = float(num1)
# num2= float(num2)
# if num1>num2:
#     print(num1, "é o maior valor")
# elif num2>num1:
#     print(num2, "é o maior valor")

# else:
#     print("Os valores são iguais")  



# #Questão2===========================
# num=float(input("Digite um número positivo ou negativo: "))
# if num>0:
#     print("Número é positivo")
# elif num<0:
#     print("Número é negativo")
# else:
#     print("0 é neutro")




# #Questão3=========================
# sexo=input("Informe seu sexo biológico: F (Feminino) ou M (Masculino) ").upper()
# if sexo=="F":
#     print('Sexo feminino')

# elif sexo=="M":
#     print("Sexo Masculino")
    
# else:
#     print("Sexo inválido")


# #Questão 4==============================
# letra=input("Digite uma LETRA qualquer: ").upper()
# if letra in "AEIOU":
#     print("Essa letra é uma vogal")
    
# else:
#     print("Essa letra é uma consoante")



# #Questão5=====================================
# nota1=float(input("Digite aqui a primeira nota do Aluno: "))
# nota2= float(input("Segunda nota: "))
# media=(nota1+nota2)/2
# print("NOTA MÉDIA: ", media )

# if media==10:
#     print("APROVADO com Distinção")
# elif media>=7:
#     print("Aprovado")
    
# else:
#     print("Reprovado")



# #Questão6==========================
# print("Digite 3 numeros: ")
# lista=[]
# for i in range(1,4):
#     lista.append(float(input(f"{i}° Número: ")))
    
# print("O maior valor digitado foi: ", max(lista))



# #Questão7===================================
# print("Digite 3 numeros: ")
# lista=[]
# for i in range(1,4):
#     lista.append(float(input(f"{i}° Número: ")))
    
# print("O maior valor digitado foi: ", max(lista))
# print("O menor valor digitado foi: ", min(lista))


# #Questão8==================================

# lista={"A":0,'B':0, "C":0}

# lista["A"]=float(input("Qual o preço do Produto A?: R$"))
# lista["B"]=float(input("Qual o preço do Produto B?: R$"))
# lista["C"]=float(input("Qual o preço do Produto C?: R$"))

# print("O produto que você deve comprar é o: ", min(lista),"\n Pois custa apenas: R$",lista[min(lista)])



# #Questão9==================================
# lista=[]
# print("Digite 3 numeros: ")

# for i in range(1,4):
#     lista.append(float(input(f"{i}° Número: ")))
    
# lista.sort(reverse=True)
# print("Os números que você digitou em ordem descrecente: ", *lista)


# #Questão10====================
# turno=input("""Digite a respectiva letra para seu turno de estudo.
#             M - Matutino
#             V - Vespertino
#             N - Noturno\nDigite aqui: """).upper()

# if turno=="M":
#     print("Bom dia e bons estudos")
    
# elif turno=="V":
#     print("Boa tarde e bons estudos")
    
# elif turno == "N":
#     print("Boa noite e bons estudos")
    
# else:
#     print("Turno Inválido")


# #Questão11=======================================
# salario=float(input("Digite o valor do seu salário: R$"))
# def ajustes(salario,percentual):
#     print("O seu salário antes do reajuste era: R$",salario)
#     print(f"O percentual de aumento aplicado foi de {percentual}%")
#     print("O valor do aumento foi de: R$",salario*percentual/100)
#     print("O seu novo salário é de: R$",salario*(percentual/100+1))

# if salario<=280:
#     ajustes(salario,20)
# elif 280 < salario <=700:
#     ajustes(salario,15)

# elif 700 < salario <=1500:
#    ajustes(salario,10)

# elif salario > 1500:
#     ajustes(salario,5)


# #Questão12========================================
# def impostos(salario_hora,horas):
#     salario=horas*salario_hora
#     print(f'''
#         (-) IR (5%)                     : R${salario*0.05:.2f}
#         (-) INSS ( 10%)                 : R${salario*0.1:.2f}
#         FGTS (11%)                      : R${salario*0.11:.2f}
#         Total de descontos              : R${salario*0.15:.2f}
#         Salário Liquido                 : R${salario-salario*0.15:.2f}''')

# salario_hora=float(input("Digite o valor do seu salário por hora: R$"))
# horas=float(input("Digite a quantidade de horas trabalhadas no mês: "))
# impostos(salario_hora,horas)


# #Questão13========================================
# dia=int(input("Digite o dia: "))
# if dia==1:
#     print("Domingo")
# elif dia==2:
#     print("Segunda")
# elif dia==3:
#     print("Terça")
# elif dia==4:
#     print("Quarta")
# elif dia==5:
#     print("Quinta")
# elif dia==6:
#     print("Sexta")
# elif dia==7:  
#     print("Sábado")
# else:
#     print("Valor inválido")

# #Questão14================================
# nota1=float(input("Digite a 1° Nota: "))
# nota2=float(input("Digite a 2° Nota: "))
# media=(nota1+nota2)/2
# if 0<=media<4:
#     print(f"Sua média é {media} , seu conceito é E")
    
# elif 4<=media<6:
#     print(f"Sua média é {media} , seu conceito é D")
    
# elif 6<=media<7.5:
#     print(f"Sua média é {media} , seu conceito é C")
    
# elif 7.5<=media<9:
#     print(f"Sua média é {media} , seu conceito é B")
    
# elif 9<=media<=10:
#     print(f"Sua média é {media} , seu conceito é A")


#Questão 15===============================
ladoA,ladoB,ladoC=0,0,0
ladoA=float(input("Digite a medida do 1° lado do triângulo: "))
ladoB=float(input("Digite a medida do 2° lado do triângulo: "))
ladoC=float(input("Digite a medida do 3° lado do triângulo: "))

if ladoA+ladoB<=ladoC or ladoC+ladoB<=ladoA or ladoA+ladoC<= ladoB:
    print("Com essas medidas não é possivel formar um Triângulo")
    




