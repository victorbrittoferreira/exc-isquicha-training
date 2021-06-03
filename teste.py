############## Sequential Structures ##############

##3 Faça um Programa que peça dois números e imprima a soma.

##num1 = int (input("Digite um numero: "))
##num2 = int (input("Digite outro numero: "))
##sum = num1 + num2
##
##print(f"A soma entre {num1} e {num2} é {sum}")


##4 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

#Nota1 = float (input("Digite a nota final do primeiro bimestre "))
#Nota2 = float (input("Digite a nota final do segundo bimestre "))
#Nota3 = float (input("Digite a nota final do terceiro bimestre "))
#Nota4 = float (input("Digite a nota final do quarto bimestre "))
#
#Media = (Nota1 + Nota2 + Nota3 + Nota4) / 4
#print( 
#    f"A média final do período letivo foi de {Media:.2f}")


##5 Faça um Programa que converta metros para centímetros.

#metros_inp = float (input("Digite o valor em metros: "))
#centim_out = metros_inp*100

#print (f"{metros_inp}; metro(s) equivale(m) a {centim_out:.0f} centímetro(s).")

#print ('{} metro(s) equivale(m) a {} centímetro(s)'.format( metros_inp, int(centim_out)))
###better option
#print ('{} metro(s) equivale(m) a {:.0f} centímetro(s)'.format( metros_inp, (centim_out)))


##6 Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

##pi = 3.14

##radius = float (input("Digite o tamanho do raio em metro(s): "))
##circle_area = pi * (radius**2)
##
##print(f'A área de um círculo de raio {radius} é {circle_area:.2f} m²(s)' )


##7 Faça um Programa que calcule área de um quadrado, em seguida mostre o 
# dobro desta área para o usuário.

#base = float (input("Digite o tamanho do base em metro(s): "))
#height = float (input("Digite o tamanho do lado em metro(s): "))
#
#square_area = (base * height)*2
#print('O dobro da área do quadrado é {:.2f} m²(s).' . format(square_area))


##8 Faça um programa que pergunte quanto você ganha por hora e o número de 
#horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido 

#pay_per_hour = float (input("Digite quanto ganha por hora trabalhada: "))
#worked_hours = float (input("Digite quantas horas trabalhou nesse mês: "))
#
#salary = pay_per_hour * worked_hours
#print("Seu salário esse mês será de {:.2f}" .format(salary))


##9 Faça um Programa que peça a temperatura em graus Farenheit, transforme
#  e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).

#temp_farenheit = float (input("Digite a temperatura em Farenheit(s): "))
#
#temp_celsius = (5 * (temp_farenheit - 32)/ 9)
#print("A temperatura em Celsius equivale a {:.2f}º" .format(temp_celsius))


##10 Faça um Programa que peça a temperatura em graus Celsius, transforme 
# e mostre em graus Farenheit.

#temp_celsius = float (input("Digite a temperatura em Celsius(s): "))
#
#temp_farenheit = (((temp_celsius/ 5)*9)+32)
#print("A temperatura em Farenheit(s) equivale a {:.2f}º" .format(temp_farenheit))


##11 Faça um Programa que peça 2 números inteiros e um número real. Calcule e 
# mostre: o produto do dobro do primeiro com metade do segundo. a soma do
# triplo do primeiro com o terceiro. o terceiro elevado ao cubo.


#while True:
#    try:
#        st_int = int (input("Digite um número inteiro: ")) 
#        break 
#    except ValueError:    
#        print('Apenas números inteiros!')
#    continue
#
#while True:
#    try:
#        nd_int = int (input("Digite outro número inteiro: ")) 
#        break 
#    except ValueError:    
#        print('Apenas números inteiros!')
#    continue
#
#while True:
#    try:
#        rd_nat = int (input("Digite um número real: ")) 
#        if rd_nat >= 0:
#                break
#        else:
#            print('Apenas números inteiros iguais ou maiores que 0..(0,1,2...')     
#    except ValueError:    
#        print('Apenas números inteiros iguais ou maiores que 0..(0,1,2...)')
#    continue
#    
#st_calc = ((2*st_int)+(nd_int/2))
#print("O produto do dobro do primeiro com metade do segundo é {}".format(st_calc))
#
#nd_calc = (3*st_int)+rd_nat
#print("A soma do triplo do primeiro com o terceiro é {}".format(nd_calc))
#
#rd_calc = rd_nat**3
#print("O terceiro elevado ao cubo é {}".format(rd_calc))

#########  
#i = input("Digite um número inteiro: ")
#
#def integer (i):
#    if i % 1 == 0:
#        return print( 'nope')
#    else:
#        return print('try again')
    



#st_numb = int (input("Digite um número inteiro: ")) 
# o primeiro numero deverá ser inteiro, isto é: (...-1, 0, 1, ...)

#nd_numb = int (input("Digite outro número inteiro: ")) 
# o segundo numero deverá ser inteiro (...-1, 0, 1, ...)

#rd_numb = int (input("Digite um número real: ")) 
# o terceiro numero deverá ser natural (0, 1, ...)

#if rd_numb % 1 == 0 and rd_numb >= 0:
#    print ('ok')
#else:
#   print('nope')


#num1 = int(input("Digite um numero inteiro: "))
#num2 = int(input("Digite outro numero inteiro: "))
#num3 = float(input("Digite um numero real: "))
#a = (num1 * 2) * (num2 / 2)
#b = (num1 * 3) + num3
#c = num3 ** 3
#
#print(f"a: {a}\nb: {b}\nc: {c}")


##12Tendo como dados de entrada a altura de uma pessoa, construa
# um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# (72.7*altura) - 58

#height_inp = float ( input('Digite a sua altura: '))
#
#ideal_weight =( height_inp  * 72.7) - 58
#
#print('Seu peso ideal para a sua altura é', ideal_weight , 'kg(s)')
#print(f'Seu peso ideal para a sua altura é {ideal_weight:.2f}kg(s)')


##13 Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#    Para homens: (72.7*h) - 58
#    Para mulheres: (62.1*h) - 44.7

#h_inp = float ( input('Digite a sua altura: '))
#
#ideal_wm =( h_inp  * 72.7) - 58
#ideal_ww =( h_inp  * 62.1) - 44.7
#
#print(f'Seu peso ideal para a sua altura é: \n {ideal_wm:.2f}kg(s) para homens')
#print(f'{ideal_ww:.2f} kg(s) para mulheres')


##14 João , homem de bem, comprou um microcomputador para 
# controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
#regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa
#de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso
#(peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite
#e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

#peso_peixe = float ( input('Digite o peso em quilos de peixe pescados: '))
#
#mult_pkg = 4
#
#excesso_peso =  peso_peixe - 50
#
#valor_multa = excesso_peso * 4
#
#print(f'O valor a ser pago para o fisco ambiental do Estado é {valor_multa:.1f} R$')


##15Faça um Programa que pergunte quanto você ganha por hora e o número de horas
#trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês,
#sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#    salário bruto.
#    quanto pagou ao INSS.
#    quanto pagou ao sindicato.
#    o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#    + Salário Bruto : R$
#    - IR (11%) : R$
#    - INSS (8%) : R$
#    - Sindicato ( 5%) : R$
#    = Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.

#salario_hora = float ( input('Digite quanto ganha por hora: '))
#horas_trabalhadas = float ( input('Digite quantas horas trabalha: '))
#salario_bruto = horas_trabalhadas * salario_hora
#print (f' Total de salário bruto {salario_bruto:.2f} R$')
#
#IR = 0.11 
#salario_ir = salario_bruto * IR
#print (f' Total de Imposto de Renda {salario_ir:.2f} R$')
#
#INSS = 0.08 
#salario_inss = (salario_bruto - salario_ir) * INSS
#print (f' Total de INSS {salario_inss:.2f} R$')
#
#SIND = 0.05 
#salario_sind = (salario_bruto - salario_ir - salario_inss) * SIND
#print (f' Total de Sindicato {salario_sind:.2f} R$')
#
#total_descontos = salario_ir + salario_inss + salario_sind
#print (f' Total de descontos {total_descontos:.2f} R$')
#
#salario_liquido = salario_bruto - total_descontos
#print (f' Total de liquido {salario_liquido:.2f} R$')


##15 Faça um programa para uma loja de tintas.
# - O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# - Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e 
# - que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
# - Informe ao usuário a quantidades de latas de tinta a serem compradas e o 
# preço total.

#area_apintar = float ( 
#    input('Digite quanto(s) metros quadrado(s) a serem pintado(s): '))
#
#litros_lata = 18
#
#m2_litro = 3
#
#custo_lata = 80
#
#m2_total_lata = litros_lata * m2_litro
#
#latas_int = (area_apintar / m2_total_lata)
#
#preco = latas_necessarias * custo_lata
#
#print (f' Total de latas a serem compras: {latas_necessarias:.0f}')
##print ('Total de latas a serem compras {}'latas_necessarias)))
#
#print (f" e o preço total é: {preco:.2f} R$")


##16 Faça um Programa para uma loja de tintas.
#O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados
#e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00
#ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas
#e os respectivos preços em 3 situações:
#    comprar apenas latas de 18 litros;
#    comprar apenas galões de 3,6 litros;
#    misturar latas e galões, de forma que o preço seja o menor.
#obs: Acrescente 10% de folga e sempre arredonde os valores para cima,
#        isto é, considere latas cheias.

#import math
#
######### CAPUT #######
#
#m2_plitro = 6
#
#folga = 1.1
#
######### 18l
#
#custo_lata = 80
#
#litros_lata = 18
#
#custo_lata_p_litro = custo_lata / litros_lata
#
######### 3,6l
#
#custo_galao = 25
#
#litros_galao = 3.6 
#
#custo_galao_p_litro = custo_galao / litros_galao
#
#razao_custo_equilib_g_x_l = 64.8
#
#
#
#print('-------------INPUT--------------')
#print('')
#area_inputar = math.ceil(float (input('Digite a área a pintar em m2(s): ')))
#print('')
#
#area_apintar = math.ceil (area_inputar * folga)
#print (f'Area a pintar com folga de 10% será de {area_apintar} m2(s)')
#print('')
#
#
#
##print('------------LATAS---------------')
##print('')
#
###### METROS PINTAVEIS POR LATA
#capacidade_lata = litros_lata * m2_plitro
##print(f'Capacidade total 18l: {capacidade_lata:.2f}')
##print('')
#
###### LATAS INTEIRAS
#latas_int = (math.ceil(area_apintar / capacidade_lata))
##print(f'Latas variaveis arredondadas: {latas_int:.2f}')
##print('')
#
###### LATAS INTEIRAS A PINTAR AREA 
#lat_int_area = area_apintar // capacidade_lata
##print(f'Latas inteiras com sobra de tinta com sobra de area pra galear {lat_int_area:.2f}')
##print('')
#
###### RESTO DE LATAS INTEIRAS POR AREA A PINTAR
#latas_float = area_apintar / capacidade_lata
##print(f'Latas variaveis não arredondas: {latas_float:.2f}')
##print('')
#
###### CUSTO TOTAL DE LATAS INTEIRAS
#custo_total_latas = latas_int * custo_lata
##print(f'Custo das latas a solicitação: {custo_total_latas:.2f} R$')
#
#
##print('')
##print('------------GALÕES--------------')
##print('')
#
###### METROS PINTAVEIS POR GALAO
#capacidade_galao = litros_galao * m2_plitro 
##print(f'Capacidade total 3,6l: {capacidade_galao:.2f}')
##print('')
#
###### GALOES INTEIROS 
#galoes_int = math.ceil( area_apintar / capacidade_galao )
##print(f'Galões variaveis arredondados: {galoes_int}')
##print('')
#
###### SOBRAS DE AREA NÃO COBERTA POR > 1 LATAS INTEIRAS
#resto_galeavel = area_apintar % capacidade_lata
##print(f'Resto de area galeavel {resto_galeavel} m2')
##print('')
#
###### GALOES POR RESTO DE AREA 
#resto_galeado = math.ceil(resto_galeavel / capacidade_galao)
##print(f'Galao(oes) necessario(s) por resto de area galeavel {resto_galeado}')
##print('')
#
###### CUSTO TOTAL DE GALOES INTEIROS
#custo_total_galoes = galoes_int * custo_galao
##print(f'Custo de galao(oes) inteiro(s): {custo_total_galoes:.2f} R$')
##print('')
#
#print('------------OUTPUT--------------')
#print('')
#
###### CUSTO TOTAL MISTO
#custo_total_misto_lg = ((lat_int_area * custo_lata) + (resto_galeado * custo_galao ))
#
#
######################### OUTPUT ###############################
#
#
###### DIVISAO IMPERFEITA DE AREA TOTAL  >= LATA(S) INTEIRA(S) + SOBRA DE AREA > SEM VANTAGEM A USAR GALAO(OES
#if latas_float > 1 and ( resto_galeavel > razao_custo_equilib_g_x_l or area_apintar % capacidade_lata == 0 ):
#    print(f'Será(ão) necessária(as) {latas_int} lata(s) e custará {custo_total_latas:.2f} R$')
#    print('')
#    print(f'Só usando {galoes_int} galao(oes), o custo total será de R$ {custo_total_galoes}')
#    print('')
#
###### DIVISAO IMPERFEITA DE AREA TOTAL  >= LATA(S) INTEIRA(S) + SOBRA DE AREA <= A VANTAGEM A USAR GALAO(OES)
#elif latas_'float > 1 and resto_galeavel <= razao_custo_equilib_g_x_l:
#    print (f'O custo total do uso misto de {lat_int_area} lata(s) e {resto_galeado} galão(ões), custará R$ {custo_total_misto_lg:.2f}')
#    print('')
#    print(f'Só usando {galoes_int} galao(oes), o custo total será de R$ {custo_total_galoes}')
#    print('')
#    print(f'Só usando {latas_int} lata(s), o custo total será de R$ {custo_total_latas}')
#    print('')
#
###### DIVISAO IMPERFEITA DE AREA TOTAL  < LATA INTEIRA + SOBRA DE AREA > SEM VANTAGEM A USAR GALAO(OES
#elif latas_int <= 1 and area_apintar > razao_custo_equilib_g_x_l :
#    print(f'Será necessário 1 lata e custará {custo_total_latas:.2f} R$')
#    print('')
#    print(f'Só usando {galoes_int} galao(oes), o custo total será de R$ {custo_total_galoes}')
#    print('')          
#
###### AREA A PINTAR COM GALAO(OES) <= A RAZAO GALAO/LATA DE AREA/CUSTO 
#elif area_apintar <= razao_custo_equilib_g_x_l:
#    print(f'Sera(ao) necessário(s) {galoes_int} galao(oes) e o custo total será {custo_total_galoes:.2f} R$')
#    print('')
#    print(f'Só usando {latas_int} lata(s), o custo total será de R$ {custo_total_latas}')
#    print('')
    

##16 Faça um programa que peça o tamanho de um arquivo para download (em MB(bytes)) e a
#velocidade de um link de Internet (em Mbps(bits - Megabits, not Megabibites)), calcule e informe o tempo
#aproximado de download do arquivo usando este link (em minutos).

#import math
#
#tamanhoArquivo = float (input('Digite o tamanho do arquivo em MB(s): '))
#larguraBanda = float (input('Digite a banda do link Mbps(s): '))
#
#tempo_total = (tamanhoArquivo * 8) /  larguraBanda
#sec = 60
#min = tempo_total / sec

#print (tempo_total)  
#print( min)
#tempos = (tamanhoArquivo * 8) / larguraBanda
#
#sec_ = 1  
#min_ = 60
#hora_ = 3600
#dia_ = 86400
#
#min_i = tempo_total / (min_)
#
##min_f = min_i //  
#
#horas_i = tempo_total / (hora_)
#
#
#dias_i = tempo_total /  (dia_)
#
#
#print(f"{dias_i:.3f} dias {horas_i:.2f} horas ou {min_i:.2f} Minutos e {tempos:.2f} Segundos")


############## Estruturas de decisão ##############


##19 Faça um Programa que peça dois números e imprima o 
#maior deles.

#fst_numb = int (input('Digite um número inteiro: '))
#sec_numb = int (input('Digite outro número inteiro: '))
#
#if fst_numb > sec_numb:
#    print(f'{fst_numb} é maior que o segundo')
#else:
#    print(f'{sec_numb} é maior que o primeiro')

    
##20 Faça um Programa que peça um valor e mostre na tela se o valor é
#positivo ou negativo.

#num = float (input('Digite um número inteiro: '))
#
#if num == 0:
#    print(f'{num} é neutro')
#
#elif num > 0:
#    print(f'{num} é postivo')
#
#elif num < 0:
#    print(f'{num} é negativo')


## 21 Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

#sex =  (input('Digite seu genêro B I O L Ó G I C O: '))
#
#if sex == 'm' or sex == 'M':
#    print(f'{sex} é masculino')
#
#elif sex == 'f' or sex == 'F':
#    print(f'{sex} é feminino')
#    
#else:
#    print(f'{sex} é não um gênero válido')


##22 Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

#letter =  input('Digite uma letra: ')
#
#vowel = ['a', 'e', 'i', 'o', 'u']
#vowel_u = [v.upper() for v in vowel]
#
#
#if (letter in vowel) or (letter in vowel_u):
#    print (f'A letra {letter.upper()} é vogal')
#
#else:
#    print (f'A letra {letter.upper()} é consoante')


## 23 Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#    A mensagem "Reprovado", se a média for menor do que sete;
#    A mensagem "Aprovado com Distinção", se a média for igual a dez.

#average_grade1 = float ( input ('Digite a primeira media do aluno: '))
#average_grade2 = float ( input ('Digite a segunda media do aluno: '))
#
#final_average_grade = (average_grade1 + average_grade2) /2 
#
#if final_average_grade == 10:
#    print ('Student Approved with distinction')
#elif final_average_grade >= 7:
#    print ('Student Approved')
#else:
#    print ('Student Repproved')

##24 Faça um Programa que leia três números e mostre o maior deles

#num1 = float ( input ('Digite o primeiro numero: '))
#num2 = float ( input ('Digite o segundo numero: '))
#num3 = float ( input ('Digite o segundo numero: '))
#
#if num1 > num2 and num3:
#    print ('O primeiro número é o maior')
#elif num2 > num3:
#    print ('O segundo número é o maior')
#else:
#    print ('O terceiro número é o maior')
        

##25 Faça um Programa que leia três números e mostre o maior e o menor deles.

num1 = float ( input ('Digite o primeiro numero: '))
num2 = float ( input ('Digite o segundo numero: '))
num3 = float ( input ('Digite o segundo numero: '))

if num1 > num2 and num3:
    print (f'{num1} primeiro número é o maior')
elif num2 > num3:
    print (f'{num2} segundo número é o maior')
else:
    print (f'{num3} terceiro número é o maior')

if num1 < num2 and num3:
    print (f'{num1} primeiro número é o menor')
elif num2 > num3:
    print (f'{num2} segundo número é o menor')
else:
    print (f'{num3} terceiro número é o menor')
