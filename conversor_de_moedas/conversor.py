import requests
from .data_hora import Horario


class ConversorMoeda:
    def __init__(self):
        self._taxas = {}
        self.atualizar_taxas()
    
    def atualizar_taxas(self):
        url = "http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
        resposta = requests.get(url)
        dados = resposta.json()
        
        # Armazena apenas os valores de 'bid' como float
        self._taxas = {
            'USD': float(dados['USDBRL']['bid']),
            'EUR': float(dados['EURBRL']['bid']),
            'BTC': float(dados['BTCBRL']['bid']),
        }

    def converter(self, valor_em_reais: float, moeda: str):
        moeda = moeda.upper()
        if moeda not in self._taxas:
            # Lança um erro se a sigla da moeda não existir
            raise ValueError(f"Moeda '{moeda}' não suportada.") 
        
        horario = Horario()
        hora_atual, data_atual= horario.obter_horario()
        
        taxa = self._taxas[moeda]
        convertido = valor_em_reais / taxa
        simbolo = self._cifrao(moeda)
        
        if moeda == 'BTC':
            return (
                f"Data: {data_atual} | Horário: {hora_atual}\n"
                f"R${valor_em_reais:.2f} - Convertido: {simbolo}{convertido:.6f}"
        )
        else:
            return (
                f"Data: {data_atual} | Horário: {hora_atual}\n"
                f"R${valor_em_reais:.2f} - Convertido: {simbolo}{convertido:.2f}"
        )
    
    def _cifrao(self, moeda:str):
        simbolos = {
        'USD': '$',
        'EUR': '€',
        'BTC': '₿'
    }
        simbolo = simbolos.get(moeda, '')
        
        return simbolo