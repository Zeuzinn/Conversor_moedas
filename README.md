# 💱 Conversor de Moedas com API

Este é um projeto simples em Python que utiliza a [AwesomeAPI](https://docs.awesomeapi.com.br/api-de-moedas) para converter valores de reais (BRL) para outras moedas como:

- 💵 Dólar americano (USD)
- 💶 Euro (EUR)
- 💰 Bitcoin (BTC)

## ✅ Funcionalidades

- Entrada interativa de valor em Reais
- Escolha da moeda de destino
- Cotação em tempo real com a AwesomeAPI
- Cálculo automático do valor convertido
- Validação de entrada (valores negativos ou inválidos)
- Loop contínuo até o usuário decidir sair

## ▶️ Como usar

Clone o repositório e execute o script com Python:

```bash
git clone https://github.com/zeuzinn/Conversor_moedas.git

cd conversor-moedas-api
python main.py
```

## 🖥️ Exemplo de uso
```
=== CONVERSOR DE MOEDAS ===

Valor em reais: 100
Converter para (USD, EUR, BTC...): USD
R$100.00 - $18.87
```

## 📦 Requisitos
Python 3.7+

Biblioteca `requests` 

## 📁 Estrutura do projeto
```
conversor-moedas-api/
├── conversor_de_moedas/
│   ├── __init__.py
│   └── conversor.py
├── main.py
└── README.md
```
