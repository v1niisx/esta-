#Verfifica estação do ano

print('\n\t\t --- Estação do Ano --- \n\t\t')

#Entradas
dat = int(input('Digite o dia: '))
mes = int(input('Digite o mes: '))
ano = int(input('Digite o ano: '))

#Processamento

if mes == 1 or mes == 2 or mes == 3:
    print('Você nasceu no Verao')
elif mes == 4 or mes == 5 or mes == 6:
    print('Você nasceu no outono')
elif mes == 7 or mes == 8 or mes == 9:
    print('Você nasceu no inverno')
elif mes == 10 or mes == 11 or mes == 12:
    print('Você nasceu na primavera')
else:
    print('invalido')
