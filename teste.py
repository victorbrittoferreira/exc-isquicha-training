############## Sequential Structures ##############

##3 Faça um Programa que peça dois números e imprima a soma.

##num1 = int (input("Digite um num: "))
##num2 = int (input("Digite outro num: "))
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
# o primeiro num deverá ser inteiro, isto é: (...-1, 0, 1, ...)

#nd_numb = int (input("Digite outro número inteiro: ")) 
# o segundo num deverá ser inteiro (...-1, 0, 1, ...)

#rd_numb = int (input("Digite um número real: ")) 
# o terceiro num deverá ser natural (0, 1, ...)

#if rd_numb % 1 == 0 and rd_numb >= 0:
#    print ('ok')
#else:
#   print('nope')


#num1 = int(input("Digite um num inteiro: "))
#num2 = int(input("Digite outro num inteiro: "))
#num3 = float(input("Digite um num real: "))
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

#sex =  input(
#    'Digite seu genêro B I O L Ó G I C O: '
# ).upper()
#
#if sex == 'm':
#    print(f'{sex} é masculino')
#
#elif sex == 'f':
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

#num1 = float ( input ('Digite o primeiro num: '))
#num2 = float ( input ('Digite o segundo num: '))
#num3 = float ( input ('Digite o segundo num: '))
#
#if num1 > num2 and num1 > num3:
#    print ('O primeiro número é o maior')
#elif num2 > num1 and num2 > num3:
#    print ('O segundo número é o maior')
#else:
#    print ('O terceiro número é o maior')
        

##25 Faça um Programa que leia três números e mostre o maior e o menor deles.

#num1 = float ( input ('Digite o primeiro num: '))
#num2 = float ( input ('Digite o segundo num: '))
#num3 = float ( input ('Digite o segundo num: '))
#
#if num1 > num2 and num1 > num3:
#    print (f'{num1} primeiro número é o maior')
#elif num2 > num1 and num2 > num3:
#    print (f'{num2} segundo número é o maior')
#else:
#    print (f'{num3} terceiro número é o maior')
#
#if num1 < num2 and num1 < num3:
#    print (f'{num1} primeiro número é o menor')
#elif num2 < num1 and num2 < num3:
#    print (f'{num2} segundo número é o menor')
#else:
#    print (f'{num3} terceiro número é o menor')


##26 Faça um programa que pergunte o preço de três produtos e informe qual produto
#você deve comprar, sabendo que a decisão é sempre pelo mais barato.

#num1 = float ( input ('Digite o preço do primeiro produto: '))
#num2 = float ( input ('Digite o preço do segundo produto: '))
#num3 = float ( input ('Digite o preço do segundo produto: '))
#
#if num1 < num2 and num1 < num3:
#    print (f'O preço do primeiro é o menor, custando R$ {num1:.2f}')
#elif num2 < num1 and num2 < num3:
#    print (f'O preço do segundo é o menor, custando R$ {num2:.2f}')
#else:
#    print (f'O preço do terceiro é o menor, custando R$ {num3:.2f}')
    
## R E F A Z E R 
##27 Faça um Programa que leia três números e mostre-os em ordem decrescente.

#num1 =  ( input ('Digite o primeiro primeiro: '))
#num2 =  ( input ('Digite o segundo segundo: '))
#num3 =  ( input ('Digite o segundo terceiro: '))
#
#num_list = [num1, num2, num3]
#
##if num1 > num2 > num3:
##    print(num1, num2, num3)
##elif num1 > num3 > num2:
##    print(num1, num3, num2)
##elif num2 > num1 > num3:
##    print(num2, num1, num3)
##elif num2 > num3 > num1:
##    print(num2, num3, num1)
##elif num3 > num1 > num2:
##    print(num3, num1, num2)
##else:
##    print(num3, num2, num1)
#
#### OR 
#
## TRAINNG IT 
#num_ordered = sorted(num_list, reverse = True )
#for num in num_ordered:
#    print(len( num))


## 28 Faça um Programa que pergunte em que turno você estuda.
#Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
#Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
#"Valor Inválido!", conforme o caso.

#ask_turn = input (
#    'Digite o turno o qual estuda, isto é, M-matutino ou V-Vespertino ou N- Noturno: '
#).upper()
#
#if ask_turn == 'M':
#    print(f'Bom dia!')
#
#elif ask_turn == 'V':
#    print(f'Boa tarde!')
#    
#elif ask_turn == 'N':
#    print(f'Boa noite!')
#    
#else:
#    print(f'Período inválido')

# a stupid way to do the same thing
#if ask_turn == 'm' or ask_turn == 'M':
#    print(f'Bom dia!')
#
#elif ask_turn == 'v' or ask_turn == 'V':
#    print(f'Boa tarde!')
#    
#elif ask_turn == 'n' or ask_turn == 'N':
#    print(f'Boa tarde!')
#    
#else:
#    print(f'Período inválido')

## 29 As Organizações Tabajara resolveram dar um aumento de salário aos seus
#colaboradores e lhe contrataram para desenvolver o programa que calculará os
#reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
#seguinte critério, baseado no salário atual:
#    salários até R$ 280,00 (incluindo) : aumento de 20%
#    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    salários de R$ 1500,00 em diante :
#        aumento de 5% Após o aumento ser realizado,
#    informe na tela:
#        o salário antes do reajuste;
#        o percentual de aumento aplicado;
#        o valor do aumento;
#        o novo salário, após o aumento.

#print('')
#currSalry = float (input (
#    'Digite o quanto ganha atualmente R$ '
#))
#
#a = 280
#b = 700
#c = 1500
#
#twenty = 20
#fiften = 15
#ten = 10
#five = 5
#
#if currSalry <= a:
#    salaryPromotion = currSalry * (1 + ( twenty /100))
#    difference = salaryPromotion - currSalry
#    percentId = twenty
#           
#elif currSalry > a and currSalry <= b:
#    salaryPromotion = currSalry * (1 + ( fiften /100))
#    difference = salaryPromotion - currSalry
#    percentId = fiften
#    
#elif currSalry > b and currSalry <= c:
#    salaryPromotion = currSalry * (1 + ( ten /100))
#    difference = salaryPromotion - currSalry
#    percentId = ten
#    
#elif currSalry > c:
#    salaryPromotion = currSalry * (1 + ( five /100))
#    difference = salaryPromotion - currSalry
#    percentId = five
#    
#print('')
#print(f' - Aplicado percentual de { percentId }%') 
#print(f' - Acrescentado R$ {difference:.2f} ')
#print(f' - Tolizando R$ {salaryPromotion:.2f} ')
    
######## ANOTHER WAWY

#salario_anterior = float(input("Digite seu salário atual: "))
#salario_atual = 0.0
#diferenca_entre_salarios = 0.0
#percentual_de_aumento = 0.0
#
#if salario_anterior <= 280:
#    percentual_de_aumento = 20
#elif salario_anterior <= 750:
#    percentual_de_aumento = 15
#elif salario_anterior <= 1500:
#    percentual_de_aumento = 10
#else:
#    percentual_de_aumento = 5
#
#diferenca_entre_salarios = salario_anterior * (percentual_de_aumento / 100)
#
#salario_atual = salario_anterior + diferenca_entre_salarios
#
#print(f"Seu salário antes do reajuste era de R${salario_anterior:.2f}")
#print(f"Seu salário foi aumentado em {percentual_de_aumento}%")
#print(f"Seu salário foi aumentado em R${diferenca_entre_salarios:.2f}")
#print(f"Seu salário atual é de R${salario_atual:.2f}")


## 30 Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
# descontos são do Imposto de Renda, que depende do salário bruto
# (conforme tabela abaixo) e 10% para o INSS e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
# O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas
# trabalhadas no mês.

# Desconto do IR:
#     Salário Bruto até 900 (inclusive) - isento
#     Salário Bruto até 1500 (inclusive) - desconto de 5%
#     Salário Bruto até 2500 (inclusive) - desconto de 10%
#     Salário Bruto acima de 2500 - desconto de 20%
# Imprima na tela as informações, dispostas conforme o exemplo abaixo.
# No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#         Salário Bruto: (5 * 220)        : R$ 1100,00
#         (-) IR (5%)                     : R$   55,00
#         (-) INSS ( 10%)                 : R$  110,00
#         FGTS (11%)                      : R$  121,00
#         Total de descontos              : R$  165,00
#         Salário Liquido                 : R$  935,00
#
#print('')
#val_hor_trab = float (input (
#    'Digite o quanto ganha por hora R$: '
#))
#print('')
#quant_hor_trab_mes = float (input (
#    'Digite o quantas horas trabalha por mês: '
#))
#
#sal_bruto = val_hor_trab * quant_hor_trab_mes
#print(f'Salario Bruto R$ {sal_bruto:.2f}')
#print('')
#
##
#
#inss = 10
#fgts = 11
#
#if sal_bruto <= 900:
#    ir = 0
#elif sal_bruto <= 1500:
#    ir = 5
#elif sal_bruto <= 2500:
#    ir = 10
#else:
#    ir = 20
#
##
#
##desc_ir = sal_bruto * (1 - (ir/100))
#desc_ir = sal_bruto * (ir/100)
#
#desc_inss = (sal_bruto - desc_ir) * (inss/100)
#
#desc_fgts = (sal_bruto - desc_ir - desc_inss) * (fgts/100)
#
##
#
#total_descontos = desc_ir + desc_inss + desc_fgts
#
#sal_liquido = sal_bruto - total_descontos
#
#print(f'IR   % {ir} - R$ {desc_ir:.2f}')
#print(f'INSS % {inss} - R$ {desc_inss:.2f}')
#print(f'FGTS % {fgts} - R$ {desc_fgts:.2f}')
#print('')
#print(f'Total de descontos = R$ {total_descontos:.2f}')
#print('')
#print(f'Salario Liquido R$ {sal_liquido:.2f}')
#print('')


## 31 Faça um Programa que leia um número e exiba o dia correspondente da semana.
#(1-Domingo, 2- Segunda, etc.),
#se digitar outro valor deve aparecer valor inválido.

#print('')
#qual_dia = int (input (
#    'Digite digite o número do dia da semana: '
#))
#
#semana = ['','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado' ]
#
#if qual_dia == 0 or qual_dia >= 8:
#        print('INVÁLIDO')
#        
#else:
#    print(f'O dia da semana é:',semana[qual_dia])

## A BETTER WAY
    
#print('')
#qual_dia = int (input ('Digite digite o número do dia da semana: '))
#
#dias_semana = ['0','Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado' ]
#
#def  dia_semana(qual_dia):
#
#    if not 1 <= qual_dia <= 7:
#        #return 'Dia INEXISTENTE
#        print(f'O dia "{qual_dia}" da semana é inexistente!')
#
#    else:
#        print(f'O dia "{qual_dia}" da semana é {dias_semana[qual_dia]}!')
#        
#dia_semana(qual_dia)


#print (f'y {dia_semana(qual_dia)}')

#print('')
#print(f'O dia da semana é {dia_semana(qual_dia)}')    
    

##32 Faça um programa que lê as duas notas parciais obtidas por um aluno numa
#disciplina ao longo de um semestre, e calcule a sua média.
#A atribuição de conceitos obedece à tabela abaixo:
#    Média de Aproveitamento  Conceito
#    Entre 9.0 e 10.0         A
#    Entre 7.5 e 9.0          B
#    Entre 6.0 e 7.5          C
#    Entre 4.0 e 6.0          D
#    Entre 4.0 e zero         E
#O algoritmo deve mostrar na tela as notas, a média,
#o conceito correspondente e a mensagem “APROVADO” se o conceito for A, B ou C
#ou “REPROVADO” se o conceito for D ou E.

#print('')
#nota1 = float (input ('Digite digite a primeira nota: '
#))
#
#print('')
#nota2 = float (input ('Digite digite a segunda nota: '
#))
#
#### MEDIA
#
#media = (nota1 + nota2) / 2
#
#letra = ''
#
#if media >= 9:
#    letra = 'A'
#    
#elif media >= 7.5:
#    letra = 'B'
#
#elif media >= 6:
#    letra = 'C'
#
#elif  media >= 4:
#    letra = 'D'
#else:
#    letra = 'E'
#    
### CATEGORIA
#    
##aprovado = ['A', 'B', 'C']
#reprovado = ['D', 'E']
#
#if letra in reprovado:
#    print(f'Aluno REPROVADO \n Nota: {letra}\n Média: {media:.2f}')
#else:
#    print(f'Aluno APROVADO \n Nota: {letra}\n Média: {media:.2f}')


## 33 Faça um Programa que peça os 3 lados de um triângulo.
#O programa deverá informar se os valores podem ser um triângulo.
#Indique, caso os lados formem um triângulo, se o mesmo é:
#    equilátero, isósceles ou escaleno.


#print('')
#lado1 = float (input ('Digite digite a media do primeiro lado: '
#))
#
#print('')
#lado2 = float (input ('Digite digite a media do segundo lado: '
#))
#
#print('')
#lado3 = float (input ('Digite digite a media do terceiro lado: '
#))
#
#
### Conceito geral de triangulo
#
#if (lado1 + lado2 > lado3
#    and lado1 + lado3 > lado2
#    and lado3 + lado2 > lado1
#):
#    #EQUILATERO
#    if lado1 == lado2 == lado3:
#        print('EQUILATERO')
#        
#    #ISOSCELES
#    elif (lado1 == lado2
#        or lado1 == lado3
#        or lado2 == lado3
#    ):
#        print('ISOSCELES')
#    
#    #ESCALENO:
#    else:
#        print('ESCALENO')
#
##NÃO É TRIANGULO 
#else:
#    print('Não é triangulo' )
        

## 34 Faça um programa que calcule as raízes de uma equação do segundo grau,
#na forma ax² + bx + c.
#O programa deverá pedir os valores de a, b e c e fazer as consistências,
#informando ao usuário nas seguintes situações:
#    Se o usuário informar o valor de A igual a zero, a equação não é do segundo
#        grau e o programa não deve fazer pedir os demais valores,
#        sendo encerrado;
#    Se o delta calculado for negativo, a equação não possui raízes reais.
#        Informe ao usuário e encerre o programa;
#    Se o delta calculado for igual a zero a equação possui apenas uma raiz
#        real; informe-a ao usuário;
#    Se o delta for positivo, a equação possui duas raiz reais;
#        informe-as ao usuário;

#print('')
#a = float (input ('Digite digite o valor de a: '
#))
#
#print('')
#b = float (input ('Digite digite o valor de b: '
#))
#
#print('')
#if a == 0:
#c = float (input ('Digite digite o valor de c: '
#))
#
### uma maneira de achar a raiz quadra ( 1 / 2) / ou raiz cubica = 1 / 3
#sqrt = 1 / 2
#
#delta = (b ** 2) - (4 * a * c)
#
#raiz1 = ( ( (- b ) + ( delta ** sqrt ) ) / ( 2 * a ) )
#raiz2 = ( ( (- b ) - ( delta ** sqrt ) ) / ( 2 * a ) )
#
#    print('Não é uma equação de segundo grau')
#
#elif delta < 0:
#    print ('A equação não possui raizes reais')
#    
#elif delta == 0:
#          print (f'A equação possui raizes iguais e reais R1: {raiz1:.2f}')
#
#else:
#    print (f'A equação possui duas raizes reais\n R1:{raiz1:.2f} \nR2: {raiz2:.2f}')
    
## melhorar o processamento

#print('')
#a = float (input ('Digite digite o valor de a: '
#))
#if a == 0:
#    print('Não é uma equação de segundo grau ')
#    
#else:
#    print('')        
#    b = float (input ('Digite digite o valor de b: '))
#    print('')
#    c = float (input ('Digite digite o valor de c: '))
#
#    delta = (b ** 2) - (4 * a * c)
#    
#    if delta < 0:
#        print ('A equação não possui raizes reais')
#
#    elif delta == 0:
#        raiz = - b / 2 * a
#        print (
#            f'A equação possui raizes iguais\n reais R1: {raiz:.2f}')
#
#    else:
#        sqrt = 1 / 2
#        
#        raiz1 = ( ( (- b ) + ( delta ** sqrt ) ) / ( 2 * a ) )
#        raiz2 = ( ( (- b ) - ( delta ** sqrt ) ) / ( 2 * a ) )
#        print (
#            f'A equação possui duas raizes reais\nR1:  {raiz1:.2f} \nR2: {raiz2:.2f}')


## 35 Faça um Programa que peça um número correspondente a um determinado ano e em
#seguida informe se este ano é ou não bissexto.

## CONTINUAR

#print('')
#ano = int (input ('Digite digite o ano: '))
#print('')
#mes = int ( input ('Digite o mês '))
#print('')
#
#dias_meses = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#meses = [ 0 , 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 
#        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
#
#def ano_bissexto(ano):
#    if ano % 4 == 0 and ( ano % 100 != 0 or ano % 400 == 0):
#        print(f'O ano {ano} é bissexto')
#    else:
#        print(f'O ano {ano} não é bissexto')
#        
#        
#ano_bissexto(ano)
#
#
#def dias_mes(ano, mes):
# #   """Return number of days in that month in that year."""
#    if not 1 <= dias_meses <= 12:
#        print('O mês {mes} é inexistente!')
#
#    if dias_meses == 2 and ano_bissexto(ano):
#        return 29
#
#    return dias_meses[month]

#def days_in_year(days. month):
#   return (month_days)

#print(f'O mês {days_in_month(year, month)} dias do ano de {(is_leap(year))}')
#print (days_in_month(2020, 9))
#print (ano_bissexto(2020))
#print(day_in_year(2020))


## 36 Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma
#é uma data válida.

print('')
#date =  input ('Digite digite a data no formato dd/mm/aaaa: ')

date = '23/09/1991'

##elements are equal math   x = x
day, month, year = date.split('/')

day, month , year = int(day) , int(month) , int (year)                        

#print(1 <= day <= 31)


def date_checker (day, month, year):
day_checker = 1 <= day <= 31
        #raise ValueError ('Dia inválido')
    #    return False    
    #print('True')
    #return True

    #def day_checker(day):
    #    if not 1 <= day <= 31:
    #        #raise ValueError ('Dia inválido')
    #        return False    
    #    #print('True')
    #    return True
month_checker =  1 <= month <= 12
#            #raise ValueError ('Mês inválido')
#            return False
#        return True
year_checker =  1 <= year
#            #raise ValueError ('Ano inválido')
#            return False    
#        return True
#        print(day_checker(day))
#        print(month_checker(month))
#        print(year_checker(year))
    #print(date_checker (day_checker, month_checker, year_checker ))
    
    
    
    #if day_checker and month_checker and year_checker== True:
    if day_checker and month_checker and year_checker == True:
        print('Data válida')
    else:
        print('Data inválida')
            
            
date_checker (day_checker, month_checker, year_checker )

#print (day_checker)
#print (month_checker)
#print (year_checker)





############################

#if ( day_checker(day) and month_checker(month) and year_checker(year)) == True:
#    print ('Data valida')
#    
#else: print ('Data invalida')


#def day_checker(day):
#    if not 1 <= day <= 31:
#        return False
#    return True
#def month_checker(month):
#    if not 1 <= month <= 12:
#        return False
#    return True
#def year_checker(year):
#    if not 1 <= year:
#        return False    
#    return True
#
#if ( day_checker(day) and month_checker(month) and year_checker(year)) == True:
#    print ('Data valida')
#    
#else: print ('Data invalida')

    #if year == 0:
    #    return False
    #if  1 > year:
    #    #return f'{year} B.C.'
    #    return True
    #return f'{year} A.D.'
