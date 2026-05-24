import requests
import time
from datetime import datetime

def buscar_cotacoes():
    try:
        resposta = requests.get("https://open.er-api.com/v6/latest/USD")
        dados = resposta.json()

        dolar_brl = dados["rates"]["BRL"]
        eur_usd = dados["rates"]["EUR"]
        brl_eur = 1 / eur_usd * dolar_brl

        agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"{agora} | Dolar: R${dolar_brl:.2f} | Euro: R${brl_eur:.2f}")

    except Exception as e:
        print(f"Erro: {e}")

print("Monitorando cotacoes...")
print("="*60)

while True:
    buscar_cotacoes()
    time.sleep(300)