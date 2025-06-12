from .conversor import ConversorMoeda
from .historico import SalvarHistorico

def obter_valor():
    try:
        valor_em_reais = float(input("Valor em reais R$ "))
        if valor_em_reais < 0:
            print("O valor para conversão deve ser maior que R$0,00 \n")
            return
        
        return valor_em_reais
    except ValueError:
        print("Erro: Deve ser inserido apenas o valor.\n")
        return None
    

def layout():
    print("-"*30)
    print("CONVERSOR DE MOEDAS")    
    print("-"*30)


def main():
    conversor = ConversorMoeda()
    historico = SalvarHistorico()
    
    while True:
        layout()

        valor_em_reais = obter_valor()
        if valor_em_reais is None:
            continue
        
        moeda = input("Converter para (USD, EUR, BTC...): ").upper()
        
        try:
            resultado = conversor.converter(valor_em_reais, moeda)
            historico.registrar_em_arquivo(resultado)
            print("-"*40)
            print(resultado)
            print("-"*40)

        except ValueError as e:
            print(f"Erro: {e}")
        
        opcao = input("Deseja converter outro valor? (S/N): ").strip().upper()
        print()
        
        if opcao != "S":
            print("Programa encerrado.")
            break