print('Com base na fórmula abaixo vamos converter a temperatura de Celsius para Fahrenheit.')
print('Se a temperatura em celsius for abaixo de 10 ou acima de 35 informar “PERIGO” se não, informar “OK”.')
print('\033[91m' + 'F = C * (9/5) + 32\n' + '\033[0m')  # '\033[1m' serve para inicar a cor vermelha e '\033[0m' termina o comando

tempC = float(input('Digite a temperatura em Celsius: '))

tempF = (tempC * 1.8) + 32

print('A temperatura em Fahrenheit é :', tempF)

if tempC <= 10 or tempC >= 35:
    print('\nPERIGO!!!')
else:
    print('\nTemperatura OK!!!')