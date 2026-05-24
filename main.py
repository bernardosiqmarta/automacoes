import requests
import time
from datetime import datetime

def buscar_cotacoes():
    try:
        resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
        dados = resposta.json()

        dolar = float(dados["USDBRL"]["bid"])
        euro = float(dados["EURBRL"]["bid"])
        bitcoin = float(dados["BTCBRL"]["bid"])

        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{agora} | Dolar: R${dolar:.2f} | Euro: R${euro:.2f} | Bitcoin: R${bitcoin:.2f}")

    except Exception as e:
        print(f"Erro: {e}")

print("Monitorando cotacoes...")
print("="*60)

while True:
    buscar_cotacoes()
    time.sleep(300)  #a cada 5 minutos