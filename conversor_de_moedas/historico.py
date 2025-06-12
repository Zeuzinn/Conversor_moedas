class SalvarHistorico:
    def __init__(self):
        self.caminho_arquivo = 'historico.txt'

    def registrar_em_arquivo(self, texto: str):
        # Abre (ou cria) o arquivo .txt e adiciona o resultado da conversão
        with open (self.caminho_arquivo, "a", encoding="UTF-8") as arquivo:
            arquivo.write(texto + "\n")
            arquivo.write('-' *40 + "\n")


