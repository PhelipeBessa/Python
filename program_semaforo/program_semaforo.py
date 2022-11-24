#O programa deve indicar uma ação com base no semáforo
#CS = Cor do semáforo
#DC = Distância do Cruzamento 

print('Indique o que o motorista deve fazer de acordo com a cor do semáforo (CS) e com a distância do')
print('cruzamento (DC) fornecidos pelo usuário.\n')
print('Se o sinal estiver ' + '\033[91m' + '(V) Vermelho' + '\033[0m' + ' o motorista deve parar.') # '\033[91m' RED
print('Se o sinal estiver ' + '\033[93m' + '(A) Amarelo' + '\033[0m' + ' e a distânia for menor que 5m o motorista deve passar com cuidado,') # '\033[93m' YELLOW
print('se a distância for maior ou igual a 5m o motorista deve parar.')
print('Se o sinal estiver ' + '\033[92m' + '(V) Verde' + '\033[0m' + ' o motorista pode passar.\n')


    
print("Opções:")
print('1 - Vermelho')
print('2 - Amarelo')
print('3 - Verde\n')

cs = int(input('Escolha a cor do sinal: '))

match cs:
    case 1:
        if cs == 1:
            print('Sinal ' + '\033[91m' + 'Vermelho.' + '\033[0m' + ' PARE!!!')
    case 2:
        if cs == 2:
            print('Sinal ' + '\033[93m' + 'Amarelo.' + '\033[0m' + ' \n')
            dc = int(input('A que velocidade você está: '))
            if dc <= 5:
                print('Passe com cuidado.')
            else:
                print('PARE!!!')
    case 3:
        if cs == 3:
            print('Sinal ' + '\033[92m' + 'Verde.' + '\033[0m' + ' Pode passar.')
    case _:
        print('Opção inválida!')

  