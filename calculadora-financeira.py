import sys
from locale import currency
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QTableWidgetItem as Item

class CalculadoraFinanceira(QtWidgets.QMainWindow):
    def __init__(self):
        super(CalculadoraFinanceira, self).__init__()
        uic.loadUi('calculadora-financeira-gui.ui', self)
        # Connecting signals
        self.simular.clicked.connect(self._simular_click)

    def _simular_click(self, button):
        # When the user clicks in the "simular" button
        # erase previous simulations
        for i in range(self.tabela.rowCount()):
            self.tabela.removeRow(0)

        # retrieve and validate data
        valor, taxa, parcelas = [field.value() for field in [self.valor, self.taxa, self.parcelas]]
        taxa = taxa/100
        financing_methods = {
            self.sac.isChecked(): self._sac_simulation,
            self.price.isChecked(): self._price_simulation,
        }

        # generate rows according to the selected simulation and given data
        rows = financing_methods[True](valor, taxa, parcelas)
        # the rows will be added to the table
        for row in rows:
            self._add_row_to_table(*row)

    def _add_row_to_table(self, parcela, valor_prestacao, amortizacao, juros, saldo_devedor):
        index = parcela
        self.tabela.insertRow(index)
        # parcela
        self.tabela.setItem(index, 0, Item(str(parcela)))
        # monetary values
        for i, value in enumerate([valor_prestacao, amortizacao, juros, saldo_devedor]):
            self.tabela.setItem(index, i + 1, Item(('R$ ' + currency(value, False, True)) if value != '' else ""))

    def _sac_simulation(self, valor, taxa, parcelas):
        rows = [(0, '', '', '', valor)]
        amortizacao = valor/parcelas

        for i in range(parcelas):
            ultimo_saldo = rows[i][-1]
            juros = ultimo_saldo*taxa
            prestacao = amortizacao + juros
            saldo = ultimo_saldo - amortizacao

            rows.append((i + 1, prestacao, amortizacao, juros, saldo))

        return rows

    def _price_simulation(self, valor, taxa, parcelas):
        rows = [(0, '', '', '', valor)]
        m = (1 + taxa)**parcelas
        prestacao = (valor*taxa*m)/(m - 1)

        for i in range(parcelas):
            ultimo_saldo = rows[i][-1]
            juros = ultimo_saldo*taxa
            amortizacao = prestacao - juros
            saldo = ultimo_saldo - amortizacao

            rows.append((i + 1, prestacao, amortizacao, juros, saldo))

        return rows

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = CalculadoraFinanceira()
    window.show()
    sys.exit(app.exec_())

