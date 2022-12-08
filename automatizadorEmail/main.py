# pip install yfinance  ~> Biblioteca do Yahoo Finance

# pip install pyautogui ~> Biblioteca para automação
# pip install pyperclip

import yfinance

# Passo 1: buscar dados dos valores das ações de forma automática no site do Yahoo Finanças
dados = yfinance.Ticker("PETR4.SA").history("6mo") # 6mo = 6 meses
dados
dados.Close # Mostra os dados da coluna Close

fechamento = dados.Close
fechamento

fechamento.plot() # Gráfcio estático

ticker = input("Digite a sigla da ação desejada: ")
dados = yfinance.Ticker(ticker).history("6mo")
grafico = fechamento.plot()
print(grafico)

# Passo 2: gerar as análises solicitadas pelo gestor de forma automática
maxima = fechamento.max()
maxima # Cotação máxima
minima = fechamento.min()
minima # Cotação mínima
atual = fechamento[-1]
atual # Cotação atual

# Passo 3: enviar um email automaticamente para o gestor com os resultados das análises
import pyautogui
import pyperclip

# Descobrir a posição do mouse
# import time
# time.sleep(5)
# pyautogui.position()

pyautogui.PAUSE = 6

pyautogui.hotkey("ctrl","t") # abrir umanova aba e digitar o endereço do gmail
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
pyautogui.click(x=1431, y=206) # clicar no botão Escrever

pyperclip.copy("phelipediogo@hotmail.com") # preencher o email do destinatario
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises Diárias") # preencher o assunto
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

mensagem = f"""
Prezado Gestor, 

Seguem as análises dos últimos 6 meses da ação {ticker}:

Cotação máxima: R$ {round(maxima, 2)}
Cotação mínima: R$ {round(minima, 2)}
Cotação atual: R$ {round(atual, 2)}
"""
pyperclip.copy(mensagem) 
pyautogui.hotkey("ctrl","v") # escrever o email

pyautogui.click(x=2182, y=705) # clicar em Enviar

print("Email enviado com sucesso!")