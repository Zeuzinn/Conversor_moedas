import requests


def moeda_usd(reais: float, dados:dict):
    dolar = float(dados['USDBRL']['bid'])
    return reais / dolar


def moeda_eur(reais: float, dados:dict):
    euro = float(dados['EURBRL']['bid'])
    return reais / euro


def moeda_btc(reais: float, dados:dict):
    btc = float(dados['BTCBRL']['bid']) # Bitcoin
    return reais / btc 


def obter_valor():
    try:
        valor = float(input("Valor em reais: "))
        if valor < 0:
            print("O valor para conversão deve ser maior que R$0,00 \n")
            return
        
        return valor    
    except ValueError:
        print("Erro: Deve ser inserido apenas o valor.\n")
        return None
    

def main():
    while True:
        # Sempre que repetir o loop, atualiza o conversor com os dados mais recentes da API
        url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        resposta = requests.get(url)
        dados = resposta.json()

        print("\n=== CONVERSOR DE MOEDAS ===\n")    
        reais = obter_valor()
        if reais is None:
            continue
        
        conversor = input("Converter para (USD, EUR, BTC...): ").upper()

        if conversor == "USD":
            convertido = moeda_usd(reais, dados)
            print(f"R${reais:.2f} - ${convertido:.2f}")

        elif conversor == "EUR":
            convertido = moeda_eur(reais, dados)
            print(f"R${reais:.2f} - €{convertido:.2f}")   

        elif conversor == "BTC":
            convertido = moeda_btc(reais, dados)
            print(f"R${reais:.2f} - Bitcoin:{convertido:.6f}")

        else:
            print("Moeda não suportada no momento.")
        
        opcao = input("Deseja converter outro valor? (S/N): ").strip().upper()
        if opcao != "S":
            print("Programa encerrado.")
            break