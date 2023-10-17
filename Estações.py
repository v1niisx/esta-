#Verfifica estação
#Entradas
dat = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))
#Processamento
if mes == 12 and dat >= 22 or mes == 1 or mes == 2 or mes == 3 and dat <=20 or mes == 3:
    print('Você nasceu no Verao')
elif mes == 3 and dat >= 21 or mes == 4 or mes == 5 or mes == 6 and dat <= 21 or mes == 6:
    print('Você nasceu no outono')
elif mes == 6 and dat <= 21 or mes == 7 or mes == 8 or mes == 9 or mes == 9 and dat <= 23:
    print('Você nasceu no inverno')
elif mes == 9 and dat >=23 or mes == 9 or mes == 10 or mes == 11 or mes == 12 or mes == 12 and dat <= 22:
    print('Você nasceu na primavera')
else:
    print('invalido')