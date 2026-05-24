import requests
import time
from datetime import datetime

def buscar_cotacoes():
    resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    dados = resposta.json()

    dolar = float(dados["USDBRL"]["bid"])
    euro = float(dados["EURBRL"]["bid"])
    bitcoin = float(dados["BTCBRL"]["bid"])

    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    linha = f"{agora} | Dolar: R${dolar:.2f} | Euro: R${euro:.2f} | Bitcoin: R${bitcoin:.2f}\n"

    print(linha)

    with open("cotacoes.txt", "a") as arquivo:
        arquivo.write(linha)

print("Monitorando cotacoes... (Ctrl+C para parar)")
print("="*60)

while True:
    buscar_cotacoes()
    time.sleep(30)