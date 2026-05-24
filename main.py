import requests
import time

def buscar_cotacoes():
    try:
        resposta = requests.get("https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
        dados = resposta.json()
        print("Resposta da API:", dados)
    except Exception as e:
        print(f"Erro: {e}")

while True:
    buscar_cotacoes()
    time.sleep(30)