# 💱 Conversor de Moedas com API

Este é um projeto simples em Python que utiliza a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para converter valores de reais (BRL) para outras moedas como:

- 💵 Dólar americano (USD)
- 💶 Euro (EUR)
- 💰 Bitcoin (BTC)

## ✅ Funcionalidades

- Entrada interativa de valor em Reais

- Escolha da moeda de destino (USD, EUR, BTC)

- Cotação em tempo real com a AwesomeAPI

- Cálculo automático do valor convertido

- Validação de entrada (valores negativos ou inválidos)

- Exibição da data e hora da conversão

- Registro do histórico em arquivo historico.txt

- Loop contínuo até o usuário decidir sair

## ▶️ Como usar

Clone o repositório e execute o script com Python:

```bash
git clone https://github.com/Zeuzinn/Conversor_moedas.git
cd conversor_de_moedas
pip install requests
python main.py

```

## 🖥️ Exemplo de uso
```
------------------------------
CONVERSOR DE MOEDAS
------------------------------
Valor em reais R$ 100
Converter para (USD, EUR, BTC...): USD

Data: 12/06/2025 | Horário: 14:23
R$100.00 - Convertido: $18.87
----------------------------------------
Deseja converter outro valor? (S/N): N

Programa encerrado.

``` 

## 📁 Estrutura do projeto
```
conversor-moedas-api/
├── conversor_de_moedas/
│   ├── __init__.py
│   ├── conversor.py
│   ├── data_hora.py
│   ├── historico.py
│   └── interacao.py
├── main.py
├── historico.txt       # É Criado após a primeira execução
└── README.md
```

## 📦 Requisitos
Python 3.7+

Biblioteca `requests`