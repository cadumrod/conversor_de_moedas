from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ui_app import Ui_MainWindow
from forex_python.converter import CurrencyRates
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.box_quantidade.setAlignment(Qt.AlignCenter)
        self.setWindowTitle("Conversor de moedas")
        
        # Inicializar o conversor de moedas
        self.converter = CurrencyRates()
        
        # Conectar o botão de conversão à função de conversão
        self.converter_btn.clicked.connect(self.converter_moeda)
        
        # Preencher as caixas de combinação com as moedas disponíveis
        self.preencher_caixas_combinacao()

    def preencher_caixas_combinacao(self):
        # Limpar as caixas de combinação
        self.box_base.clear()
        self.box_alvo.clear()
        
        # Obter as moedas disponíveis
        moedas_disponiveis1 = list(self.converter.get_rates('USD').keys()) + ['USD']
        moedas_disponiveis2 = list(self.converter.get_rates('BRL').keys()) + ['BRL']
        
        # Preencher as caixas de combinação com as moedas disponíveis
        self.box_base.addItems(moedas_disponiveis1)
        self.box_alvo.addItems(moedas_disponiveis2)

    def converter_moeda(self):
        # Obter as moedas selecionadas e a quantidade
        moeda_base = self.box_base.currentText().upper()
        moeda_alvo = self.box_alvo.currentText().upper()
        quantidade_str = self.box_quantidade.text()

        # Substituir ',' por '.'
        quantidade_str = quantidade_str.replace(',', '.')

        # Converter para float
        try:
            quantidade = float(quantidade_str)
        except ValueError:
            print("Erro: A quantidade inserida não é um número válido.")
            return

        # Realizar a conversão de moeda
        try:
            quantia_convertida = self.converter.convert(moeda_base, moeda_alvo, quantidade)
        except Exception as e:
            print(f"Erro ao converter moeda: {e}")
            return

        # Exibir o resultado na caixa de texto
        self.box_resultado.setPlainText(f"{quantidade} {moeda_base} equivale a \naproximadamente {quantia_convertida:,.2f} {moeda_alvo}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
