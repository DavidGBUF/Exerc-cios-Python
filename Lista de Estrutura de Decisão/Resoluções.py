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


#Questão10====================
turno=input("""Digite a respectiva letra para seu turno de estudo.
            M - Matutino
            V - Vespertino
            N - Noturno\nDigite aqui: """).upper()

if turno=="M":
    print("Bom dia e bons estudos")
    
elif turno=="V":
    print("Boa tarde e bons estudos")
    
elif turno == "N":
    print("Boa noite e bons estudos")
    
else:
    print("Turno Inaválido")



