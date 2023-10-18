# #Questão1===============================
# print("Alô Mundo!")



# #Questão2===============================
# num=input("Digite um número: ")
# print(f"O número informado foi {num}")



# #Questão3===============================

# num1, num2= float(input("Digite dois números e receba sua soma: ")),float(input())
# print(f"A soma de {num1} e {num2} é igual a {num1+num2}")



# # Questão4===============================
# cont=0
# for i in range(4):
    
#     cont+=float(input(f"Digite a {i+1}° Nota: "))
    
# print("A média das notas dadas é", cont/4)



# # Questão5===============================
# centi=float(input("Digite quantos Centímetros deseja converter: "))
# print(f"Isso equivale a {centi/100} metros")




# # Questão6===============================
# raio=float(input("Quantas unidades tem o raio do círculo?: "))
# print(f"Um circulo com {raio} unidades de medida tem área de {3.141592*raio**2:0.2f} Unidades²")




# # Questão7===============================
# lado=float(input("Quanto mede o lado de seu Quadrado?: "))

# print(f"A área dele é de {lado**2}u² e o dobro de sua área é de {(lado**2)*2}u²")



# # Questão8===============================
# salario_hora,horas_mes= float(input("Quantos reais você ganha por hora?: ")),float(input("E quantas horas você trabalhou este mês?: "))
# print(f"Seu sálario deve ser de R${salario_hora*horas_mes}")



# # Questão9===============================
# fahrenheit=float(input("Converta de Fahrenheit para graus Celsius! Digite a temperatura em °F: "))
# print(f'Isso equivale a {5 * ((fahrenheit-32) / 9):0.2f}°C')



# #Questão10======================================
# celsius=float(input("Digite aqui a temperatura em celsius que será convertida: "))
# Fahrenheit=(celsius*9/5+32)
# print(f"Isso equivale a {Fahrenheit}°F")



# #Questão11====================================
# inteiro_1,inteiro_2,real= input("Digite dois números inteiros e um real: ").split()
# inteiro_1, inteiro_2, real= int(inteiro_1),int(inteiro_2), float(real)
# print(f"O dobro do primeiro vezes metade do segundo é {inteiro_1*2*(inteiro_2/2)}")
# print(f"\n A soma do triplo do primeiro com o terceiro é {inteiro_1*3+real}\n")
# print(f"O terceiro elevado ao cubo é {real**3}")


# #Questão12=====================================
# altura= float(input("Digite aqui sua altura em metros: "))
# print(f"Seu peso ideal é de {(72.7*altura) - 58}")



# #Questão13=======================================
# altura= float(input("Digite aqui sua altura em metros: "))
# print(f"""Seu peso ideal é:
#       {(72.7*altura) - 58}kg sexo masculino
#       {(62.1*altura) - 44.7:.2f}kg sexo feminino""")




# #Questão14===================================
# excesso=float(input("Digite aqui quantos kilogramas de peixe você tem: "))-50
# multa=excesso*4
# print(f"Você tem {excesso}kg a mais do que o limite, deverá pagar uma multa de R${multa}")


# #Questão15===========================================
# salario_hora=float(input("Quanto você ganha por hora trabalhada?: R$"))
# horas=float(input("Quantas horas você trabalhou este mês?: "))
# salario=salario_hora*horas
# print(f"""
# + Salário Bruto : R${salario}
# - IR (11%) : R${salario-salario*0.11}
# - INSS (8%) : R${salario-salario*0.08}
# - Sindicato ( 5%) : R${salario-salario*0.05}
# = Salário Liquido : R${salario-salario*0.24}""")



#Questão16========================================
metros_q=float(input("Quantos metros quadrados tem a área que você vai pintar?: "))
litros=metros_q/3
if litros/18>int(litros/18):
    print(f"Serão necessárias {int(litros/18)+1} latas, você pagará R${(int(litros/18)+1)*80}")
else:
    print(f"Serão necessárias {litros/18} latas, você pagará R${litros/18*80}")








    
